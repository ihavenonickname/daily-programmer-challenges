% https://www.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/

-module(main).
-export([main/0]).

moves({X, Y}) ->
    [
        {X - 2, Y + 1},
        {X - 1, Y + 2},
        {X + 1, Y + 2},
        {X + 2, Y + 1},
        {X + 2, Y - 1},
        {X + 1, Y - 2},
        {X - 1, Y - 2},
        {X - 2, Y - 1}
    ].

count_moves(_, _, []) -> no;
count_moves(Target, _, [{Pos, Depth}|_]) when Pos == Target -> Depth;
count_moves(Target, Visited, [{Pos, Depth}|Rest]) ->
    Unseen = [{X, Depth + 1} || X <- moves(Pos), not sets:is_element(X, Visited)],
    count_moves(Target, sets:add_element(Pos, Visited), Rest ++ Unseen).

count_moves(Target) -> count_moves(Target, sets:new(), [{{0, 0}, 0}]).

main() ->
    io:format("~w~n", [count_moves({3, 7})]),
    io:format("Hello, world!~n").
