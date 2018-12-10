(* === Cartes === *)
let char_couleur = function
  | 'D' -> 0 | 'H' -> 1 | 'S' -> 2 | 'C' -> 3
  | c -> failwith (Printf.sprintf "str_couleur %c" c)

let char_rang = function
  | 'T' -> 10 | 'J' -> 11 | 'Q' -> 12 | 'K' -> 13 | 'A' -> 14
  | c -> (Char.code c) - (Char.code '0')

let rang_str = function
  | 10 -> "T" | 11 -> "J" | 12 -> "Q" | 13 -> "K" | 14 | 1 -> "A"
  | r -> string_of_int r

let carte_compare (_,r1) (_,r2) = r1-r2

let carte_tri = List.sort carte_compare

let str_carte s = (char_couleur s.[1], char_rang s.[0])


(* === Combinaisons === *)
let compte c =
  let tcoul = Array.make 4 [] in
  let trang = Array.make 14 0 in
  let tcoul1 = Array.make 4 [] in
  let trang1 = Array.make 14 0 in
  let ajoute (c,r) =
    tcoul.(c) <- (c,r)::tcoul.(c);
    tcoul1.(c) <- (c,r)::tcoul1.(c);
    trang.(r-1) <- trang.(r-1) + 1;
    trang1.(r-1) <- trang1.(r-1) + 1;
    if r==14 then begin
        tcoul1.(c) <- (c,1)::tcoul1.(c);
        trang1.(0) <- trang1.(0) + 1;
      end
  in
  List.iter ajoute c;
  (tcoul,tcoul1,(Array.to_list trang),(Array.to_list trang1))

let fold_lefti f acc0 l = 
  let rec aux i acc = function
    | [] -> acc
    | h::t -> aux (i+1) (f acc i h) t
  in
  aux 0 acc0 l

let multiple n acc i nb = match acc with
  | None -> if nb=n then Some (i+1) else None
  | s -> s

let carre = fold_lefti (multiple 4) None

let brelan = fold_lefti (multiple 3) None

let paire = fold_lefti (multiple 2) None

let double_paire trang =
  let multiples acc i nb = if nb=2 then (i+1)::acc else acc
  in
  match fold_lefti multiples [] trang with 
  | r1::r2::_ -> Some (r1,r2)
  | _ -> None

let couleur tcoul =
  let aux acc l = match acc with
    | None -> if (List.length l)>=5 then Some l else None
    | s -> s
  in
  Array.fold_left aux None tcoul

let full trang =
  match brelan trang, paire trang with
  | Some r1, Some r2 -> Some (r1,r2)
  | _ -> None

let suite trang =
  let aux (cpt,rmax) i nb =
    if nb>0 then begin
      if cpt>3 then (cpt+1,Some (i+1))
      else (cpt+1,rmax)
    end
    else (0,rmax)
  in
  snd (fold_lefti aux (0,None) trang)

let quinte_flush tcoul =
  let aux acc l = match acc with
    | None -> if (List.length l)>=5 then Some l else None
    | s -> s
  in
  match Array.fold_left aux None tcoul with
  | None -> None
  | Some l ->
    let l2 = carte_tri l in
    let _,_,_,trang2 = compte l2 in
    suite trang2

let kickers forb n l =
  let l = List.rev_map snd l in
  let rec aux n l =
    if n=0 then []
    else
      match l with
      | [] -> []
      | h::t -> if List.mem h forb then aux n t
                else h::(aux (n-1) t)
  in aux n l

let combinaison board hand =
  let l = carte_tri (board@hand) in
  let tcoul,tcoul1,trang,trang1 = compte l in
  match quinte_flush tcoul1 with
  | Some r -> (8,[r;r-1;r-2;r-3;r-4])
  | None ->
    match carre trang with 
    | Some r -> (7,[r;r;r;r]@(kickers [r] 1 l))
    | None ->
      match full trang with 
      | Some (r1,r2) -> (6,[r1;r1;r1;r2;r2])
      | None ->
	match couleur tcoul with 
	| Some l -> (5,(kickers [] 5 (List.rev l)))
	| None ->
	  match suite trang1 with 
	  | Some r -> (4,[r;r-1;r-2;r-3;r-4])
	  | None ->
	    match brelan trang with 
	    | Some r -> (3,[r;r;r]@(kickers [r] 2 l))
	    | None ->
	      match double_paire trang with 
	      | Some (r1,r2) -> (2,[r1;r1;r2;r2]@(kickers [r1;r2] 1 l))
	      | None ->
		match paire trang with 
		| Some r -> (1,[r;r]@(kickers [r] 3 l))
		| None -> (0,(kickers [] 5 l))

let comb_str = [|"HIGH_CARD";"PAIR";"TWO_PAIR";"THREE_OF_A_KIND";"STRAIGHT";"FLUSH";"FULL_HOUSE";"FOUR_OF_A_KIND";"STRAIGHT_FLUSH"|]

let aff_comb i (x,k) = Printf.printf "%d %s %s\n" i comb_str.(x) (String.concat "" (List.map rang_str k))

let ligne_cartes () = List.map str_carte (String.split_on_char ' ' (read_line ()))


(* === MAIN === *)
let main () =
  let h1 = ligne_cartes () in
  let h2 = ligne_cartes() in
  let b = ligne_cartes () in
  let c1 = combinaison b h1 in
  let c2 = combinaison b h2 in
  if c1=c2 then print_endline "DRAW"
  else if c1>c2 then aff_comb 1 c1
  else aff_comb 2 c2

let _ = main ()
