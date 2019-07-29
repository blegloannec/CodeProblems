module Int = struct
  type t = int
  let compare = compare
end

module IntSet = Set.Make(Int)

let sum_smooth n =
  let rec aux s n =
    if n=0 then 0
    else
      let x = IntSet.min_elt s in
      let s = IntSet.remove x s in
      let s = List.fold_left (fun s d -> IntSet.add (d*x) s) s [2;3;5] in
      x + aux s (n-1)
  in aux (IntSet.singleton 1) n

let _ =
  let v = int_of_string (input_line stdin) in
  let s = sum_smooth v in
  Printf.printf "%d\n" s
