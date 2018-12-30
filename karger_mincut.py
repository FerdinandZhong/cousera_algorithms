import random
import os

def merge_graph(vertices):
    selected_position = random.randrange(0, len(vertices)-1)
    random_a = vertices[selected_position]
    selected_number = random_a[1][random.randrange(0, len(random_a) - 1)]
    random_b = [item for item in vertices if selected_number in item[0]][0]
    random_a[0].extend(random_b[0])
    random_a[1]=[x for x in random_a[1] if x not in random_b[0]]
    random_a[1].extend([x for x in random_b[1] if x not in random_a[0]])
    vertices[selected_position] = random_a
    vertices.remove(random_b)
    if len(vertices) > 2:
        vertices = merge_graph(vertices)
    return vertices

if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    results = []
    for i in range(0, 20):
        with open(BASE_DIR + '/data/kargerMinCut.txt') as f:
            content = f.readlines()
        content = [list(map(int, x.split())) for x in content]
        content = [[[x[0]], x[1:]] for x in content]
        result = merge_graph(content)
        if (len(result[0]) > 1):
            results.append(len(result[0][1]))
        else:
            if(len(result[0])< len(result[1])):
                results.append(len(result[0]))
            else:
                results.append(len(result[1]))
    results.sort()
    print(results)
