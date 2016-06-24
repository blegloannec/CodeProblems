type couleur = Ca | Co | P | T
type rang = int
type carte = couleur * rang

let couleur_str = function
  | Ca -> "Carreau"
  | Co -> "Coeur"
  | P -> "Pique"
  | T -> "Trefle"

let couleur_int = function
  | Ca -> 0
  | Co -> 1
  | P -> 2
  | T -> 3

let rang_str = function
  | 11 -> "Valet"
  | 12 -> "Dame"
  | 13 -> "Roi"
  | 14 -> "As"
  | r -> string_of_int r

let char2col = function
  | 'H' -> Co | 'C' -> T | 'S' -> P | _ -> Ca

let char2rank = function
  | 'A' -> 14 | 'K' -> 13 | 'Q' -> 12 | 'J' -> 11 | 'T' -> 10
  | x -> (Char.code x) - (Char.code '0')
     
let carte_str (c,r) = (rang_str r)^" de "^(couleur_str c)

let carte_parse s = (char2col s.[1], char2rank s.[0])
  
let carte_compare (c1,r1) (c2,r2) = if r1=r2 then (couleur_int c1)-(couleur_int c2) else r1-r2
(* NB : compare c1 c2, marche aussi et prend l'ordre des constructeurs *)

let carte_tri = List.sort carte_compare


(* === Combinaisons === *)
let compte c = 
  let tcoul = Array.make 4 [] in
  let trang = Array.make 13 0 in
  let ajoute (c,r) =
    tcoul.(couleur_int c) <- (c,r)::tcoul.(couleur_int c);
    trang.(r-2) <- trang.(r-2) + 1
  in
  List.iter ajoute c;
  (tcoul,(Array.to_list trang))

let fold_lefti f acc0 l = 
  let rec aux i acc = function
    | [] -> acc
    | h::t -> aux (i+1) (f acc i h) t
  in
  aux 0 acc0 l

let multiple n acc i nb = match acc with
  | None -> if nb=n then Some (i+2) else None
  | s -> s

let carre = fold_lefti (multiple 4) None

let brelan = fold_lefti (multiple 3) None

let paire = fold_lefti (multiple 2) None

let double_paire trang =
  let multiples acc i nb = if nb=2 then (i+2)::acc else acc
  in
  match fold_lefti multiples [] trang with 
  | r1::r2::_ -> Some (r1,r2)
  | _ -> None

let couleur tcoul =
  let aux acc l = match acc with
    | None -> if (List.length l)>=5 then Some (snd (List.hd l)) else None
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
      if cpt>3 then (cpt+1,Some (i+2))
      else (cpt+1,rmax)
    end
    else (0,rmax)
  in
  snd (fold_lefti aux (0,None) trang)

(* cas particulier de l'as utilise en low card *)
let lowsuite = function
  | [(_,2);(_,3);(_,4);(_,5);(_,14)] -> Some ()
  | _ -> None
    
let quinte_flush tcoul =
  let aux acc l = match acc with
    | None -> if (List.length l)>=5 then Some l else None
    | s -> s
  in
  match Array.fold_left aux None tcoul with
  | None -> None
  | Some l ->
    let l2 = carte_tri l in
    let _,trang2 = compte l2 in
    suite trang2

let rec dernier = function
  | [h] -> h
  | _::t -> dernier t
  | _ -> failwith "erreur"

let combinaison hand =
  let l = carte_tri hand in
  let tcoul,trang = compte l in
  match quinte_flush tcoul with 
  | Some r -> (8,r,0)
  | None ->
    match carre trang with 
    | Some r -> (7,r,0)
    | None ->
      match full trang with 
      | Some (r1,r2) -> (6,r1,r2)
      | None ->
	match couleur tcoul with 
	| Some r -> (5,r,0)
	| None ->
	  match suite trang with 
	  | Some r -> (4,r,0)
	  | None ->
	     match lowsuite l with
	     | Some _ -> (4,-1,0)
	     | None ->
		match brelan trang with 
		| Some r -> (3,r,0)
		| None ->
		   match double_paire trang with 
		   | Some (r1,r2) -> (2,r1,r2)
		   | None ->
		      match paire trang with 
		      | Some r -> (1,r,0)
		      | None -> (0,0,0)

let aff_comb (x,y,z) = Printf.printf "(%d,%d,%d)\n" x y z


(* === MAIN === *)
let main () =
  let t = Scanf.scanf " %d" (fun x -> x) in
  for c = 1 to t do
    let h1,h2 = Scanf.scanf " %s %s %s %s %s %s %s %s %s %s" (fun a b c d e f g h i j -> (List.map carte_parse [a;b;c;d;e], List.map carte_parse [f;g;h;i;j])) in
    let c1 = combinaison h1 and c2 = combinaison h2 in
    if c1>c2 then Printf.printf "Player 1\n"
    else if c1<c2 then Printf.printf "Player 2\n"
    else begin
      let l1 = List.sort (fun x y -> y-x) (List.map snd h1) and l2 = List.sort (fun x y -> y-x) (List.map snd h2) in
      if l1>l2 then Printf.printf "Player 1\n"
      else Printf.printf "Player 2\n"
    end
  done

let _ = 
  main ()
