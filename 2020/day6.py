from collections import Counter


def puzzle1():
    with open('inputs/input6.txt') as f:
        total = sum(len(set(group.replace('\n', ''))) for group in f.read().split('\n\n'))
        print(total)


def puzzle2():
    with open('inputs/input6.txt') as f:
        total = sum(
            sum(
                x == len(group.split('\n')) for x in Counter(group.replace('\n', '')).values()
            ) for group in f.read().split('\n\n'))
        print(total)


def main():
    puzzle2()


if __name__ == "__main__":
    main()