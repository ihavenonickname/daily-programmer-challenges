% https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/

-module(main).
-export([main/0]).

challenge([]) -> false;
challenge([0|_]) -> true;
challenge([H|T]) ->
    case lists:member(-H, T) of
        true -> true;
        false -> challenge(T)
    end.

main() ->
    io:format("~w~n", [challenge([-97364, -71561, -69336, 19675, 71561, 97863])]),
    io:format("Hello, world!~n").
