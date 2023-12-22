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
        self.weight = {}

    def __repr__(self):
        return 'N+'+self.id

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
            if nodes[id].weight[link] < 1:
            #if link not in nodes[id].used:
                #print('adding',id,link)
                queue.append(link)
    print('connected',len(found))
    if len(found) == len(nodes):
        return True

def connected_count(nodes, start_id):
    found = set()
    queue = [start_id]
    while queue:

        id = queue.pop()
        print(id,nodes.keys())
        if id in found:
            continue
        else:
            found.add(id)
        for link in nodes[id].links:
            #print(link)
            #if nodes[id].weight[link] < 1:
            if link not in nodes[id].used:
                #print('adding',id,link)
                queue.append(link)
    return len(found)


def flow(nodes, start_id, end_id, used_pairs):
    print('flow',used_pairs)
    count = 0
    for id in nodes:
        for link in nodes[id].links:
            nodes[id].weight[link] = 0
    for pair in used_pairs:
        #print(pair)
        nodes[pair[0]].weight[pair[1]] = 1
        nodes[pair[1]].weight[pair[0]] = 1
    ret_pairs = []
    while connected(nodes, start_id):
        count += 1
        print("count",count)
        queue = [(start_id, [start_id])]
        done = False
        path_count = 0
        while queue and not done:
            (id,path) = queue.pop()
            if id == end_id:
                print('solve',count,id,path_count)
                for i in range(len(path)-1):
                    id0 = path[i]
                    id1 = path[i+1]
                    nodes[id0].weight[id1] += 1
                    nodes[id1].weight[id0] -= 1
                    ret_pairs.append((id0,id1))
                    #print("removing",id0,id1)
                done = True
            else:
                path_count +=1
                if len(path) < 10:
                    print(path_count, path, len(queue))
                if path_count % 1000 == 0:
                    print(path_count, len(queue))
                for link in nodes[id].links:
                    if nodes[id].weight[link] < 1 and link not in path:
                        new_path = path.copy()
                        new_path.append(link)
                        queue.append((link, new_path))
    #print(used_pairs, count, ret_pairs)
    return (count,ret_pairs)


import networkx as nx
from math import prod
from random import random

# Uses library. Karger's algorithm (on Wikipedia) what we need. What I have ought to work but has a bug in the max_flow?



def get_crossings(nodes, score):
    crossings = []
    for n in nodes.values():
        for l in n.links:
            if score[n.id] * score[l] < 0:
                crossings.append((n.id,l))
    return crossings

def weighted_average(nodes):
    score = {}
    new_score = {}
    for n in nodes.values():
        score[n.id] = random()*2 -1
        new_score[n] = None

    round = 0
    while 1:

        maximum = max(score.values())
        minimum = min(score.values())

        for n in nodes.values():
            score[n.id] = -1 + 2*(score[n.id]-minimum)/(maximum - minimum)


        crossings = get_crossings(nodes, score)
        count = len(crossings)
        print('Round', round,count)
        print(score)

        assert count >= 6
        if count == 6:
            break



        for n in nodes.values():
            new_score[n.id] = sum(score[l] for l in n.links)/len(n.links)

        for n in nodes.values():
            score[n.id] = new_score[n.id]
        round += 1
    for (a,b) in crossings:
        nodes[a].used.append(b)

    count = len([n for n in nodes.values() if score[n.id]>0])
    #count = connected_count(nodes, list(nodes.values())[0].id)
    return count * (len(nodes) - count)

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

    res = weighted_average(nodes)
    return res

    node_count = len(nodes)

    for node in nodes:
        for link in nodes[id].links:
            pass
            #print(node,link)
            # interesting to know why this variant fails.
            #G.add_edge(node,link)
    if 0:
        print(nx.minimum_edge_cut(G))
        G.remove_edges_from(nx.minimum_edge_cut(G))
        for c in nx.connected_components(G):
            print(c)
        return prod(len(c) for c in nx.connected_components(G))

    # cmg, bvb for test
    # fqt, pbl for main
    #start_id = 'cmg'
    #end_id = 'bvb'
    start_id, end_id = 'fqt', 'pbl'
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
            print('trial result',used_pairs,trial_pair,new_flow)
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
    return max_len * (node_count - max_len)






    assert 0, "not implemented"


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2023_25().run_cmdline()
