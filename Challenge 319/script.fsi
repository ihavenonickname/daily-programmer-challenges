// https://www.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/

open System

let concat (xs: seq<char>) = String.Concat(xs)

let split (str: string) = str.Split(' ')

let tryApply f fallback x =
    match x with
    | Some y -> f y
    | None -> fallback

let substringsLeft s =
    [ for n in 1 .. (Seq.length s) -> concat <| Seq.take n s ]

let substringsRight s =
    [ for n in (Seq.length s - 1) .. -1 .. 0 -> concat <| Seq.skip n s ]

let bestOverlap word1 word2 =
    Seq.zip (substringsRight word1) (substringsLeft word2)
    |> Seq.skipWhile (fun (a, b) -> a <> b)
    |> Seq.tryHead
    |> tryApply fst ""

let condenseWords word1 word2 =
    match bestOverlap word1 word2 with
    | "" -> word1 + " " + word2
    | overlap ->
        let n = Seq.length overlap
        word1 + concat (Seq.skip n word2)

let condenseText text =
    text
    |> split
    |> Seq.reduce condenseWords
