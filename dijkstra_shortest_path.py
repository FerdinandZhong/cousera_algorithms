import sys
import os

class DijkstraShortestPath(object):
    def __init__(self, input_file):
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                line = line.split()
                self.graph[int(line[0])] = [tuple(map(int, x.split(','))) for x in line[1:]]

    def compute_vertices_keys(self, keys, crossing_edges, source, V):
        for edge in crossing_edges:
            if edge[0] not in V:
                if edge[0] in keys:
                    if edge[1] + keys[source][0] < keys[edge[0]][0]:
                        keys[edge[0]] = (edge[1] + keys[source][0], keys[edge[0]][1] + [source])
                else:
                    current = keys.get(source) or [0]
                    keys[edge[0]] = (edge[1] + current[0], list(V) + [source])
        return keys

    def first_e_qs(self, vertices, keys):
        n = len(vertices)
        if (n >= 2):
            pivot = vertices[0]
            i = 1
            tmp = 0
            for j in range(1, len(vertices)):
                if keys[pivot][0] > keys[vertices[j]][0]:
                    tmp = vertices[i]
                    vertices[i] = vertices[j]
                    vertices[j] = tmp
                    i = i + 1
            tmp = vertices[i - 1]
            vertices[i - 1] = pivot
            vertices[0] = tmp
            final_result = self.first_e_qs(vertices[:i - 1], keys)
            final_result.append(pivot)
            final_result.extend(self.first_e_qs(vertices[i:], keys))
            return final_result
        else:
            return vertices

    def find_paths(self):
        V = [1]
        V = set(V)
        keys = {}
        current_shortest = 1
        while set(self.graph.keys() - V):
            keys = self.compute_vertices_keys(keys, self.graph.get(current_shortest), current_shortest, V)
            current_shortest = self.first_e_qs(list(set(keys.keys()) - V), keys)[0]
            V.add(current_shortest)
        return keys



if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    dsp = DijkstraShortestPath(BASE_DIR + '/data/dijkstraData.txt')
    keys = dsp.find_paths()
    print(keys[7])
    print(keys[37])
    print(keys[59])
    print(keys[82])
    print(keys[99])
    print(keys[115])
    print(keys[133])
    print(keys[165])
    print(keys[188])
    print(keys[197])