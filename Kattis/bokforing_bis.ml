(*
  Code using Hashtbl (~ same perf.)
  /!\ the initial size given to the table at creation is crucial as
      it affects the cost of Hashtbl.reset / Hashtbl.clear
*)
let _ =
  let n,q = Scanf.scanf " %d %d" (fun x y -> (x,y)) in
  let h = Hashtbl.create 10 and d = ref 0 in
  for t = 1 to q do
    let c,i = Scanf.scanf " %s %d" (fun x y -> (x,y)) in
    if c = "SET" then
      let x = Scanf.scanf " %d" (fun x -> x) in
      Hashtbl.add h i x
    else if c = "RESTART" then
      begin
        d := i;
        Hashtbl.reset h
      end
    else
      Printf.printf "%d\n" (try Hashtbl.find h i with Not_found -> !d)
  done
