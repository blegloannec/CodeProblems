(*
  > en temps normal pour minimiser l'enveloppe
  >= ici pour mettre tous les points de l'enveloppe sur l'enveloppe
  meme ceux qui ne sont pas des sommets mais sont sur une arete
*)
let trigo_turn (x1,y1) (x2,y2) (x3,y3) =
  (x1-x3)*(y2-y3)-(y1-y3)*(x2-x3) >= 0

let hd l = List.hd !l
let hd2 l = List.hd (List.tl !l)
let lg l = List.length !l
  
let andrew l =
  let top = ref [] and bot = ref [] in
  let aux p =
    while (lg top)>=2 && not (trigo_turn p (hd top) (hd2 top)) do
      top := List.tl !top
    done;
    top := p::(!top);
    while (lg bot)>=2 && not (trigo_turn (hd2 bot) (hd bot) p) do
      bot := List.tl !bot
    done;
    bot := p::(!bot);
  in
  List.iter aux l;
  bot := List.tl (List.tl !bot); (* on vire les pts en doublon avec top *)
  List.rev_append !bot !top

(*let print_list l =
  List.iter (fun (x,y) -> Printf.printf "%f %f\n" x y) l*)
    
let _ =
  let n = Scanf.scanf " %d" (fun x -> x) in
  let l = ref [] in
  for j=0 to n-1 do
    let x = Scanf.scanf " %d %d" (fun x y -> (x,y))  in
    l := x::(!l)
  done;
  let a = andrew (List.sort compare !l) in
  (*print_list a;*)
  (* si l'enveloppe (maximisee en y mettant tous les points possibles)
     a autant de points que le polygone, c'est convexe *)
  Printf.printf "%s\n" (if (List.length a)=n then "NO" else "YES")
