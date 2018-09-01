type inoeud =
  {
    mutable v : int;
    mutable p : inoeud option;
    mutable c : inoeud list;
  }
(*and arbre = Vide | Noeud of inoeud*)

let get = function
  | Some x -> x
  | _ -> failwith "get"
    
let mono_tree x p =
  {v=x; p=Some p; c=[];}
    
let init_tree () =
  {v=0; p=None; c=[];}

let changeValue a x =
  a.v <- x; a

let print a =
  Printf.printf "%d\n" a.v; a
    
let rec aux_visitLeft a = function
  | b::c::t when c==a -> b
  | _::t -> aux_visitLeft a t
  | _ -> failwith "vl"

let visitLeft a =
  aux_visitLeft a (get a.p).c

let rec aux_visitRight a = function
  | c::b::t when c==a -> b
  | _::t -> aux_visitRight a t
  | _ -> failwith "vr"
    
let visitRight a =
  aux_visitRight a (get a.p).c

let visitParent a =
  get a.p

let visitChild a n =
  List.nth a.c (n-1)

let delete a =
  let p = get a.p in
  p.c <- List.filter (fun x -> x!=a) p.c; p

let insertChild a x =
  a.c <- (mono_tree x a)::a.c; a

let rec aux_insertLeft p a x = function
  | b::t as l when b==a -> (mono_tree x p)::l
  | b::t -> b::(aux_insertLeft p a x t)
  | _ -> failwith "il"
    
let insertLeft a x =
  let p = get a.p in
  p.c <- aux_insertLeft p a x p.c; a
    
let rec aux_insertRight p a x = function
  | b::t when b==a -> a::(mono_tree x p)::t
  | b::t -> b::(aux_insertRight p a x t)
  | _ -> failwith "ir"
     
let insertRight a x =
  let p = get a.p in
  p.c <- aux_insertRight p a x p.c; a

    
let _ =
  let q = Scanf.scanf " %d" (fun x -> x) in
  let curr = ref (init_tree ()) in
  for j=0 to q-1 do
    let com = Scanf.scanf " %s " (fun x -> x)  in
    if com="print" then curr := print (!curr)
    else if com="delete" then curr := delete (!curr)
    else if com="change" then begin
      let x = Scanf.scanf " %d " (fun x -> x)  in
      curr := changeValue (!curr) x
    end
    else if com="visit" then begin
      let com2 = Scanf.scanf " %s " (fun x -> x)  in
      if com2="left" then curr := visitLeft (!curr)
      else if com2="right" then curr := visitRight (!curr)
      else if com2="parent" then curr := visitParent (!curr)
      else begin
	let x = Scanf.scanf " %d " (fun x -> x)  in
	curr := visitChild (!curr) x
      end
    end
    else if com="insert" then begin
      let com2,x = Scanf.scanf " %s %d " (fun x y -> (x,y))  in
      if com2="left" then curr := insertLeft (!curr) x
      else if com2="right" then curr := insertRight (!curr) x
      else if com2="child" then curr := insertChild (!curr) x
    end
  done
