def is_valid_passport(passport_dict):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    # all required keys must be there
    missing_required_keys = required_keys.difference(set(passport_dict.keys()))
    return len(missing_required_keys) == 0 or missing_required_keys == {'cid'}


def interval(num, min_val, max_val):
    return num >= min_val and num <= max_val


def is_valid_passport_strict(passport_dict):
    if not is_valid_passport(passport_dict):  # quick check first for field presence
        return False

    byr = passport_dict['byr']  # byr (Birth Year) - four digits; at least 1920 and at most 2002
    try:
        if not interval(int(byr), 1920, 2002):
            return False
    except ValueError:  # not an int
        return False

    iyr = passport_dict['iyr']  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    try:
        if not interval(int(iyr), 2010, 2020):
            return False
    except ValueError:  # not an int
        return False

    eyr = passport_dict['eyr']  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    try:
        if not interval(int(eyr), 2020, 2030):
            return False
    except ValueError:  # not an int
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    hgt = passport_dict['hgt']
    hgt_num = hgt[:-2]
    unit = hgt[-2:]
    try:
        if unit == 'cm':
            if not interval(int(hgt_num), 150, 193):
                return False
        elif unit == 'in':
            if not interval(int(hgt_num), 59, 76):
                return False
        else:  # unknown unit
            return False

    except ValueError:  # not an int
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = passport_dict['hcl']
    if not hcl.startswith('#'):
        return False
    hcl = hcl[1:]
    try:
        hcl = int(hcl, 16)
    except ValueError:  # not a hex string
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl = passport_dict['ecl']
    if ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = passport_dict['pid']
    if len(pid) != 9:
        return False
    try:
        pid = int(pid)
    except ValueError:  # not an int
        return False

    return True


def main():
    with open('inputs/input4.txt') as f:
        passports = f.read().split('\n\n')

    valid_passport_count = 0
    for passport in passports:
        # split into key-value pairs, convert into dict
        passport_key_values = passport.split()
        passport_dict = {}
        for key_value_pair in passport_key_values:
            key, value = key_value_pair.split(':')
            passport_dict[key] = value
        if is_valid_passport_strict(passport_dict):
            valid_passport_count += 1

    print(valid_passport_count)


if __name__ == "__main__":
    main()