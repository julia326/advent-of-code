def decode_binary_str(input, is_row):
    sum = 0
    zero_char = 'F' if is_row else 'L'
    for i in range(len(input)):
        sum += (0 if input[-1*(i+1)] == zero_char else pow(2, i))
    return sum


def decode(seat):
    return (decode_binary_str(seat[:7], is_row=True), decode_binary_str(seat[-3:], is_row=False))


def seat_id(seat):
    decoded_seat = decode(seat)
    return decoded_seat[0] * 8 + decoded_seat[1]


def puzzle1():
    print(seat_id('BBBFFBFLLR'))


def puzzle2():
    # compute all seat IDs in input
    with open('inputs/input5.txt') as f:
        seats = f.read().split()

    sorted_seat_ids = sorted(seat_id(seat) for seat in seats)
    for i in range(1, len(sorted_seat_ids)):
        if sorted_seat_ids[i] - sorted_seat_ids[i-1] == 2:
            print(sorted_seat_ids[i]-1)


def main():
    puzzle2()


if __name__ == "__main__":
    main()
