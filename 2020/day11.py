from collections import Counter
import time


def count_adjacent_seats(matrix, row, col):
    seats = []
    for i in [row-1, row, row+1]:
        for j in [col-1, col, col+1]:
            if i == row and j == col or i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]):
                continue
            seats.append(matrix[i][j])
    return Counter(seats)


def count_first_seen_seats(matrix, row, col):
    seats = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    def get_range_up():
        return reversed(range(row))

    def get_range_down():
        return range(row+1, num_rows)

    def get_range_left():
        return reversed(range(col))

    def get_range_right():
        return range(col+1, num_cols)

    def maybe_add_to_seats(pos_list):
        for i, j in pos_list:
            if matrix[i][j] != '.':  # it's a seat
                seats.append(matrix[i][j])
                return

    # N
    pos_list = list(zip(get_range_up(), [col]*num_cols))
    maybe_add_to_seats(pos_list)

    # E
    pos_list = list(zip([row]*num_rows, get_range_right()))
    maybe_add_to_seats(pos_list)

    # S
    pos_list = list(zip(get_range_down(), [col]*num_cols))
    maybe_add_to_seats(pos_list)

    # W
    pos_list = list(zip([row]*num_rows, get_range_left()))
    maybe_add_to_seats(pos_list)

    # diagonal: NE
    pos_list = list(zip(get_range_up(), get_range_right()))
    maybe_add_to_seats(pos_list)

    # diagonal: SE
    pos_list = list(zip(get_range_down(), get_range_right()))
    maybe_add_to_seats(pos_list)

    # diagonal: SW
    pos_list = list(zip(get_range_down(), get_range_left()))
    maybe_add_to_seats(pos_list)

    # diagonal: NW
    pos_list = list(zip(get_range_up(), get_range_left()))
    maybe_add_to_seats(pos_list)

    return Counter(seats)


def get_next_seat_value(matrix, row, col, cutoff=4, adjacency_func=count_adjacent_seats):
    cur_seat = matrix[row][col]

    # Floor (.) never changes; seats don't move, and nobody sits on the floor.
    if cur_seat == '.':
        return cur_seat

    counter = adjacency_func(matrix, row, col)

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if cur_seat == 'L' and counter['#'] == 0:
        return '#'

    # If a seat is occupied (#) and <cutoff> or more seats adjacent to it are also occupied, the seat becomes empty.
    if cur_seat == '#' and counter['#'] >= cutoff:
        return 'L'

    # Otherwise, the seat's state does not change.
    return cur_seat


def run_round_puzzle1(seats):
    new_seats = []
    for i, row in enumerate(seats):
        new_row = [get_next_seat_value(seats, i, j) for j in range(len(row))]
        new_seats.append(new_row)
    return new_seats


def run_round_puzzle2(seats):
    new_seats = []
    for i, row in enumerate(seats):
        new_row = [get_next_seat_value(seats, i, j, cutoff=5, adjacency_func=count_first_seen_seats) for j in range(len(row))]
        new_seats.append(new_row)
    return new_seats


def puzzle(seats, run_round_func):
    start = time.time()
    print(len(seats))
    while True:
        new_seats = run_round_func(seats)
        if new_seats == seats:
            break
        seats = new_seats

    # count occupied seats
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1
    print(occupied)
    end = time.time()
    print(end - start)



def main():
    with open('inputs/input11.txt') as f:
        seats = f.read().split('\n')
    puzzle(seats, run_round_puzzle2)


if __name__ == "__main__":
    main()
