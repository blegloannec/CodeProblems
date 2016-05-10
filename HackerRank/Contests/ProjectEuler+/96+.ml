(*
  Very old sudoku solver (+ a solution counter) written a long time ago...
  Solver uses 3 "difficulty" levels.
  Can be used to solve as well as to generate a grid with a required
  difficulty level (with a unique solution).
  Medium level solver (no guessing/backtracking) should
  be enough for this problem but actually timeouts on half
  of the testcases! Inefficient implementation or bug??
  Difficult level solver (backtrack) passes everything instantaneously!
*)

let matrice_3d n = 
  let f i = Array.make_matrix n n true in
    Array.init n f;;

let matrix_copy n s d =
  for i=0 to n-1 do
    for j=0 to n-1 do
      d.(i).(j) <- s.(i).(j)
    done
  done;;

exception Erreur;;
exception Stop;;

let nb_sol = ref 0;;

let admissible t n =
  try 
    let p = n*n in
      for i=0 to p-1 do
	let l = Array.make p true 
	and c = Array.make p true
	and b = Array.make p true
	and ix = (i/n)*n and iy = (i mod n)*n
	in
	  for j=0 to p-1 do
	    if t.(i).(j)>0 then begin
	      if l.(t.(i).(j)-1) then l.(t.(i).(j)-1) <- false
	      else raise Erreur;
	    end;
	    if t.(j).(i)>0 then begin
	      if c.(t.(j).(i)-1) then c.(t.(j).(i)-1) <- false
	      else raise Erreur;
	    end; 
	    let x = ix+j/n and y = iy+(j mod n) in
	    if t.(x).(y)>0 then begin
	      if b.(t.(x).(y)-1) then b.(t.(x).(y)-1) <- false
	      else raise Erreur;
	    end;
	  done;
      done;
      true
  with
    | Erreur -> false;;

let solver n t level =
  let p = n*n in
  (* Ensembles des valeurs possibles *)
  let e = matrice_3d p in
  (* Nb de possibilités pour chaque case vide *)
  let nb = Array.make_matrix p p 0 in
  (* Nb de cellules vides - pour niveau moyen *)
  let vides = ref 0 in

  (* Construit l'ensemble e.(x).(y) *)
  let init x y =
    nb.(x).(y) <- p;
    incr vides; (* pour niveau moyen *)
    let a = (x/n)*n and b = (y/n)*n in
    let maj i j = 
      if (t.(i).(j)>0) && (e.(x).(y).(t.(i).(j)-1)) then begin
	e.(x).(y).(t.(i).(j)-1) <- false;
	nb.(x).(y) <- nb.(x).(y) - 1;
      end;
    in
      for i=0 to p-1 do
	maj i y;
	maj x i;
	maj (a+i/n) (b+(i mod n));
      done;
  in

  (* Propage le remplissage de la grille *)
  let rec traite x y =
    if nb.(x).(y) = 0 then init x y;
    if nb.(x).(y) = 1 then begin
      let rec v i =
	if e.(x).(y).(i) then i+1 else v (i+1)
      in t.(x).(y) <- v 0;
      decr vides; (* pour niveau moyen *)
      propage x y
    end;
  and propage x y =
    let a = (x/n)*n and b = (y/n)*n in
    let maj i j = 
      if (t.(i).(j)=0) && (nb.(i).(j)>1) && (e.(i).(j).(t.(x).(y)-1)) then begin
	e.(i).(j).(t.(x).(y)-1) <- false;
	nb.(i).(j) <- nb.(i).(j) - 1;
	if nb.(i).(j)=1 then traite i j;
      end;
    in
      for i=0 to p-1 do
	maj x i;
	maj i y; 
	maj (a+i/n) (b+(i mod n));
      done;
  in
    (* Niveau facile *)
    let easy () =
      for i=0 to p-1 do
	for j=0 to p-1 do
	  if t.(i).(j)=0 then traite i j;
	done;
      done;
    in easy ();
    
    (* Niveau moyen *)
    if level=1 then begin
      let traite_bloc i f1 f2 =
	(* Nb de case pour chaque chiffre *)
	let nbc = Array.make p 0 in
	(* Denière case possible pour chaque chiffre *)
	let dcp = Array.make p (-1,-1) in
	  for j=0 to p-1 do
	    let a = f1 i j and b = f2 i j in
	      if t.(a).(b)=0 then 
		let ajoute x v =
		  if v then begin
		    nbc.(x) <- nbc.(x) + 1;
		    dcp.(x) <- (a,b);
		  end
		in
		  Array.iteri ajoute e.(a).(b);
	  done;
	  let bilan x v =
	    if v=1 then begin
	      let a,b = dcp.(x) in
		if t.(a).(b)=0 then begin
		  t.(a).(b) <- x + 1;
		  vides := !vides - 1;
		  propage a b;
		end;
	    end;
	  in
	    Array.iteri bilan nbc;
      in
	while !vides > 0 do
	  for i=0 to p-1 do
	    (* Ligne *)
	    traite_bloc i (fun i j -> i) (fun i j -> j);
	    (* Colonne *)
	    traite_bloc i (fun i j -> j) (fun i j -> i);	  
	    (* Carre *)
	    traite_bloc i (fun i j -> (i/n)*n+j/n) (fun i j -> (i mod n)*n+(j mod n));
	  done;
	done;
    end;
    
    (* Niveau difficile *)
    if level>1 then begin
      let reinit () =
	Array.iter (fun v -> Array.iter (fun y -> Array.fill y 0 p true) v) e;
	Array.iter (fun v -> Array.fill v 0 p 0) nb;
	vides := 0;
	easy ();
      in
      let get_best_cell () =
	let a = ref 0 and b = ref 0 and m = ref (p+1) in
	  for i=0 to p-1 do
	    for j=0 to p-1 do
	      if t.(i).(j)=0 && nb.(i).(j)<(!m) then begin
		a := i;
		b := j;
		m := nb.(i).(j);
	      end
	    done
	  done;
	  (!a,!b);
      in
      let rec backtrack () =
	if !vides=0 then begin 
	  incr nb_sol;
	  raise Stop;
	end
	else begin
	(* Calcul de la cellule la plus contrainte *)
	let x,y = get_best_cell () in
	let svg = Array.make_matrix p p 0 in
	  matrix_copy p t svg;
	  for k=0 to p-1 do 
	    if e.(x).(y).(k) then begin
	      t.(x).(y) <- k+1;
	      decr vides;
	      propage x y;
	      if admissible t n then backtrack ();
	      matrix_copy p svg t;
	      reinit ();
	    end;
	  done; 
	end
      in try backtrack () with Stop -> ()
    end;;
  
let counter n t =
  let p = n*n in
  (* Ensembles des valeurs possibles *)
  let e = matrice_3d p in
  (* Nb de possibilités pour chaque case vide *)
  let nb = Array.make_matrix p p 0 in
  (* Nb de cellules vides - pour niveau moyen *)
  let vides = ref 0 in

  (* Construit l'ensemble e.(x).(y) *)
  let init x y =
    nb.(x).(y) <- p;
    incr vides; (* pour niveau moyen *)
    let a = (x/n)*n and b = (y/n)*n in
    let maj i j = 
      if (t.(i).(j)>0) && (e.(x).(y).(t.(i).(j)-1)) then begin
	e.(x).(y).(t.(i).(j)-1) <- false;
	nb.(x).(y) <- nb.(x).(y) - 1;
      end;
    in
      for i=0 to p-1 do
	maj i y;
	maj x i;
	maj (a+i/n) (b+(i mod n));
      done;
  in

  (* Propage le remplissage de la grille *)
  let rec traite x y =
    if nb.(x).(y) = 0 then init x y;
    if nb.(x).(y) = 1 then begin
      let rec v i =
	if e.(x).(y).(i) then i+1 else v (i+1)
      in t.(x).(y) <- v 0;
      decr vides; (* pour niveau moyen *)
      propage x y
    end;
  and propage x y =
    let a = (x/n)*n and b = (y/n)*n in
    let maj i j = 
      if (t.(i).(j)=0) && (nb.(i).(j)>1) && (e.(i).(j).(t.(x).(y)-1)) then begin
	e.(i).(j).(t.(x).(y)-1) <- false;
	nb.(i).(j) <- nb.(i).(j) - 1;
	if nb.(i).(j)=1 then traite i j;
      end;
    in
      for i=0 to p-1 do
	maj x i;
	maj i y; 
	maj (a+i/n) (b+(i mod n));
      done;
  in
    (* Niveau facile *)
    let easy () =
      for i=0 to p-1 do
	for j=0 to p-1 do
	  if t.(i).(j)=0 then traite i j;
	done;
      done;
    in easy ();    
    
    (* Niveau difficile *)
      let reinit () =
	Array.iter (fun v -> Array.iter (fun y -> Array.fill y 0 p true) v) e;
	Array.iter (fun v -> Array.fill v 0 p 0) nb;
	vides := 0;
	easy ();
      in
      let get_best_cell () =
	let a = ref 0 and b = ref 0 and m = ref (p+1) in
	  for i=0 to p-1 do
	    for j=0 to p-1 do
	      if t.(i).(j)=0 && nb.(i).(j)<(!m) then begin
		a := i;
		b := j;
		m := nb.(i).(j);
	      end
	    done
	  done;
	  (!a,!b);
      in
      let rec backtrack () =
	if !vides=0 then begin 
	  incr nb_sol;
	  (*raise Stop;*)
	end
	else begin
	(* Calcul de la cellule la plus contrainte *)
	let x,y = get_best_cell () in
	let svg = Array.make_matrix p p 0 in
	  matrix_copy p t svg;
	  for k=0 to p-1 do 
	    if e.(x).(y).(k) then begin
	      t.(x).(y) <- k+1;
	      decr vides;
	      propage x y;
	      if admissible t n then backtrack ();
	      matrix_copy p svg t;
	      reinit ();
	    end;
	  done; 
	end
      in try backtrack ();!nb_sol with Stop -> -1;;

let print_grille n t =
  let p = n*n in
  for i=0 to p-1 do
    for j=0 to p-1 do
      print_int t.(i).(j);
    done;
    print_newline ()
  done

let main () =
  let t = Array.make_matrix 9 9 0 in
  for i=0 to 8 do
    let l = read_line () in
    for j=0 to 8 do
      t.(i).(j) <- (Char.code l.[j]) - (Char.code '0')
    done
  done;
  solver 3 t 2;
  print_grille 3 t
    
let _ = main ()
