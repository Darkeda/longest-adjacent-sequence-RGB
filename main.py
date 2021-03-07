import argparse
import sys
import numpy as np

init_rows = 0
init_cols = 0
matrix = []
highest_counter = 0
visited = []



def scipt_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), nargs='*')
    args = parser.parse_args()

    if not args.file:
        print("Please input rows and cols\n")
        user_reader()
    else:
        file_reader(args.file)


def file_reader(list: list):
    global init_rows, init_cols, matrix

    for f in list:
        text = []
        for line in f:
            text.append(line)

        size = text.pop(0).split(" ")
        init_rows = int(size[0])
        init_cols = int(size[1])
        for line in text:
            matrix.append(line.split())
        init_visited(init_rows, init_rows)
        print(find_longest_adjacent_sequence())
        reset_everything()


def user_reader():
    global init_rows, init_cols, matrix
    first_line = input()
    combo = first_line.split(" ")
    init_rows = int(combo[0])
    init_cols = int(combo[1])

    for i in range(init_rows):
        row = input()
        matrix.append(row.split())
    init_visited(init_rows, init_rows)
    print(find_longest_adjacent_sequence())
    reset_everything()


def init_visited(rows: int, cols: int):
    global visited
    visited = np.zeros((rows, cols))


def reset_everything():
    global init_rows, init_cols, matrix, highest_counter, visited
    init_rows = 0
    init_cols = 0
    matrix = []
    highest_counter = 0
    visited = []


def reset_visited():
    global visited
    visited = np.clip(visited, 0, 0)


def is_it_same_char(char, list):
    global init_rows, init_cols
    combined = sum([i.count(char) for i in list])
    if combined == init_rows * init_cols:
        return True
    return False


def BFS(current_symbol, next_symbol, next_row: int, next_col: int):
    global highest_counter

    if current_symbol != next_symbol:
        return

    visited[next_row][next_col] = 1
    row_to_move = [0, 0, 1, -1]
    col_to_move = [1, -1, 0, 0]
    highest_counter += 1

    for number in range(4):
        if is_next_valid(row_to_move[number] + next_row, col_to_move[number] + next_col, current_symbol):
            BFS(current_symbol, next_symbol, row_to_move[number] + next_row, col_to_move[number] + next_col)


def is_next_valid(next_row: int, next_col: int, symbol):
    global matrix, init_rows, init_cols
    if init_rows > next_row >= 0 and init_cols > next_col >= 0:

        if matrix[next_row][next_col] == symbol and visited[next_row][next_col] == 0:
            return True
        else:

            return False
    else:

        return False


def find_longest_adjacent_sequence():
    global init_rows, init_cols, matrix, highest_counter
    max = -1

    if is_it_same_char(matrix[0][0], matrix):
        return init_rows * init_cols

    for i in range(init_rows):
        for t in range(init_cols):
            reset_visited()
            highest_counter = 0

            if i + 1 < init_rows:
                BFS(matrix[i][t], matrix[i + 1][t], i, t)

            if highest_counter > max:
                max = highest_counter

            reset_visited()
            highest_counter = 0

            if t + 1 < init_cols:
                BFS(matrix[i][t], matrix[i][t + 1], i, t)

            if highest_counter > max:
                max = highest_counter

    return max


if __name__ == '__main__':
    scipt_input()
