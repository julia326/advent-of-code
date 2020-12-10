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
    if cur_num > target:  # invalid path
        return 0

    out = 0
    for incr in [1, 2, 3]:
        next_num = cur_num + incr
        if next_num in jolts:
            out += is_path(next_num, target, jolts)
    return out


def puzzle2_recursive_takes_too_long_and_does_not_work(jolts):
    start = time.time()
    max_jolts = max(jolts)
    print(max_jolts)
    jolts = set(jolts)
    print(is_path(0, max_jolts, jolts))
    end = time.time()
    print(end - start)


def puzzle2(jolts):
    max_jolts = max(jolts)

    count = defaultdict(int)
    # memoize the number of paths from each adapter to the target, and keep track of the count
    count[jolts[0]] = 1
    for i in range(1, len(jolts)):
        # how many paths are there from this element to the sink?
        jolt = jolts[i]
        for j in [1, 2, 3]:
            if (jolt - j) in count:
                count[jolt] += count[jolt - j]
    print(count[max_jolts])


def main():
    with open('inputs/input10.txt') as f:
        jolts = sorted(list(map(int, f.read().split('\n'))))
    jolts.insert(0, 0)  # diff to original voltage
    puzzle2(jolts)


if __name__ == "__main__":
    main()
