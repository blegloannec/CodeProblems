let rec find repr x =
  if repr.(x) <> x then repr.(x) <- find repr repr.(x);
  repr.(x);;

let union repr x y =
  let x = find repr x and y = find repr y in
  repr.(y) <- x;
  x <> y;;

let ord c = (Char.code c) - (Char.code 'A');;

let _ =
  let h,w,k = Scanf.sscanf (read_line ()) " %d %d %d" (fun x y z -> (x,y,z)) in
  let grid = Array.init h (fun _ -> read_line ()) in
  let comp = ref 0 in
  let seen = Array.make 26 false in
  let repr = Array.init 26 (fun i -> i) in
  for j = 0 to w-1 do
    let c0 = ord grid.(0).[j] in
    for i = 0 to h-1 do
      let c = ord grid.(i).[j] in
      if not seen.(c) then (
        incr comp;
        seen.(c) <- true
      );
      if union repr c0 c then decr comp
    done
  done;
  Printf.printf "%d\n" !comp;;
