(* Hashtbl.HashedType + hash_size *)
module type HashedType = sig
  type t
  val equal : t -> t -> bool
  val hash_size : int
  val hash : t -> int
end

module type HashTrie = sig
  type elt
  type htrie = Node of htrie*htrie | Leaf of elt list | Nil
  val empty : htrie
  val find : elt -> htrie -> elt
  val find_opt : elt -> htrie -> elt option
  val find_all : elt -> htrie -> elt list
  val add : elt -> htrie -> htrie
  val remove : elt -> htrie -> htrie
end

module Make(H : HashedType) : (HashTrie with type elt = H.t) = struct
  type elt = H.t
  type htrie = Node of htrie*htrie | Leaf of elt list | Nil

  let empty : htrie = Nil
                                                      
  let find : elt -> htrie -> elt = fun x tree ->
    let rec aux h t =
      let c = h land 1 and h = h lsr 1 in
      match t with
      | Nil -> raise Not_found
      | Leaf l -> List.find ((=) x) l
      | Node (l,r) -> aux h (if c=0 then l else r)
    in aux (H.hash x) tree

  let find_opt : elt -> htrie -> elt option = fun x tree ->
    try Some (find x tree)
    with Not_found -> None
     
  let find_all : elt -> htrie -> elt list = fun x tree ->
    let rec aux h t =
      let c = h land 1 and h = h lsr 1 in
      match t with
      | Nil -> []
      | Leaf l -> List.filter ((=) x) l
      | Node (l,r) -> aux h (if c=0 then l else r)
    in aux (H.hash x) tree
     
  let add : elt -> htrie -> htrie = fun x tree ->
    let rec aux h d t =
      let c = h land 1 and h = h lsr 1 in
      if d=0 then
        match t with
        | Nil -> Leaf [x]
        | Leaf l -> Leaf (x::l)
        | _ -> failwith "add"
      else
        match t with
        | Nil ->
           if c=0 then Node ((aux h (d-1) Nil), Nil)
           else Node (Nil, (aux h (d-1) Nil))
        | Leaf _ -> failwith "add"
        | Node (l,r) ->
           if c=0 then Node ((aux h (d-1) l), r)
           else Node (l, (aux h (d-1) r))
    in aux (H.hash x) H.hash_size tree

  let rec list_remove x = function
    | [] -> []
    | h::t when h=x -> t
    | h::t -> h::(list_remove x t)
     
  let remove : elt -> htrie -> htrie = fun x tree ->
    let rec aux h t =
      let c = h land 1 and h = h lsr 1 in
      match t with
      | Nil -> Nil
      | Leaf l -> Leaf (list_remove x l)
      | Node (l,r) -> begin
          match (if c=0 then aux h l else l),(if c=1 then aux h r else r) with
          | Nil,Nil -> Nil
          | l,r -> Node (l,r)
        end
    in aux (H.hash x) tree
end


(* test code for strings *)
let random_string l =
  let a = Char.code 'a' in
  String.init l (fun _ -> Char.chr (a+(Random.int 26)))

module HashedString : (HashedType with type t = string) = struct
  type t = string
  let equal = (=)
  let hash_size = 22
  let hash = Hashtbl.hash
end

module StringHTrie = Make(HashedString)

module OrderedString : (Set.OrderedType with type t = string) = struct
  type t = string
  let compare = Pervasives.compare
end

module StringSet = Set.Make(OrderedString)

let main0 () =
  let t = ref StringHTrie.empty in
  for i = 0 to 1000000 do
    let s = random_string 5 in
    t := StringHTrie.add s !t
  done

let main1 () =
  let t = ref StringSet.empty in
  for i = 0 to 1000000 do
    let s = random_string 5 in
    t := StringSet.add s !t
  done
  
let main2 () =
  let t = Hashtbl.create 1000000 in
  for i = 0 to 1000000 do
    let s = random_string 5 in
    Hashtbl.add t s ()
  done
  
let _ =
  Random.self_init ();
  main0 ()
