let _ =
  let n,q = Scanf.scanf " %d %d" (fun x y -> (x+1,y)) in
  let wealth = Array.make n 0 and time = Array.make n 0 in
  let rec aux t defw deft =
    if t <= q then
      let c,i = Scanf.scanf " %s %d" (fun x y -> (x,y)) in
      match c with
      | "SET" ->
         let x = Scanf.scanf " %d" (fun x -> x) in
         wealth.(i) <- x;
         time.(i) <- t;
         aux (t+1) defw deft
      | "RESTART" ->
         aux (t+1) i t
      | _ ->
         Printf.printf "%d\n" (if time.(i) > deft then wealth.(i) else defw);
         aux (t+1) defw deft
  in aux 1 0 0
