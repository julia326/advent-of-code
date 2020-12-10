from collections import defaultdict
import time


def puzzle1(jolts):
    # count up how many step sizes of 1, 2, 3
    counts = defaultdict(int)
    counts[3] = 1  # built-in adapter
    for i in range(1, len(jolts)):
        counts[jolts[i]-jolts[i-1]] += 1
    print(counts)
    print(counts[1] * counts[3])


def is_path(cur_num, target, jolts):
    if cur_num == target:  # path is valid and reached end
        return 1
    if cur_num not in jolts:
        return 0
    return is_path(cur_num + 1, target, jolts) + \
        is_path(cur_num + 2, target, jolts) + \
        is_path(cur_num + 3, target, jolts)


def puzzle2(jolts):
    start = time.time()
    print(max(jolts))
    jolts = set(jolts)
    print(is_path(0, max(jolts), jolts))
    end = time.time()
    print(end - start)


def is_path_more_efficient(cur_num, target, jolts):
    if cur_num == target:  # path is valid and reached end
        return 1
    if cur_num not in jolts:
        return 0

    # remove current element before passing down the tree
    jolts.discard(cur_num)
    return is_path_more_efficient(cur_num + 1, target, jolts) + \
        is_path_more_efficient(cur_num + 2, target, jolts) + \
        is_path_more_efficient(cur_num + 3, target, jolts)


def puzzle2_more_efficient(jolts):
    start = time.time()
    max_jolts = max(jolts)
    print(max_jolts)
    jolts = set(jolts)
    print(is_path(0, max_jolts, jolts))
    end = time.time()
    print(end - start)


def main():
    with open('inputs/input10.txt') as f:
        jolts = sorted(list(map(int, f.read().split('\n'))))
    jolts.insert(0, 0)  # diff to original voltage
    puzzle2_more_efficient(jolts)


if __name__ == "__main__":
    main()
