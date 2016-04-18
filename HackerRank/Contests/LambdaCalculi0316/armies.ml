(*
  Maintaining a sorted list of couples (value, nb of soldiers) is not efficient enough
  as insertion will be O(n).
  Using OCaml Map module is not efficient enough either...
  We use custom binary heaps relying on custom dynamic tables (as the heaps can be very large
  it is not possible to allocate statically enough space).
  Heap merges are:
    - in O(n log n) for a naive element-by-element insertion
    - in O(n), but with additional memory operations, for a new heapification of the
      concatenation of the tables of both heaps
  But this still too slow (for 1 testcase), hence merges will be stored in "pending merges" lists and will only
  be recursively applied when needed by a pop.
*)

(*
  Classic dynamic table
  size*2 when needed>size
  size/2 when needed<size/4
*)
module DynTable = struct
  type 'a t = { mutable real_size : int;
		mutable virtual_size : int;
		mutable table : 'a array; }

  exception Empty_table
    
  let size : 'a t -> int = fun dt ->
    dt.virtual_size

  let make : int -> 'a -> 'a t = fun n x ->
    if n<=0 then
      { real_size = 1; virtual_size = 0; table = Array.make 1 x; }
    else
      { real_size = n; virtual_size = n; table = Array.make n x; }

  let resize : 'a t -> int -> unit = fun dt n ->
    dt.real_size <- n;
    let nt = Array.make dt.real_size dt.table.(0) in
    for i=1 to dt.virtual_size-1 do
      nt.(i) <- dt.table.(i)
    done;
    dt.table <- nt

  let lazy_resize : 'a t -> int -> unit = fun dt n ->
    if dt.real_size<n then resize dt n
      
  let expand : 'a t -> unit = fun dt ->
    resize dt (dt.real_size lsl 1)

  let shrink : 'a t -> unit = fun dt ->
    resize dt (dt.real_size lsr 1)

  let get : 'a t -> int -> 'a = fun dt i ->
    dt.table.(i mod dt.virtual_size)
      
  let set : 'a t -> int -> 'a -> unit = fun dt i x ->
    dt.table.(i mod dt.virtual_size) <- x
      
  let push : 'a t -> 'a -> unit = fun dt x ->
    if dt.virtual_size=dt.real_size then expand dt;
    dt.table.(dt.virtual_size) <- x;
    dt.virtual_size <- dt.virtual_size+1

  let pop : 'a t -> 'a = fun dt ->
    if dt.virtual_size=0 then raise Empty_table;
    dt.virtual_size <- dt.virtual_size-1;
    let result = dt.table.(dt.virtual_size) in
    if dt.virtual_size>0 && (dt.virtual_size lsl 2)<=dt.real_size then shrink dt;
    result
end


  
module type OrderedType = sig
  type t
  val compare : t -> t -> int
end

  
(* Binary heaps using dynamic tables *)
module BinHeap(Ord : OrderedType) = struct
  type t = { mutable size : int;
	     table : Ord.t DynTable.t; }

  exception Empty_heap
    
  let init : Ord.t -> t = fun x ->
    { size = 0; table = DynTable.make 0 x; }

  let size : t -> int = fun bh ->
    bh.size
      
  let get : t -> int -> Ord.t = fun bh i ->
    DynTable.get bh.table i

  let get_table : t -> Ord.t DynTable.t = fun bh ->
    bh.table
      
  let set : t -> int -> Ord.t -> unit = fun bh i x ->
    DynTable.set bh.table i x

  let rec up : t -> int -> unit = fun bh p ->
    if p>0 then begin
      let vp = get bh p in
      let q = (p-1)/2 in
      let vq = get bh q in
      if (Ord.compare vp vq)<0 then begin
	set bh p vq;
	set bh q vp;
	up bh q
      end
    end
    
  let push : t -> Ord.t -> unit = fun bh x ->
    DynTable.push bh.table x;
    bh.size <- bh.size+1;
    up bh (bh.size-1)

  let rec down : t -> int -> unit = fun bh p ->
    let g = 2*p+1 in
    if g<bh.size then begin (* there is a left child *)
      let vp = get bh p in
      let vg = get bh g in
      let d = g+1 in
      if d<bh.size && (Ord.compare vg (get bh d))>0 then begin
	(* there is a right child smaller than the left *)
	if (Ord.compare vp (get bh d)>0) then begin
	  set bh p (get bh d);
	  set bh d vp;
	  down bh d
	end
      end
      else if (Ord.compare vp vg)>0 then begin
	set bh p vg;
	set bh g vp;
	down bh g
      end
    end
      
  let pop : t -> Ord.t = fun bh ->
    if bh.size=0 then raise Empty_heap;
    let result = get bh 0 in
    let last = DynTable.pop bh.table in
    bh.size <- bh.size-1;
    if bh.size>0 then begin
      set bh 0 last;
      down bh 0
    end;
    result

  (*
    Convert a table to a heap in O(n)
    (instead of O(n log n) using n insertions)
  *)
  let heapify : Ord.t DynTable.t -> t = fun dt ->
    let bh = { size = DynTable.size dt; table = dt; } in
    for p=bh.size/2 downto 0 do
      down bh p
    done;
    bh   
end

module Int = struct
  type t = int
  let compare x y = y-x
end

module IntHeap = BinHeap(Int)

(*
  Merging armies efficiently:
  - basic O(n log n) merge by inserting elements one by one for small army
  - theoretically efficient O(n) merge (but implies some memory realloc) by
    concatening armies and re-heapifying the table for large army
*)
let merge armies i j =
  let ais = IntHeap.size armies.(i-1) in
  let ajs = IntHeap.size armies.(j-1) in
  let ni,nj,ais,ajs = if ais>ajs then i,j,ais,ajs else j,i,ajs,ais in
  if ajs>175 then begin
    let dt = IntHeap.get_table armies.(ni-1) in
    DynTable.lazy_resize dt (ais+ajs);
    for k=0 to ajs-1 do
      DynTable.push dt (IntHeap.get armies.(nj-1) k)
    done;
    armies.(ni-1) <- IntHeap.heapify dt
  end
  else for k=0 to ajs-1 do
      IntHeap.push armies.(ni-1) (IntHeap.get armies.(nj-1) k)
    done;
  armies.(i-1) <- armies.(ni-1)

(* Apply pending merges *)
let rec apply_merges armies merges i =
  if merges.(i-1)<>[] then begin
    List.iter (fun j -> apply_merges armies merges j; merge armies i j) merges.(i-1);
    merges.(i-1) <- []
  end
    
let _ =
  let n,q = Scanf.scanf " %d %d" (fun x y -> (x,y)) in
  let armies = Array.init n (fun _ -> IntHeap.init 0) in
  let merges = Array.make n [] in (* pending merges *)
  let maxes = Array.make n (-1) in (* max of each army *)
  for k=0 to q-1 do
    let com,i = Scanf.scanf " %d %d" (fun x y -> (x,y))  in
    if com=1 then Printf.printf "%d\n" maxes.(i-1)
    else if com=2 then begin
      apply_merges armies merges i; (* we only apply the pending merges here *)
      ignore (IntHeap.pop armies.(i-1));
      if (IntHeap.size armies.(i-1))>0 then
	maxes.(i-1) <- IntHeap.get armies.(i-1) 0
      else
	maxes.(i-1) <- -1
    end
    else if com=3 then begin
      let c = Scanf.scanf " %d" (fun x -> x)  in
      IntHeap.push armies.(i-1) c;
      if maxes.(i-1)<c then maxes.(i-1) <- c
    end
    else begin
      let j = Scanf.scanf " %d" (fun x -> x)  in
      merges.(i-1) <- j::merges.(i-1); (* we add a pending merge *)
      if maxes.(i-1)<maxes.(j-1) then maxes.(i-1) <- maxes.(j-1)
    end
  done
