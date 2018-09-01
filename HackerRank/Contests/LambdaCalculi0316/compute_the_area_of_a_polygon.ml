let triarea (x1,y1) (x2,y2) (x3,y3) =
  0.5 *. ((x2-.x1)*.(y3-.y1) -. (x3-.x1)*.(y2-.y1))

let rec area p0 = function
  | p1::p2::[] -> triarea p0 p1 p2
  | p1::p2::t -> (triarea p0 p1 p2)+.(area p0 (p2::t))


let round x =
  let f,i = modf x in
  if f>=0.5 then i+.1. else i
     
let _ =
  let n = Scanf.scanf " %d" (fun x -> x) in
  let l = ref [] in
  for j=0 to n-1 do
    let x = Scanf.scanf " %f %f" (fun x y -> (x,y))  in
    l := x::(!l)
  done;
  let a = area (List.hd (!l)) (List.tl (!l)) in
  Printf.printf "%f\n" (abs_float a)
