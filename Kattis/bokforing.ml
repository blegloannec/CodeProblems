(* Purely functional code using Map *)
module IntMap = Map.Make(struct type t = int let compare = compare end)

let rec query q h d =
  if q > 0 then
    let c,i = Scanf.scanf " %s %d" (fun x y -> (x,y)) in
    if c = "SET" then
      let x = Scanf.scanf " %d" (fun x -> x) in
      query (q-1) (IntMap.add i x h) d
    else if c = "RESTART" then
      query (q-1) IntMap.empty i
    else
      begin
        Printf.printf "%d\n" (try IntMap.find i h with Not_found -> d);
        query (q-1) h d
      end

let _ =
  let n,q = Scanf.scanf " %d %d" (fun x y -> (x,y)) in
  query q IntMap.empty 0
