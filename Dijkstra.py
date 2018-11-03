edges = []

nan = -1

begin_index = 0

reached_dist_dict = {}

reached_path_dict = {}


def init(node_size):
    global edges
    edges = []
    for i in range(0, node_size):
        edges.append([nan for j in range(0, node_size)])
        if i != begin_index:
            reached_dist_dict[i] = nan
            reached_path_dict[i] = []
        else:
            reached_dist_dict[i] = 0
            reached_path_dict[i] = [i]

def add_edge(begin, end, weight):
    edges[begin][end] = weight


def dijkstra():
    dijkstra_once(begin_index, 0, [begin_index])


def dijkstra_once(now_index, distance, nodes):
    index_edge_dict = {}
    for i in range(0, len(edges[now_index])):
        if edges[now_index][i] != nan:
            index_edge_dict[i] = edges[now_index][i]
    sort_index_edge_dict = {}
    keys = [key for key in index_edge_dict.keys()]
    times = len(keys)
    for i in range(0, times):
        for key in keys:
            ifMin = True
            for k in index_edge_dict.keys():
                if index_edge_dict[key] > index_edge_dict[k]:
                    ifMin = False
                    break
            if ifMin:
                sort_index_edge_dict[key] = index_edge_dict[key]
                index_edge_dict.pop(key)
                keys.remove(key)
    #print(now_index, sort_index_edge_dict)
    for key in sort_index_edge_dict.keys():
        dist = distance + sort_index_edge_dict[key]
        new_nodes = [node for node in nodes]
        new_nodes.append(key)
        closer = False
        if reached_dist_dict[key] == nan:
            closer = True
        else:
            if dist < reached_dist_dict[key]:
                closer = True
        if closer:
            reached_dist_dict[key] = dist
            reached_path_dict[key] = new_nodes
            #print(key, sort_index_edge_dict[key], dist)
            dijkstra_once(key, dist, new_nodes)


def question_2():
    global begin_index
    begin_index = 0 #起始点
    init(7) #7*7的邻接矩阵
    add_edge(0, 1, 1) #0->1的距离为1
    add_edge(1, 0, 3)
    add_edge(0, 2, 7)
    add_edge(1, 2, 3)
    add_edge(2, 1, 1)
    add_edge(1, 4, 1)
    add_edge(4, 3, 2)
    add_edge(3, 4, 1)
    add_edge(2, 3, 3)
    add_edge(2, 5, 5)
    add_edge(5, 2, 2)
    add_edge(5, 4, 3)
    add_edge(5, 6, 2)
    for line in edges:
        print(line)
    print(reached_dist_dict)
    dijkstra()
    print(reached_dist_dict)
    print(reached_path_dict)


def question_3():
    global begin_index
    for i in range(0, 6):
        begin_index = i
        init(6)
        add_edge(0, 1, 50)
        add_edge(0, 3, 40)
        add_edge(0, 4, 25)
        add_edge(0, 5, 10)
        add_edge(1, 0, 50)
        add_edge(1, 2, 15)
        add_edge(1, 3, 20)
        add_edge(1, 5, 25)
        add_edge(2, 1, 15)
        add_edge(2, 3, 10)
        add_edge(2, 4, 20)
        add_edge(3, 0, 40)
        add_edge(3, 1, 20)
        add_edge(3, 2, 10)
        add_edge(3, 4, 10)
        add_edge(3, 5, 25)
        add_edge(4, 0, 25)
        add_edge(4, 2, 20)
        add_edge(4, 3, 10)
        add_edge(4, 5, 55)
        add_edge(5, 0, 10)
        add_edge(5, 1, 25)
        add_edge(5, 3, 25)
        add_edge(5, 4, 55)
        print(i)
        for line in edges:
            print(line)
        print(reached_dist_dict)
        dijkstra()
        print(reached_dist_dict)
        print(reached_path_dict)

    
if __name__ == '__main__':
    question_2()
    #question_3()
    
