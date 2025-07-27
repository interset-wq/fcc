# https://cdn.freecodecamp.org/curriculum/python/graph1-example.png
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph: dict[str, list], 
                  start: str, 
                  target: str=''
                ) -> tuple[dict[str, float], dict[str, list[str]]]:

    """计算两个节点的最短距离"""

    # 未访问的节点
    unvisited = list(graph) # ['A', 'B', 'C', 'D', 'E', 'F']
    # 假定起始节点与其他节点的距离假定为无穷大
    # 起点到图上各个节点的最最短距离
    distances: dict[str, float] = {node: 0 if node == start else float('inf') for node in graph}
    # 用于记录最短路径
    paths: dict[str, list] = {node: [] for node in graph}
    # 最短路径的起点
    paths[start].append(start)
    
    while unvisited:
        # 到起始节点距离最短的节点
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    # distances起始节点到其他节点的最短距离
    # paths最短距离对应的路径
    return distances, paths
    
shortest_path(my_graph, 'B', 'E')