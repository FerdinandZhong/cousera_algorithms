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
        self.X = set()
        for line in edges:
            element = line.split()
            self.X.add(int(element[0]))
            if int(element[0]) not in self.graph:
                self.graph[int(element[0])] = [(int(element[1]), int(element[2]))]
            else:
                self.graph[int(element[0])].append((int(element[1]), int(element[2])))
        first_element = edges[0].split()
        self.V.add(int(first_element[0]))
        self.X.remove(int(first_element[0]))
        print(self.V, self.X)
        print(self.graph)

    def create_heap(self):
        cut = {}
        current_heap = heap(key=lambda x: x[1])
        for v in self.V:
            connected_nodes = [node for node in self.graph.get(v) if node[0] not in self.V]
            for connected_node in connected_nodes:
                if connected_node[0] not in cut:
                    cut[connected_node[0]] = connected_node
                else:
                    if cut[connected_node[0]][1] <= connected_node[1]:
                        continue
                    else:
                        cut[connected_node[0]][1] = connected_node
        for cut in cut.values():
            current_heap.push(cut)
        print([item[1] for item in current_heap._data])
        return current_heap

    def find_prim(self):
        total_cost = 0
        while len(self.X) > 0:
            current_heap = self.create_heap()
            selected = current_heap.peek()
            self.X.add(selected[1][0])
            self.V.remove(selected[1][0])
            total_cost += selected[0]
        return total_cost



if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/prim_test.txt') as f:
        content = f.readlines()
    total_numbers = content[0]
    edges = content[1:]
    prim_algorithm = prim_algorithm(edges)
    # prim_algorithm.create_heap()
    print(prim_algorithm.find_prim())