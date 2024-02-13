def find_lowest_cost_node(costs_map,processed,finish):
    lowest_cost = costs_map[finish]
    lowest_cost_node = None
    for node,cost in costs_map.items():
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node




def find_fastest_path(graph, start, finish):
    costs_map = {node:float("inf") for node in graph.keys()}
    parents_map = {node:None for node in graph.keys()}
    costs_map[start] = 0
    initial_neighbours = graph[start]
    for neighbor in initial_neighbours:
        costs_map[neighbor] = initial_neighbours[neighbor]
        parents_map[neighbor] = start
    processed = [start]
    node = find_lowest_cost_node(costs_map,processed,finish)
    while node != None:
        cost  = costs_map[node]
        neighbors = graph[node]
        for neighbour_node, neighbour_cost in neighbors.items():
            new_cost  = cost + neighbour_cost
            if costs_map[neighbour_node] > new_cost:
                costs_map[neighbour_node] = new_cost
                parents_map[neighbour_node] = node
        
        processed.append(node)
        node = find_lowest_cost_node(costs_map, processed,finish)

    if parents_map[finish] != None:
        stack = [finish]
        previous_node = parents_map[finish]
        while previous_node :
            stack.append(previous_node)
            previous_node = parents_map.get(previous_node)
        print(f"Found a path from {start} to {finish}! It takes {costs_map[finish]} to cover.The route is {'>'.join(reversed(stack))}")
    else:
        print("Sorry no path found!")


graph = {
    "BOOK":{
        "LP":5,
        "POSTER":0
    },
    "LP":{"GUITAR":15,"DRUM":20,"BOOK":3},
    "POSTER":{"GUITAR":30,"DRUM":35,"LP":4},
    "GUITAR":{"PIANO":20},
    "DRUM":{"PIANO":10} ,
    "PIANO":{"BOOK":50}  
}

find_fastest_path(graph,"POSTER","BOOK")