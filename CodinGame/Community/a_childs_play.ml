let w,h = Scanf.sscanf (read_line ()) "%d %d" (fun w h -> (w,h))
let n = int_of_string (read_line ())
let g = Array.init h (fun _ -> read_line ())
let dx0,dy0 = -1,0

let rec start i =
    try i, String.index g.(i) 'O'
    with Not_found -> start (i+1)

let robot =
    let memo = Hashtbl.create 800 and trace = Array.make 800 (0,0) in
    let rec move x y dx dy i n =
        if n=0 then x,y
        else
            try
                let t = Hashtbl.find memo (x,y,dx,dy) in
                trace.(t + (n-i) mod (i-t))
            with Not_found ->
                Hashtbl.add memo (x,y,dx,dy) i;
                trace.(i) <- (x,y);
                let dx,dy = if g.(x+dx).[y+dy]='#' then dy,-dx else dx,dy in
                move (x+dx) (y+dy) dx dy (i+1) n
    in move

let _ =
    let x0,y0 = start 0 in
    let x,y = robot x0 y0 dx0 dy0 0 n in
    Printf.printf "%d %d\n" y x
