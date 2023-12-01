import itertools


def find_sum_2020_subset(nums, k):
    for comb in itertools.combinations(nums, k):
        if sum(comb) == 2020:
            print(comb)
            product = 1
            for num in comb:
                product *= num
            print(product)


def puzzle1():
    with open('inputs/input1.txt') as f:
        nums = [int(x) for x in f.read().split()]
    find_sum_2020_subset(nums, 2)


def puzzle2():
    with open('inputs/input1.txt') as f:
        nums = [int(x) for x in f.read().split()]
    find_sum_2020_subset(nums, 3)


def main():
    puzzle2()


if __name__ == "__main__":
    main()
