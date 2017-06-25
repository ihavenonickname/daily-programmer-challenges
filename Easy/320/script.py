# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

import sys

def walk(initial_row, initial_col, size):
    last = size - 1

    # From upper left to upper right.
    for i in range(last):
        yield initial_row, initial_col + i

    # From upper right to bottom right.
    for i in range(last):
        yield initial_row + i, initial_col + last

    # From bottom right to bottom left.
    for i in range(last):
        yield initial_row + last, initial_col + last - i

    # From bottom left to upper left.
    for i in range(last):
        yield initial_row + last - i, initial_col

def walked_matrix(size):
    matrix = [list(range(size)) for _ in range(size)]

    matrix[size // 2][size // 2] = size ** 2

    counter = 1

    for i in range(size // 2):
        # Each row decreases 2 in size per walk (a cell from the left, another
        # from the right).
        row_size = size - (i * 2)

        # Each walk starts from a cell below and to the right.
        # (0, 0), (1, 1), (2, 2), ...
        for row, col in walk(i, i, row_size):
            matrix[row][col] = counter
            counter += 1

    return matrix

def main():
    size = int(sys.argv[1])

    for row in walked_matrix(size):
        print(" ".join("%2d" % cell for cell in row))
        print()

if __name__ == "__main__":
    main()
