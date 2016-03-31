let rec test = function
  | x::y::t when x=y -> false
  | x::t -> test t
  | _ -> true


let _ =
  let t = Scanf.scanf "%d" (fun x -> x) in
  for i=0 to t-1 do
    let n = Scanf.scanf " %d" (fun x -> x) in
    let l = ref [] in
    for j=0 to n-1 do
      let x = Scanf.scanf " %d %d" (fun x _ -> x)  in
      l := x::(!l)
    done;
    print_endline (if (test (List.sort compare (!l))) then "YES" else "NO")
  done
