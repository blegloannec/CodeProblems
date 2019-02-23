type elem = Int of int | Str of string

let elem_str : elem -> string = function
  | Int x -> string_of_int x
  | Str s -> s

let op : elem -> elem -> elem = fun a b ->
  match a,b with
  | Int x, Int y -> Int (x+y)
  | _ -> Str ((elem_str a)^(elem_str b))

let conv : string -> elem = fun s ->
  try Int (int_of_string s)
  with _ -> Str s

let pascal x =
  let e = Array.length x in
  let h = Hashtbl.create 100000 in
  let rec aux l n =
    if l = 0 then x.(n)
    else if n = 0 then x.(0)
    else if n = l+e-1 then x.(e-1)
    else
      try Hashtbl.find h (l,n)
      with Not_found ->
        let res = op (aux (l-1) (n-1)) (aux (l-1) n) in
        Hashtbl.add h (l,n) res;
        res
  in aux

let _ =
  let [e;l;n] = List.map int_of_string (String.split_on_char ' ' (read_line ())) in
  let x = Array.of_list (List.map conv (String.split_on_char ' ' (read_line ()))) in
  print_endline (elem_str (pascal x (l-1) (n-1)))
