(* 2 stacks expression parser *)
type expr = Id of char | Int of int | Sum of expr*expr | Sub of expr*expr | Mul of expr*expr | Div of expr*expr | Pow of expr*expr

let is_digit c = (Char.code '0' <= Char.code c) && (Char.code c <= Char.code '9')

let prio = function
  | ';' -> 0
  | '(' -> 1
  | ')' -> 2
  | '+' | '-' -> 3
  | '*' | '/' -> 4
  | '^' -> 5
  | _ -> -1

let cons op e1 e2 =
  match op with
  | '+' -> Sum (e1,e2)
  | '-' -> Sub (e1,e2)
  | '*' -> Mul (e1,e2)
  | '/' -> Div (e1,e2)
  | '^' -> Pow (e1,e2)
  | _ -> failwith "cons"

let parse_expr e =
  let e = e^";" in
  let vals = Stack.create () and ops = Stack.create () in
  let digit_last = ref false in
  for i=0 to (String.length e)-1 do
    if prio e.[i] >= 0 then begin
      while (e.[i] <> '(') && (not (Stack.is_empty ops)) && (prio (Stack.top ops) >= prio e.[i]) do
	let r = Stack.pop vals in
	let l = Stack.pop vals in
	Stack.push (cons (Stack.pop ops) l r) vals
      done;
      if e.[i]==')' then ignore (Stack.pop ops)
      else Stack.push e.[i] ops;
      digit_last := false
    end
    else if (is_digit e.[i]) then begin
      (*
	parsing integers char per char
	try to avoid that when the input allows a way to produce
	a list of actual tokens, like ["(", "-34", "+", "128", ")"]
	but here we have to deal with a list of chars so...
      *)
      if !digit_last then
	match Stack.pop vals with
	| Int v -> Stack.push (Int (10*v+((Char.code e.[i])-(Char.code '0')))) vals
	| _ -> failwith "digit_last"
      else Stack.push (Int ((Char.code e.[i])-(Char.code '0'))) vals;
      digit_last := true
    end
    else if e.[i]<>' ' then begin
      Stack.push (Id e.[i]) vals;
      digit_last := false
    end
  done;
  Stack.pop vals


(* evaluation, useless here *)
let rec fast_expo a b =
  if b=0 then 1
  else if (b mod 2)=0 then fast_expo (a*a) (b/2)
  else a*(fast_expo (a*a) ((b-1)/2))
    
let rec eval_expr = function
  | Int i -> i
  | Sum (e1,e2) -> (eval_expr e1)+(eval_expr e2)
  | Sub (e1,e2) -> (eval_expr e1)-(eval_expr e2)
  | Mul (e1,e2) -> (eval_expr e1)*(eval_expr e2)
  | Div (e1,e2) -> (eval_expr e1)/(eval_expr e2)
  | Pow (e1,e2) -> fast_expo (eval_expr e1) (eval_expr e2)
  | _ -> failwith "eval"

let rec print_expr = function
  | Int i -> Printf.sprintf "%d" i
  | Id c -> Printf.sprintf "%c" c
  | Sum (e1,e2) -> Printf.sprintf "(%s) + (%s)" (print_expr e1) (print_expr e2)
  | Sub (e1,e2) -> Printf.sprintf "(%s) - (%s)" (print_expr e1) (print_expr e2)
  | Mul (e1,e2) -> Printf.sprintf "(%s)*(%s)" (print_expr e1) (print_expr e2)
  | Div (e1,e2) -> Printf.sprintf "(%s)/(%s)" (print_expr e1) (print_expr e2)
  | Pow (e1,e2) -> Printf.sprintf "(%s)^(%s)" (print_expr e1) (print_expr e2)


(*
  simplification
  recursively build the polynomial from the expr tree
*)
let deg = 6
let rec poly = function
  | Sum (a,b) ->
     let pa = poly a and pb = poly b in
     let p = Array.make deg 0 in
     for i=0 to deg-1 do
       p.(i) <- pa.(i)+pb.(i)
     done;
     p
  | Sub (a,b) ->
     let pa = poly a and pb = poly b in
     let p = Array.make deg 0 in
     for i=0 to deg-1 do
       p.(i) <- pa.(i)-pb.(i)
     done;
     p
  | Mul (a,b) ->
     let pa = poly a and pb = poly b in
     let p = Array.make deg 0 in
     for i=0 to deg-1 do
       for j=0 to i do
	 p.(i) <- p.(i) + pa.(j)*pb.(i-j)
       done
     done;
     p
  | Div (a,b) ->
     let pa = poly a and pb = poly b in
     let p = Array.make deg 0 in
     for i=0 to deg-1 do
       p.(i) <- pa.(i)/pb.(0)
     done;
     p
  | Pow (a,b) ->
     let pa = poly a and pb = poly b in
     let p = Array.make deg 0 in
     if pa.(0)<>0 then p.(0) <- fast_expo pa.(0) pb.(0)
     else if pa.(1)<>0 then p.(pb.(0)) <- fast_expo pa.(1) pb.(0);
     p
  | Int i ->
     let p = Array.make deg 0 in
     p.(0) <- i;
     p
  | Id _ ->
     let p = Array.make deg 0 in
     p.(1) <- 1;
     p

let print_poly p =
  let first = ref true in
  for i=5 downto 0 do
    if (not !first) then begin
      if p.(i)<0 then Printf.printf " - "
      else if p.(i)>0 then Printf.printf " + ";
      p.(i) <- abs p.(i)
    end;
    if p.(i)<>0 then begin
      let sv = if p.(i)=1 && i>0 then "" else if p.(i) = -1 && i>0 then "-" else string_of_int p.(i) in
      if i>1 then Printf.printf "%sx^%d" sv i
      else if i=1 then Printf.printf "%sx" sv
      else Printf.printf "%s" sv;
      first := false
    end
  done;
  print_newline ()

    
let main () =
  (* replacements for the parser to work *)
  let re = Str.regexp "\\([0-9]\\)x" in
  let re2 = Str.regexp ")(" in
  let re3 = Str.regexp "x(" in
  let re4 = Str.regexp ")x" in
  let re5 = Str.regexp "\\(^\\|(\\) *- *\\([0-9]+\\)" in
  let re6 = Str.regexp "\\(^\\|(\\) *- *(" in (* 1 implicite *)
  let t = int_of_string (read_line ()) in
  for i=1 to t do
    let e = read_line () in
    (*print_endline e;*)
    let e = Str.global_replace re5 "\\1(0-\\2)" e in
    let e = Str.global_replace re6 "\\1(0-1)(" e in
    let e = Str.global_replace re "\\1*x" e in
    let e = Str.global_replace re2 ")*(" e in
    let e = Str.global_replace re3 "x*(" e in
    let e = Str.global_replace re4 ")*x" e in
    (*print_endline e;*)
    let e = parse_expr e in
    (*print_endline (print_expr e);*)
    print_poly (poly e)
  done

let _ = main ()
