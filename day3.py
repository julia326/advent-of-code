import pandas as pd


def move1(i, j):
    return i+1, j+3

def move2(i, j):
    return i+1, j+1

def move3(i, j):
    return i+1, j+5

def move4(i, j):
    return i+1, j+7

def move5(i, j):
    return i+2, j+1


def compute_tree_count_with_move(matrix, move_func):
    row_num, col_num = [0, 0]
    tree_count = 0
    while row_num < len(matrix) - 1:  # until we reach the bottom
        row_num, col_num = move_func(row_num, col_num)
        try:
            val = matrix[row_num][col_num]
        except IndexError:
            import pdb; pdb.set_trace()
        if val == '#':
            tree_count += 1
        elif val == '.':
            pass
        else:
            raise ValueError("Unexpected val: %s" % val)
    return tree_count


def main():
    with open('input3.txt') as f:
        trees = f.read().split()

    list_of_lists = []
    # repeat the pattern first to make this a square, make a processed input file
    # if the line is 5 chars but 100 lines, need to repeat the line 100/5 = 20 times
    # so if the line is k chars long but n lines, need to repeat the line n/k times
    num_lines = len(trees)
    num_trees = len(trees[0])
    num_repeats = (round(num_lines / num_trees) + 1) * 7
    for line in trees:
        line_list = list(line * num_repeats)
        list_of_lists.append(line_list)

    tree_count1 = compute_tree_count_with_move(list_of_lists, move1)
    tree_count2 = compute_tree_count_with_move(list_of_lists, move2)
    tree_count3 = compute_tree_count_with_move(list_of_lists, move3)
    tree_count4 = compute_tree_count_with_move(list_of_lists, move4)
    tree_count5 = compute_tree_count_with_move(list_of_lists, move5)
    print(tree_count1 * tree_count2 * tree_count3 * tree_count4 * tree_count5)


if __name__ == "__main__":
    main()