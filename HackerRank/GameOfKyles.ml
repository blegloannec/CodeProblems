
let g = Array.make 301 (-1)
  
let mex h =
  let m = ref 0 in
  while Hashtbl.mem h !m do
    incr m
  done;
  !m
  
let rec grundy n =
  if g.(n)>=0 then g.(n)
  else begin
    let h = Hashtbl.create (n*n/2) in
    for i=0 to (n-1)/2 do
      if n-1-i>=0 then
	Hashtbl.add h ((grundy i) lxor (grundy (n-1-i))) ()
    done;
    for i=0 to (n-2)/2 do
      if n-2-i>=0 then
	Hashtbl.add h ((grundy i) lxor (grundy (n-2-i))) ()
    done;
    g.(n) <- mex h;
    g.(n)
  end

let main () =
  let re = Str.regexp "X+" in
  let t = int_of_string (read_line ()) in
  for i = 1 to t do
    let _ = int_of_string (read_line ()) in
    let s = Str.split re (read_line ()) in
    print_endline (if (List.fold_left (fun a x -> a lxor (grundy (String.length x))) 0 s)>0 then "WIN" else "LOSE")
  done
      
let _ = main ()
