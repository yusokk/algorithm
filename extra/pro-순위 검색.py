import bisect

def set_tree(tree, info):
    infos = info.split()
    next_node = tree
    for i in range(3):
        if not next_node.get(infos[i], 0):
            next_node[infos[i]] = {}
        next_node = next_node[infos[i]]
    if not next_node.get(infos[3], 0):
        next_node[infos[3]] = []
    next_node[infos[3]].append(int(infos[4]))


def sort_tree(tree):
    next_nodes = tree.values()
    for _ in range(3):
        temp_nodes = []
        for node in next_nodes:
            temp_nodes += node.values()
        next_nodes = temp_nodes

    for last_node in next_nodes:
        last_node.sort()



def handle_query(tree, query):
    count = 0
    split = query.split(' and ')
    next_nodes = [tree]
    last_query = split[-1].split()
    creteria = int(last_query[1])

    for i in range(4):
        temp_nodes = []
        target = split[i]
        if i == 3:
            target = last_query[0]
        for node in next_nodes:
            if target == '-':
                temp_nodes += [node[key] for key in node.keys()]
            else:
                if not node.get(target, 0):
                    continue
                temp_nodes.append(node[target])
        next_nodes = temp_nodes

    for scores in next_nodes:
        index = bisect.bisect_left(scores, creteria)
        count += len(scores) - index

    return count


def solution(info, query):
    answer = []
    tree = {}

    for info_str in info:
        set_tree(tree, info_str)

    sort_tree(tree)

    for q in query:
        answer.append(handle_query(tree, q))

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])