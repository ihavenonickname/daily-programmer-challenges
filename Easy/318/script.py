# https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/

import sys
from itertools import permutations

def _challenge(numbers, parcial_result, target, history, ops):
    if not numbers:
        return target == parcial_result

    if not parcial_result:
        history.append(str(numbers[0]))
        return _challenge(numbers[1:], numbers[0], target, history, ops)

    for symbol, functions in ops:
        if not functions["requisite"](parcial_result, numbers[0]):
            continue

        history.append(symbol)
        history.append(str(numbers[0]))

        new_parcial = functions["eval"](parcial_result, numbers[0])

        if _challenge(numbers[1:], new_parcial, target, history, ops):
            return True

        history.pop()
        history.pop()

    return False

def challenge(numbers, target):
    ops = {
        "+": {
            "eval": lambda x, y: x + y,
            "requisite": lambda x, y: True
        },
        "-": {
            "eval": lambda x, y: x - y,
            "requisite": lambda x, y: True
        },
        "*": {
            "eval": lambda x, y: x * y,
            "requisite": lambda x, y: True
        },
        "/": {
            "eval": lambda x, y: x / y,
            "requisite": lambda x, y: y != 0
        }
    }.items()

    for permutation in permutations(numbers):
        history = []

        if _challenge(list(permutation), None, target, history, ops):
            return " ".join(history) + " = " + str(target)

    return None

def main():
    parsed_input = [int(x) for x in sys.argv[1].split(" ")]

    result = challenge(parsed_input[:-1], parsed_input[-1])

    if result:
        print(result)
    else:
        print("No result found")

if __name__ == "__main__":
    main()
