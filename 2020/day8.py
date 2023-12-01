def run_program(lines):
    # interpret each instruction line
    acc_value = 0
    hit_loop = False
    i = 0
    i_visited = set()
    while not hit_loop:
        if i == len(lines):  # we reached end_of_file without breaking the loop
            break
        elif i in i_visited:  # we hit the loop
            hit_loop = True
            continue
        i_visited.add(i)
        instruction, num = lines[i].split()
        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            acc_value += int(num)
            i += 1
        elif instruction == 'jmp':
            i += int(num)
        else:
            raise ValueError('unexpected instruction %s' % instruction)
        continue

    return (hit_loop, acc_value)


def puzzle1():
    with open('inputs/input8.txt') as f:
        lines = f.read().split('\n')
    hit_loop, acc_value = run_program(lines)
    print(acc_value)


def puzzle2():
    with open('inputs/input8.txt') as f:
        lines = f.read().split('\n')
    # go through each line, construct a new set of instructions to see if it terminates
    for i, line in enumerate(lines):
        if line.startswith('acc'):
            continue
        new_lines = lines.copy()
        new_lines[i] = line.replace('jmp', 'nop') if line.startswith('jmp') else line.replace('nop', 'jmp')
        hit_loop, acc_value = run_program(new_lines)
        if not hit_loop:
            print('It terminated! %d' % acc_value)
            break


def main():
    puzzle2()


if __name__ == "__main__":
    main()
