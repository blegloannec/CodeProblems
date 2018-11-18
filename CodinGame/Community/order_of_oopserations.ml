(* 2 stacks expression parser *)
type expr = Int of int | Sum of expr*expr | Sub of expr*expr | Mul of expr*expr | Div of expr*expr

let is_digit c = (Char.code '0' <= Char.code c) && (Char.code c <= Char.code '9')

(* !! non-standard priorities here !! *)
let prio = function
  | '$' -> 0
  | '*' -> 1
  | '-' -> 2
  | '/' -> 3
  | '+' -> 4
  | _ -> failwith "prio"

let cons op e1 e2 =
  match op with
  | '+' -> Sum (e1,e2)
  | '-' -> Sub (e1,e2)
  | '*' -> Mul (e1,e2)
  | '/' -> Div (e1,e2)
  | _ -> failwith "cons"

let parse_expr e =
  let e = e^"$" in
  let vals = Stack.create () and ops = Stack.create () in
  let i = ref 0 in
  while !i < (String.length e) do
    if (is_digit e.[!i]) || (e.[!i]='-' && (!i=0 || not (is_digit e.[!i-1]))) then
      begin
        let neg = (e.[!i]='-') in
        if neg then incr i;
        let v = ref 0 in
        while !i<(String.length e) && (is_digit e.[!i]) do
          v := 10*(!v) + (Char.code e.[!i])-(Char.code '0');
          incr i
        done;
        if neg then v := -(!v);
        Stack.push (Int !v) vals
      end
    else
      begin
        while (not (Stack.is_empty ops)) && (prio (Stack.top ops) >= prio e.[!i]) do
	  let r = Stack.pop vals in
	  let l = Stack.pop vals in
	  Stack.push (cons (Stack.pop ops) l r) vals
        done;
        Stack.push e.[!i] ops;
        incr i
      end
  done;
  Stack.pop vals

let rec eval_expr = function
  | Int i -> i
  | Sum (e1,e2) -> (eval_expr e1)+(eval_expr e2)
  | Sub (e1,e2) -> (eval_expr e1)-(eval_expr e2)
  | Mul (e1,e2) -> (eval_expr e1)*(eval_expr e2)
  | Div (e1,e2) -> (eval_expr e1)/(eval_expr e2)

let main () =
  let e = read_line () in
  let e = parse_expr e in
  print_int (eval_expr e)

let _ = main ()
