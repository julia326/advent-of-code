import re


# these 2 functions from https://wiki.python.org/moin/BitManipulation
def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

def process_mask(mask):
    clear_bits = []
    set_bits = []
    for i, bit in enumerate(list(reversed(mask))):
        if bit == 'X':
            continue
        bit = int(bit)
        if bit == 1:
            set_bits.append(i)
        elif bit == 0:
            clear_bits.append(i)
    return set_bits, clear_bits


def apply_mask_puzzle1(mask, value):
    set_bits, clear_bits = process_mask(mask)
    for set_bit in set_bits:
        value = setBit(value, set_bit)
    for clear_bit in clear_bits:
        value = clearBit(value, clear_bit)
    return value


def puzzle1(instructions):
    datastore = {}
    mask = None
    for line in instructions:
        if line.startswith('mask'):  # reset the mask we're working with
            mask = line.split(' = ')[1]
            continue
        address, value = re.search('\[(.+?)\] = (.+?)$', line).groups()  # okay fine regex

        value = apply_mask_puzzle1(mask, int(value))
        datastore[int(address)] = value
    print(sum(datastore.values()))


def binstr(i, size):
    return bin(i)[2:].zfill(size)


# returns a list of resolved addresses (strings) after applying floating bits
def generate_all_addresses(masked_address):
    # each X is a floating bit, can be 0 or 1
    floating_pos = []
    for i, char in enumerate(masked_address):
        if char == 'X':
            floating_pos.append(i)
    num_floating_pos = len(floating_pos)
    new_masks = []
    for i in range(2**num_floating_pos):
        bin_str = binstr(i, num_floating_pos)
        new_mask = list(masked_address)
        # replace the X's with the chars in this order to generate one mask
        for i, pos in enumerate(floating_pos):
            new_mask[pos] = bin_str[i]
        new_mask = ''.join(new_mask)
        new_masks.append(new_mask)
    return new_masks


def apply_mask_puzzle2(mask, value):
    # replace the X's with 0s, binary or with value
    value |= int(mask.replace('X', '0'), 2)
    value_list = list(binstr(value, len(mask)))

    # set floating bits
    for i, char in enumerate(mask):
        if char == 'X':
            value_list[i] = 'X'

    return ''.join(value_list)


def puzzle2(instructions):
    datastore = {}
    for line in instructions:
        if line.startswith('mask'):  # reset the mask we're working with
            mask = line.split(' = ')[1]
            continue
        # figure out all addresses for this mask
        address, value = re.search('\[(.+?)\] = (.+?)$', line).groups()
        # what are all the addresess?
        masked_address = apply_mask_puzzle2(mask, int(address))
        all_addresses = generate_all_addresses(masked_address)
        for address in all_addresses:
            datastore[int(address, 2)] = int(value)

    print(sum(datastore.values()))


def main():
    with open('inputs/input14.txt') as f:
        instructions = f.read().split('\n')
    puzzle1(instructions)


if __name__ == "__main__":
    main()
