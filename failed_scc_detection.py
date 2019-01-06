import random
import os, sys
import pandas as pd
import numpy as np
global graph
global reversed_graph
global current_time
global S

def dfs(v):
    global current_time
    node_list =  reversed_graph.at[v, 'v']
    reversed_graph.set_value(v,'explored', True)
    for node in node_list:
        # print(reversed_graph.at[node, 'explored'])
        if node in reversed_graph.index and not reversed_graph.at[node, 'explored']:
            dfs(node)
        else:
            continue
    current_time += 1
    if v in graph.index:
        graph.set_value(v, 'time', current_time)

def second_dfs(v):
    global S
    graph.set_value(v,'leader', S)
    node_list = graph.at[v, 'u']
    for node in node_list:
        if node in graph.index and not graph.at[node, 'explored']:
            dfs(node)
        else:
            continue

if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    data = pd.read_csv(BASE_DIR + '/data/SCC.txt', sep=" ", header=None, index_col=False).dropna(axis=1)
    data.columns = ["v", "u"]
    graph = data.groupby('v')['u'].apply(list).to_frame()
    reversed_graph = data.groupby('u')['v'].apply(list).to_frame()
    reversed_graph.insert(1, 'explored', False)
    graph.insert(1, 'explored', False)
    graph.insert(2, 'time', 0)
    graph.insert(3, 'leader', None)
    current_time = 0
    all_reversed_nodes = reversed_graph.index.values
    all_reversed_nodes[:]= all_reversed_nodes[::-1]
    for node in all_reversed_nodes:
        if not reversed_graph.at[node, 'explored']:
            dfs(node)
    print(reversed_graph.loc[reversed_graph['explored']==True].head(10))
    print(graph.loc[graph['time']>0].head(10))
    all_times =  np.sort(graph['time'].values, axis=None)
    all_times[:] = all_times[::-1]
    for time in all_times:
        node = graph.loc[graph['time'] == time].iloc[0]
        if not node['explored']:
            S = node.index.astype(int)[0]
            second_dfs(node.index.astype(int)[0])
    final_sccs = graph.groupby('leader').size().reset_index(name='counts')
    print(final_sccs)