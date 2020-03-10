(* Chomp game on 3xN grid *)

let h = Hashtbl.create 15000
exception Winner
  
let rec winning c =
  try Hashtbl.find h c
  with Not_found ->
    let r1,r2,r3 = c in
    try 
      for i = 0 to r3-1 do
	if not (winning (r1,r2,i)) then raise Winner
      done;
      for i = 0 to r2-1 do
	if not (winning (r1,i,(min r3 i))) then raise Winner
      done;
      for i = 0 to r1-1 do
	if not (winning (i,(min r2 i),(min r3 i))) then raise Winner
      done;
      Hashtbl.add h c false;
      false
    with Winner ->
      Hashtbl.add h c true;
      true

let main () =
  Hashtbl.add h (0,0,0) true;
  let t = Scanf.scanf " %d" (fun x -> x) in
  for i = 1 to t do
    let c = Scanf.scanf " %d %d %d" (fun r1 r2 r3 -> (r1,r2,r3)) in
    Printf.printf "%s\n" (if winning c then "WIN" else "LOSE")
  done

let _ = main ()
