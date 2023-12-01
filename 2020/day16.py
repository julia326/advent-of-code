from collections import defaultdict
from io import StringIO
import pandas as pd


def get_ranges_with_field(tickets):
    out = {}
    for line in tickets:
        if ': ' in line:  # specifies a range
            field, ranges = line.split(': ')
            range_list = []
            for range_str in ranges.split(' or '):
                min_val, max_val = map(int, range_str.split('-'))
                range_list.append((min_val, max_val))
            out[field] = range_list
    return out


def get_ranges(tickets):
    ranges_with_field = get_ranges_with_field(tickets)
    return [item for sublist in ranges_with_field.values() for item in sublist]


def get_ranges_with_field(tickets):
    out = {}
    for line in tickets:
        if ': ' in line:  # specifies a range
            field, ranges = line.split(': ')
            range_list = []
            for range_str in ranges.split(' or '):
                min_val, max_val = map(int, range_str.split('-'))
                range_list.append((min_val, max_val))
            out[field] = range_list
    return out


def is_valid(value, range_list):
    return any(value >= min_value and value <= max_value for (min_value, max_value) in range_list)


def puzzle1(tickets):
    ranges = get_ranges(tickets)

    invalid_value_total = 0
    nearby_ticket_start = tickets.index('nearby tickets:')
    for ticket in tickets[nearby_ticket_start+1:]:
        for value in map(int, ticket.split(',')):
            if not is_valid(value, ranges):
                invalid_value_total += value
    print(invalid_value_total)


def match_values_to_field(field_values, ranges_with_fields):
    valid_field_names = []
    for field_name, range_list in ranges_with_fields.items():
        # are all of these field values legal?
        if all(is_valid(value, range_list) for value in field_values):
            valid_field_names.append(field_name)
    return valid_field_names


def puzzle2(tickets):
    ranges = get_ranges(tickets)

    valid_ticket_lines = []
    # throw out any invalid tickets first
    for ticket in tickets[tickets.index('nearby tickets:')+1:]:
        if all(is_valid(value, ranges) for value in map(int, ticket.split(','))):
            valid_ticket_lines.append(ticket)

    data = pd.read_csv(StringIO('\n'.join(valid_ticket_lines)), header=None)

    # field position possibilities, which we'll have to resolve after
    possible_field_positions = defaultdict(set)
    ranges_with_fields = get_ranges_with_field(tickets)

    for col in range(data.shape[1]):
        field_values = list(data[col])
        field_names = match_values_to_field(field_values, ranges_with_fields)
        for field_name in field_names:
            possible_field_positions[field_name].add(col)

    # do value resolution: find the one with only one possibility, remove it from other fields, etc.
    resolved_fields = {}  # field to pos
    last_resolved_field = None
    while True:
        for field, pos_set in possible_field_positions.items():
            if len(pos_set) == 1:
                resolved_fields[field] = pos_set.pop()
                last_resolved_field = field
                break
        # update the possible list
        del possible_field_positions[last_resolved_field]
        for field, pos_set in possible_field_positions.items():
            if resolved_fields[last_resolved_field] in pos_set:
                pos_set.remove(resolved_fields[last_resolved_field])

        # are we done?
        if len(possible_field_positions) == 0:
            break

    # what are my ticket fields?
    my_ticket = list(map(int, tickets[tickets.index('your ticket:')+1].split(',')))

    # match attributes with ticket numbers
    fields_to_values = {}
    for field, index in resolved_fields.items():
        fields_to_values[field] = my_ticket[index]

    # which ones start with "departure"?
    product = 1
    for field, value in fields_to_values.items():
        if field.startswith('departure'):
            product *= value
    print(product)


def main():
    with open('inputs/input16.txt') as f:
        tickets = f.read().split('\n')
    puzzle2(tickets)


if __name__ == "__main__":
    main()
