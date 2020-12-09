from itertools import combinations


def compute_all_pairs_sum(nums):
    sum_set = set()
    for (a, b) in combinations(nums, 2):
        sum_set.add(a + b)
    return sum_set


def puzzle1(lines, k):
    for i in range(k, len(lines)):
        # compute subset of lines
        lines_subset = lines[i-k:i]
        sum_set = compute_all_pairs_sum(lines_subset)
        if lines[i] not in sum_set:
            return lines[i]


def puzzle2(target, nums):
    # gross solution: given a target number, find the set of contiguous numbers that add to it
    for i in range(len(nums)):
        # if this is the starter number, there will exist a contiguous number after this that will
        # either add up to target or exceed it. continue until we equal or exceed
        running_sum = 0
        sum_range = []
        for j in range(i, len(nums)):
            running_sum += nums[j]
            sum_range.append(nums[j])
            if running_sum == target:
                print(min(sum_range) + max(sum_range))
                return
            elif running_sum > target:
                break


def main():
    with open('inputs/input9.txt') as f:
        lines = list(map(int, f.read().split('\n')))
    target = puzzle1(lines, k=25)
    puzzle2(target, lines)


if __name__ == "__main__":
    main()
