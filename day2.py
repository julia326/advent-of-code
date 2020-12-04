from collections import defaultdict


def is_valid_1(policy, password):
    [interval, char] = policy.split(' ')
    [min_count, max_count] = [int(x) for x in interval.split('-')]
    # count up all letters in the password
    letter_count = defaultdict(int)
    for letter in password:
        letter_count[letter] += 1

    return letter_count[char] >= min_count and letter_count[char] <= max_count


def is_valid_2(policy, password):
    [positions, char] = policy.split(' ')
    num_matches = 0
    for pos in positions.split('-'):
        if password[int(pos)-1] == char:
            num_matches += 1
    return num_matches == 1


def main():
    with open('inputs/input2.txt') as f:
        password_lines = f.read().split('\n')
    print(len(password_lines))

    valid_password_count = 0
    for password_line in password_lines:
        [policy, password] = password_line.split(': ')
        if is_valid_2(policy, password):
            valid_password_count += 1

    print(valid_password_count)


if __name__ == "__main__":
    main()
