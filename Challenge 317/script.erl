% https://www.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/

-module(main).
-export([main/0]).

production($a) -> "bc";
production($b) -> "a";
production($c) -> "aaa".

collatz(Word, History) ->
    case string:length(Word) < 2 of
        true -> lists:reverse(History);
        false ->
            Suffix = production(lists:nth(1, Word)),
            NewWord = string:slice(Word, 2) ++ Suffix,
            collatz(NewWord, [NewWord|History])
    end.

collatz(Word) -> collatz(Word, []).

print([]) -> ok;
print([H|T]) ->
    io:format("~s~n", [H]),
    print(T).

main() ->
    print(collatz("aaa")).
