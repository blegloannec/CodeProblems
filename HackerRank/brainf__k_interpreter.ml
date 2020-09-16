(*
  OCaml BrainFuck interpreter with:
   - proper functional implementation of the tape
   - arrays for the program/input as they are static anyway
*)
type token = NOP | LEFT | RIGHT | PLUS | MINUS | DOT | COMMA | LBRACK of int | RBRACK of int
type program = token array
type tape = Blank | Cell of tape * int * tape

(* when moving left/right, we have to recreate the left/right neighbor
   so that its right/left pointer actually points towards the current
   version of the current cell *)
let move_left : tape -> tape = fun cell ->
  match cell with
  | Cell (Cell (l, v, _), _, _) -> Cell (l, v, cell)
  | Cell (Blank, _, _) -> Cell (Blank, 0, cell)
  | _ -> failwith "move_left"

let move_right : tape -> tape = fun cell ->
  match cell with
  | Cell (_, _, Cell (_, v, r)) -> Cell (cell, v, r)
  | Cell (_, _, Blank) -> Cell (cell, 0, Blank)
  | _ -> failwith "move_right"

let add_cell : int -> tape -> tape = fun d cell ->
  match cell with
  | Cell (l, v, r) -> Cell (l, (v+d) land 255, r)
  | _ -> failwith "add_cell"

let incr_cell = add_cell 1
let decr_cell = add_cell (-1)

let get_val : tape -> int = fun cell ->
  match cell with
  | Cell (_, v, _) -> v
  | _ -> failwith "get_char"

let set_val : tape -> char -> tape = fun cell v ->
  match cell with
  | Cell (l, _, r) -> Cell (l, Char.code v, r)
  | _ -> failwith "set_val"

let interpret : program -> string -> bool = fun prog input ->
  let timeout = 100000 in
  let psize = Array.length prog in
  let rec run : int -> int -> int -> tape -> bool = fun time pidx iidx cell ->
    if pidx < psize && time < timeout then
      let runxt = run (time+1) (pidx+1) iidx in
      match prog.(pidx) with
      | LEFT  -> runxt (move_left cell)
      | RIGHT -> runxt (move_right cell)
      | PLUS  -> runxt (incr_cell cell)
      | MINUS -> runxt (decr_cell cell)
      | DOT   ->
         Printf.printf "%c" (Char.chr (get_val cell));
         runxt cell
      | COMMA -> run (time+1) (pidx+1) (iidx+1) (set_val cell input.[iidx])
      | LBRACK iloop when get_val cell  = 0 -> run (time+1) iloop iidx cell
      | RBRACK iloop when get_val cell != 0 -> run (time+1) iloop iidx cell
      | _     -> runxt cell
    else pidx >= psize
  in run 0 0 0 (Cell (Blank, 0, Blank))

let parse_program : string -> program = fun sprog ->
  let size = String.length sprog in
  let prog = Array.make size LEFT in
  let rec aux i lstack =
    if i<size then
      if sprog.[i] = '[' then
        aux (i+1) (i::lstack)
      else if sprog.[i] = ']' then
        begin
          let l = List.hd lstack in
          prog.(l) <- LBRACK i;
          prog.(i) <- RBRACK l;
          aux (i+1) (List.tl lstack)
        end
      else
        begin
          prog.(i) <-
            (match sprog.[i] with
             | '<' -> LEFT  | '>' -> RIGHT | '+' -> PLUS
             | '-' -> MINUS | '.' -> DOT   | ',' -> COMMA
             |  _  -> NOP);
          aux (i+1) lstack
        end
  in
  aux 0 [];
  prog

let _ =
  let n,m = Scanf.sscanf (read_line ()) " %d %d" (fun x y -> (x,y)) in
  let input = read_line () in
  let re = Str.regexp "[^][<>+.,-]" in
  let prog = parse_program (String.concat "" (List.init m (fun _ -> Str.global_replace re "" (read_line ())))) in
  let term = interpret prog input in
  print_newline ();
  if not term then print_endline "PROCESS TIME OUT. KILLED!!!"
