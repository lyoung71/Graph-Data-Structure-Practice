class Vertex:
    def __init__(self, val):
        self.val = val
        self.adjacent_vertices = []

    def __str__(self):
        return str(self.val) + ' adjacent: ' + str([x for x in self.adjacent_vertices])

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        else:
            self.adjacent_vertices.append(vertex)

    def get_connections(self):
        return self.adjacent_vertices

    def get_val(self):
        return self.val

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, val):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(val)
        self.vert_dict[val] = new_vertex
        return new_vertex

    def get_vertex(self, v):
        if v in self.vert_dict:
            return self.vert_dict[v]
        else:
            return None

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_adjacent_vertex(self.vert_dict[to])
        self.vert_dict[to].add_adjacent_vertex(self.vert_dict[frm])

    def get_vertices(self):
        return self.vert_dict.keys()


    def dfs_traverse(self, vertex, visited_vertices={}):
        visited_vertices[vertex] = True
        print(vertex)

        for vert in self.adjacent_vertices:
            if visited_vertices[vert]:
                continue
            self.dfs_traverse(self, vert, visited_vertices)


g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('a', 'f')
g.add_edge('b', 'c')
g.add_edge('b', 'd')
g.add_edge('c', 'd')
g.add_edge('c', 'f')
g.add_edge('d', 'e')
g.add_edge('e', 'f')
