"""
Dijkstra's algorithm for weighted graphs (DAG)
"""


def find_lowest_cost_node(costs, processed):
    """
    calculate the lowest cost node
    :param costs: input with all costs known
    :param processed: list of all processed nodes
    :return: lowest cost node
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_algorithm():
    """
    Algorithm to find the shortest path
    :return: dictionary of all parents
    """
    infinity = float("inf")
    graph = {
        "start": {"a": 10},
        "a": {"c": 20},
        "b": {"a": 1},
        "c": {"fin": 30, "b": 1},
        "fin": {},
    }
    costs = {"a": 10, "b": infinity, "c": infinity, "fin": infinity}
    parents = {"a": "start", "b": "c", "c": "a", "fin": None}
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for name in neighbors.keys():
            new_cost = cost + neighbors[name]
            if costs[name] > new_cost:
                costs[name] = new_cost
                parents[name] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return parents


if __name__ == "__main__":
    print(dijkstra_algorithm())
