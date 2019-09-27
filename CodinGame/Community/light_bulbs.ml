let rec switch s t =
  match s,t with
  | a::s1, b::t1 when a=b -> switch s1 t1
  | a::s1, b::t1 ->
     let one = List.mapi (fun i _ -> if i=0 then '1' else '0') s1 in
     (switch s1 one) + 1 + (switch one t1)
  | _ -> 0

let string_to_char_list s =
  List.rev (Seq.fold_left (fun l c -> c::l) [] (String.to_seq s))

let _ =
  let s = string_to_char_list (read_line ()) in
  let t = string_to_char_list (read_line ()) in
  print_int (switch s t)
