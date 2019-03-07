import heapq
import os

class heap(object):
    def __init__(self, initial=None, key=lambda x:x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def peek(self):
        return self._data[0][1]

class prim_algorithm():
    def __init__(self, edges):
        self.graph = {}
        self.V = set()
        self.Left_nodes = set()
        self.current_heap = heap(key=lambda x: x[1])
        for line in edges:
            element = line.split()
            self.Left_nodes.add(int(element[0]))
            self.Left_nodes.add(int(element[1]))
            # need to keep double sides, since it's undirected graph
            if int(element[0]) not in self.graph:
                self.graph[int(element[0])] = [(int(element[1]), int(element[2]))]
            else:
                self.graph[int(element[0])].append((int(element[1]), int(element[2])))
            if int(element[1]) not in self.graph:
                self.graph[int(element[1])] = [(int(element[0]), int(element[2]))]
            else:
                self.graph[int(element[1])].append((int(element[0]), int(element[2])))
        first_element = edges[0].split()
        self.V.add(int(first_element[0]))
        self.Left_nodes.remove(int(first_element[0]))
        # print(self.V, self.Left_nodes)
        # print(self.graph)

    def create_heap(self):
        cut = {}
        for v in self.V:
            if v in self.graph:
                connected_nodes = [node for node in self.graph.get(v) if node[0] not in self.V]
                # print("connected node : {}".format(connected_nodes))
                for connected_node in connected_nodes:
                    if connected_node[0] not in cut:
                        cut[connected_node[0]] = connected_node
                    else:
                        if cut[connected_node[0]][1] <= connected_node[1]:
                            continue
                        else:
                            cut[connected_node[0]] = connected_node
            else:
                continue
        for cut in cut.values():
            self.current_heap.push(cut)
        # print([item[1] for item in self.current_heap._data])
        # print("heap: {}".format(self.current_heap._data))
        return self.current_heap

    def extract_min(self):
        while True:
            smallest_value = self.current_heap.pop()
            # print("retrieved smallest value: {}".format(smallest_value))
            if smallest_value[0] in self.V:
                continue
            else:
                return smallest_value

    def find_prim(self):
        total_cost = 0
        while len(self.Left_nodes) > 0:
            self.create_heap()
            selected = self.extract_min()
            self.V.add(selected[0])
            self.Left_nodes.remove(selected[0])
            # print("current V: {}, Left Nodes: {}".format(self.V, self.Left_nodes))
            total_cost += selected[1]
        return total_cost



if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/edges.txt') as f:
        content = f.readlines()
    total_numbers = content[0]
    edges = content[1:]
    prim_algorithm = prim_algorithm(edges)
    # prim_algorithm.create_heap()
    print(prim_algorithm.find_prim())