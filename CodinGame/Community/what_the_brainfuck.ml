(*
  OCaml not-so-functional BrainFuck interpreter with:
   - an array for the torus memory of a given size
   - arrays for the program/input as they are static anyway
*)
type token = NOP | LEFT | RIGHT | PLUS | MINUS | DOT | COMMA | LBRACK of int | RBRACK of int
type program_t = token array
type input_t = int list

let interpret : program_t -> input_t -> int -> unit = fun prog input msize ->
  let psize = Array.length prog in
  let mem = Array.make msize 0 in
  let rec run : int -> input_t -> int -> unit = fun pidx input midx ->
    if pidx < psize then
      let runxt = run (pidx+1) input in
      match prog.(pidx) with
      | LEFT  ->
         if midx > 0 then runxt (midx-1)
         else failwith "POINTER OUT OF BOUNDS"
      | RIGHT ->
         if midx+1 < msize then runxt (midx+1)
         else failwith "POINTER OUT OF BOUNDS"
      | PLUS  ->
         if mem.(midx) < 255 then mem.(midx) <- mem.(midx)+1
         else failwith "INCORRECT VALUE";
         runxt midx
      | MINUS ->
         if mem.(midx) > 0 then mem.(midx) <- mem.(midx)-1
         else failwith "INCORRECT VALUE";
         runxt midx
      | DOT   ->
         Printf.printf "%c" (Char.chr mem.(midx));
         runxt midx
      | COMMA ->
         mem.(midx) <- List.hd input;
         run (pidx+1) (List.tl input) midx
      | LBRACK iloop when mem.(midx)  = 0 -> run iloop input midx
      | RBRACK iloop when mem.(midx) != 0 -> run iloop input midx
      | _ -> runxt midx
  in run 0 input 0

let parse_program : string -> program_t = fun sprog ->
  let size = String.length sprog in
  let prog = Array.make size NOP in
  let rec aux i lstack =
    if i<size then
      if sprog.[i] = '[' then
        aux (i+1) (i::lstack)
      else if sprog.[i] = ']' then
        match lstack with
        | l::lstail ->
           let l = List.hd lstack in
           prog.(l) <- LBRACK (i+1);
           prog.(i) <- RBRACK (l+1);
           aux (i+1) lstail
        | _ -> failwith "SYNTAX ERROR"
      else
        begin
          prog.(i) <-
            (match sprog.[i] with
             | '<' -> LEFT  | '>' -> RIGHT | '+' -> PLUS
             | '-' -> MINUS | '.' -> DOT   | ',' -> COMMA
             |  _  -> NOP);
          aux (i+1) lstack
        end
    else if lstack != [] then failwith "SYNTAX ERROR"
  in
  aux 0 [];
  prog

let _ =
  try
    let l, s, n = Scanf.sscanf (read_line ()) " %d %d %d" (fun x y z -> (x,y,z)) in
    let prog = parse_program (String.concat "" (List.init l (fun _ -> read_line ()))) in
    let input = List.init n (fun _ -> read_int ()) in
    interpret prog input s
  with Failure(err) -> print_endline err
