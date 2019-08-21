def try_coloring(graph, num_colors):
    assert num_colors >= 0, "Invalid number of colors: %s" % num_colors
    colors = {}

    def neighbors_have_different_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)

    for node, adjacents in graph.items():

        found_color = False

        for color in range(num_colors):
            if neighbors_have_different_colors(adjacents, color):
                found_color = True
                colors[node] = color
                break

        if not found_color:
            return None

    return colors


def find_graph_colors(graph):
    for num_colors in range(1, len(graph)):
        colors = try_coloring(graph, num_colors)
        if colors:
            return colors

'''
grafo = {
    '1': ['2', '5'],
    '2': ['1', '3', '5', '6', '7'],
    '3': ['2', '4', '7', '8'],
    '4': ['3', '8'],
    '5': ['1', '2', '6', '8'],
    '6': ['2', '5', '7', '8'],
    '7': ['2', '3', '6', '8'],
    '8': ['3', '4', '5', '6', '7']
    }

'''
grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    }

colors = find_graph_colors(grafo)
min_color = (max(list(colors.values()))) + 1
print("Número mínimo de %d cores no mapa." % min_color)