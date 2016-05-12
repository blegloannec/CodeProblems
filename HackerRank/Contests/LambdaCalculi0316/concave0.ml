(* Incorrect : marcherait si les sommets etaient donnes DANS L'ORDRE *)
let triarea (x1,y1) (x2,y2) (x3,y3) =
  let res = (x2-.x1)*.(y3-.y1) -. (x3-.x1)*.(y2-.y1) in
  (*Printf.printf "%f\n" res;*)
  res

let sgn x = if x>=0. then 1 else -1
    
let rec concave p0 p01 = function
  | p1::p2::[] ->
     let s1 = sgn (triarea p1 p2 p0) in
     let s2 = sgn (triarea p2 p0 p01) in
     if s1=s2 then s1 else 0
  | p1::p2::p3::t ->
     let s1 = sgn (triarea p1 p2 p3) in
     let s2 = concave p0 p01 (p2::p3::t) in
     if s1=s2 then s1 else 0

let _ =
  let n = Scanf.scanf " %d" (fun x -> x) in
  let l = ref [] in
  for j=0 to n-1 do
    let x = Scanf.scanf " %f %f" (fun x y -> (x,y))  in
    l := x::(!l)
  done;
  match !l with p0::p1::t ->
  let a = concave p0 p1 (!l) in
  Printf.printf "%s\n" (if a=0 then "YES" else "NO")
