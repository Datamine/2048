open Core.Std

let testlist = [2;2;0;4]

let f acc next =
  let (res, last) = acc in
  match last, next with
  | 0, 0 -> (res, 0)
  | 0, v -> (res, v)
  | p, 0 -> (res, p)
  | p, c ->
     if p = c
     then ((p+c) :: res, 0)
     else (p :: res, c)

(* Produce a list of n copies of item *)
let several item n =
  let rec itr acc n =
    if n = 0 then acc
    else itr (item :: acc) (n - 1)
  in
  itr [] n

let () =
  let result, last = List.fold testlist ~init:([], 0) ~f in

  (* The fold leaves one value hanging in the last postion, so append
     it, then reverse the whole result list *)
  let result = List.rev (last :: result) in

  (* Now pad the list with zeroes to length 4 *)
  let c = List.length result in
  let result = result @ (several 0 (4 - c)) in
  printf "Initial: '%s'\nResult:  '%s'\n"
         (List.to_string ~f:Int.to_string testlist)
         (List.to_string ~f:Int.to_string result)
