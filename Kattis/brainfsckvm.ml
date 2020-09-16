(*
  OCaml not-so-functional BrainFuck interpreter with:
   - an array for the torus memory of a given size
   - arrays for the program/input as they are static anyway
*)
type token = NOP | LEFT | RIGHT | PLUS | MINUS | DOT | COMMA | LBRACK of int | RBRACK of int
type program = token array
type loop_stack = (int*int) list  (* index of [  &  time we entered the loop *)
type out_state = Term | Loop of int

let interpret : program -> string -> int -> out_state = fun prog input msize ->
  let timeout = 50000000 in
  let psize = Array.length prog in
  let isize = String.length input in
  let mem = Array.make msize 0 in
  let rec run : int -> loop_stack -> int -> int -> int -> out_state = fun time lstack pidx iidx midx ->
    if pidx < psize then
      begin
        if time > timeout && time-(snd (List.hd lstack)) > timeout then
          Loop (fst (List.hd lstack))
        else
          let runxt = run (time+1) lstack (pidx+1) iidx in
          match prog.(pidx) with
          | LEFT  -> runxt (if midx = 0 then msize-1 else midx-1)
          | RIGHT -> runxt (if midx = msize-1 then 0 else midx+1)
          | PLUS  ->
             mem.(midx) <- (mem.(midx)+1) land 255;
             runxt midx
          | MINUS ->
             mem.(midx) <- (mem.(midx)-1) land 255;
             runxt midx
          | DOT   ->
             (*Printf.printf "%c" (Char.chr mem.(midx));*)
             runxt midx
          | COMMA ->
             mem.(midx) <- (if iidx < isize then Char.code input.[iidx] else 255);
             run (time+1) lstack (pidx+1) (iidx+1) midx
          | LBRACK iloop ->
             (* /!\ time+2 because we jump at iloop+1, right after the ] *)
             if mem.(midx) = 0 then run (time+2) lstack (iloop+1) iidx midx
             else run (time+1) ((pidx,time)::lstack) (pidx+1) iidx midx
          | RBRACK iloop ->
             (* /!\ time+2 cf above *)
             if mem.(midx) != 0 then run (time+2) lstack (iloop+1) iidx midx
             else run (time+1) (List.tl lstack) (pidx+1) iidx midx
          | _     -> runxt midx
      end
    else Term
  in run 0 [] 0 0 0

let parse_program : string -> program = fun sprog ->
  let size = String.length sprog in
  let prog = Array.make size NOP in
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

let rec testcase t =
  if t>0 then
    let sm, _, _ = Scanf.sscanf (read_line ()) " %d %d %d" (fun x y z -> (x,y,z)) in
    let prog = parse_program (read_line ()) in
    let input = read_line () in
    begin
      match interpret prog input sm with
      | Term -> Printf.printf "Terminates\n"
      | Loop l ->
         let r = (match prog.(l) with LBRACK r -> r | _ -> failwith "r") in
         Printf.printf "Loops %d %d\n" l r
    end;
    testcase (t-1)

let _ =
  let t = int_of_string (read_line ()) in
  testcase t
