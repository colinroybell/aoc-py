from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_25(DayBase):
    YEAR = "2023"
    DAY = "25"

class Node:
    def __init__(self, id):
        self.id = id
        self.links = []
        self.used = []

def connected(nodes, start_id):
    found = set()
    queue = [start_id]
    while queue:
        id = queue.pop()
        if id in found:
            continue
        else:
            found.add(id)
        for link in nodes[id].links:
            #print(link)
            if link not in nodes[id].used:
                #print('adding',id,link)
                queue.append(link)
    print(len(found))
    if len(found) == 1490:
        return True

def flow(nodes, start_id, end_id, used_pairs):
    print('flow',used_pairs)
    count = 0
    for id in nodes:
        nodes[id].used = []
    for pair in used_pairs:
        #print(pair)
        nodes[pair[0]].used.append(pair[1])
        nodes[pair[1]].used.append(pair[0])
    ret_pairs = []
    while connected(nodes, start_id):
        count += 1
        queue = [(start_id, [start_id])]
        done = False
        while queue and not done:
            (id,path) = queue.pop()
            if id == end_id:
                #print('solve',count,id,path)
                for i in range(len(path)-1):
                    id0 = path[i]
                    id1 = path[i+1]
                    nodes[id0].used.append(id1)
                    nodes[id1].used.append(id0)
                    ret_pairs.append((id0,id1))
                    #print("removing",id0,id1)
                done = True
            else:
                for link in nodes[id].links:
                    if link not in nodes[id].used and link not in path:
                        new_path = path.copy()
                        new_path.append(link)
                        queue.append((link, new_path))
    print(used_pairs, count, ret_pairs)
    return (count,ret_pairs)


import networkx as nx
from math import prod

# Uses library. Karger's algorithm (on Wikipedia) what we need. What I have ought to work but has a bug in the max_flow?


def part_a(input):
    nodes = {}
    wires = []

    G  = nx.Graph()
    for line in input_generator(input):
        (id, wire_strings) = line.split(': ')
        if id not in nodes:
            nodes[id] = Node(id)
        wires_s = wire_strings.split(' ')
        for wire in wires_s:
            if wire not in nodes:
                nodes[wire] = Node(wire)
            #if id == 'pzl' and wire =='hfx':
            #    continue
            #if id == 'cmg' and wire == 'bvb':
            #    continue
            #if id == 'jgt' and wire == 'nvd':
           #     continue
            nodes[id].links.append(wire)
            nodes[wire].links.append(id)
            wires.append((id,wire))
            G.add_edge(id,wire)

    for node in nodes:
        for link in nodes[id].links:
            print(node,link)
            # interesting to know why this variant fails.
            #G.add_edge(node,link)
    print(nx.minimum_edge_cut(G))
    G.remove_edges_from(nx.minimum_edge_cut(G))
    for c in nx.connected_components(G):
        print(c)
    return prod(len(c) for c in nx.connected_components(G))

    # cmg, bvb for test
    start_id = 'fqt'
    end_id = 'pbl'
    used_pairs = []
    while 1:
        (count,ret_pairs) = flow(nodes,start_id,end_id,used_pairs)
        if count == 0:
            break
        found = True
        for trial_pair in ret_pairs:
            trial_used_pairs = used_pairs.copy()
            trial_used_pairs.append(trial_pair)
            (new_flow,_) = flow(nodes,start_id,end_id,trial_used_pairs)
            print(used_pairs,trial_pair,new_flow)
            if new_flow < count:
                used_pairs.append(trial_pair)
                break
        assert found
        print('new',used_pairs)

    for id in nodes:
        nodes[id].used = []
    for pair in used_pairs:
        nodes[pair[0]].used.append(pair[1])
        nodes[pair[1]].used.append(pair[0])

    found = set()
    queue = [start_id]
    while queue:
        id = queue.pop()
        if id in found:
            continue
        else:
            found.add(id)
        for link in nodes[id].links:
            print(link)
            if link not in nodes[id].used:
                print('adding',id,link)
                queue.append(link)

    max_len = len(found)
    print(used_pairs,max_len)
    return max_len * (1490 - max_len)






    assert 0, "not implemented"


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2023_25().run_cmdline()
