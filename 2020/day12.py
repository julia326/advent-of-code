ORDER = ['N', 'E', 'S', 'W']


def get_facing(current_facing, direction, amount):
    num_turns = int(amount/90)    
    cur_index = ORDER.index(current_facing)
    next_index = (cur_index + num_turns) % 4 if direction == 'R' else (cur_index - num_turns) % 4
    return ORDER[next_index]


def update_pos(var_to_read, i, j, amount):
    if var_to_read == 'N':
        j += amount
    elif var_to_read == 'S':
        j -= amount
    elif var_to_read == 'E':
        i += amount
    elif var_to_read == 'W':
        i -= amount
    else:
        raise ValueError('unexpected var: %s' % var_to_read)
    return i, j


def puzzle1(moves):
    i, j = 0, 0
    facing = 'E'
    for move in moves:
        direction = move[0]
        amount = int(move[1:])
        if direction in ORDER:
            i, j = update_pos(direction, i, j, amount)

        elif direction == 'F':
            i, j = update_pos(facing, i, j, amount)

        else:
            facing = get_facing(facing, direction, amount)

    print(abs(i) + abs(j))


def compute_r90_rotations(direction, amount):
    num_turns = int(amount/90)
    return (num_turns if direction == 'R' else 4 - num_turns)


def update_waypoint_pos(ship_i, ship_j, waypoint_i, waypoint_j, direction, amount):
    # MATH
    offset_i, offset_j = waypoint_i - ship_i, waypoint_j - ship_j
    # figure out how many R90 rotations we need
    num_turns = int(amount/90)
    num_r90_turns = (num_turns if direction == 'R' else 4 - num_turns)
    for i in range(num_r90_turns):
        waypoint_i, waypoint_j = ship_i + offset_j, ship_j - offset_i
        offset_i, offset_j = waypoint_i - ship_i, waypoint_j - ship_j  # recompute offsets
    return waypoint_i, waypoint_j


def puzzle2(moves):
    i, j = 0, 0
    waypoint_i, waypoint_j = 10, 1
    for move in moves:
        # the only direction that actually moves the ship is an F
        direction = move[0]
        amount = int(move[1:])
        if direction == 'F':
            # move to the waypoint "amount" number of times
            incr_i, incr_j = waypoint_i - i, waypoint_j - j  # distance to waypoint
            i += (amount * incr_i)  # new positions
            j += (amount * incr_j)
            waypoint_i, waypoint_j = i + incr_i, j + incr_j  # reset waypoint
        elif direction in ORDER:  # only change waypoint, not ship position
            waypoint_i, waypoint_j = update_pos(direction, waypoint_i, waypoint_j, amount)
        else:
            waypoint_i, waypoint_j = update_waypoint_pos(i, j, waypoint_i, waypoint_j, direction, amount)
    print(abs(i) + abs(j))


def main():
    with open('inputs/input12.txt') as f:
        moves = f.read().split('\n')
    puzzle2(moves)


if __name__ == "__main__":
    main()
