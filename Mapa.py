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

def create_map():
    map_ = {}
    i = int(input("Quantidade de regiões: "))
    for i in range(i):
        country = input("Digite o nome da %dº região: " % (i + 1))
        print("Digite o nome das regiões vizinhas separadas por [,]: ")
        print("Ex: Recife,Olinda,Camaragibe")
        neighbours = list(input().split(","))
        map_[country] = neighbours

    return map_

colors = find_graph_colors(create_map())
min_color = (max(list(colors.values()))) + 1
print("Número mínimo de %d cores no mapa." % min_color)
