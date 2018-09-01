let sqr x = x*.x

let dist (x1,y1) (x2,y2) =
  sqrt ((sqr (x1-.x2)) +. (sqr (y1-.y2)))

let rec perim p0 = function
  | p1::p2::t -> (dist p1 p2)+.(perim p0 (p2::t))
  | p1::[] -> dist p1 p0

let _ =
  let n = Scanf.scanf " %d" (fun x -> x) in
  let l = ref [] in
  for j=0 to n-1 do
    let x = Scanf.scanf " %f %f" (fun x y -> (x,y))  in
    l := x::(!l)
  done;
  Printf.printf "%f\n" (perim (List.hd (!l)) (!l))

