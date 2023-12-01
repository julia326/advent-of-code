import networkx as nx


# parse each line to get a list of weighted edges to pass to DAG
def edges_from_rule(rule):
    a = rule.split(' contain ')
    from_node = a[0][:-5]
    if rule.endswith('contain no other bags.'):  # it's a leaf, no edges
        return []

    edges = []
    for to_node_text in a[1].split(', '):
        # extract color and edge weight
        split_text = to_node_text.split(' ')
        to_node = ' '.join(split_text[1:3])
        weight = int(split_text[0])
        edges.append((from_node, to_node, weight))
    return edges


def puzzle1(rules):
    dg = nx.DiGraph()
    # make a DAG with all the rules
    for rule in rules:
        dg.add_weighted_edges_from(edges_from_rule(rule))

    count = sum(nx.has_path(dg, node, 'shiny gold') for node in dg.nodes) - 1  # subtract shiny gold
    print(count)


def get_tree_sum(dg, node):
    # if node is leaf node, return 0
    out_edges = list(dg.out_edges(node))
    if len(out_edges) == 0:
        return 0

    # add up subtree sums
    total = 0
    for edge in out_edges:
        next_node = edge[1]
        weight = dg.get_edge_data(node, next_node)['weight']
        total += weight * (get_tree_sum(dg, next_node) + 1)
    return total


def puzzle2(rules):
    dg = nx.DiGraph()
    for rule in rules:
        dg.add_weighted_edges_from(edges_from_rule(rule))

    print(get_tree_sum(dg, 'shiny gold'))


def main():
    # read in all rules
    input_path = 'inputs/input7.txt'
    with open(input_path) as f:
        rules = f.read().split('\n')
    puzzle2(rules)


if __name__ == "__main__":
    main()