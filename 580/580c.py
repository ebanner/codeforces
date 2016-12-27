from collections import defaultdict, deque
from itertools import count

class Node:
    def __init__(self, id, cat):
        self.id = id
        self.cat = cat
        self.children = []
        self.explored = False
        self.i = 0

    def __iter__(self):
        return self

    def __repr__(self):
        # return str((self.id, self.cat, [child.id for child in self.children]))
        return 'ID:{}'.format(self.id)

    @property
    def nb_child(self):
        return len(self.children)

    def next(self):
        try:
            child = self.children[self.i]
            self.i += 1
        except IndexError:
            raise StopIteration
        else:
            return child

def do_dfs(root, m):
    """Do an iterative version of dfs()

    Parameters
    ----------
    root : root node of the dfs
    m : maximum number of cats

    """
    E1, E2 = 'E1', 'E2'

    S = deque()
    S.appendleft([[root, False, 0, 0], E1])
    while S:
        # print S
        data, entry_point = S.popleft()

        if entry_point == E1:
            node, active, longest_chain, incoming_chain = data # unpack arguments

            current_chain = incoming_chain+1 if node.cat else 0
            new_longest = max(current_chain, longest_chain)
            if not node.children: # base case
                RETVAL = new_longest <= m
            else: # recursive case
                nb_legal = i = 0
                child = node.children[i]
                S.appendleft([[node, active, longest_chain, incoming_chain, current_chain, new_longest, nb_legal, i], E2])
                S.appendleft([(child, node.cat, new_longest, current_chain), E1])
        elif entry_point == E2:
            node, active, longest_chain, incoming_chain, current_chain, new_longest, nb_legal, i = data

            nb_path = RETVAL
            nb_legal += nb_path
            i += 1
            if i == node.nb_child: # end of while loop
                RETVAL = nb_legal
            else: # continuation of while loop
                child = node.children[i]
                S.appendleft([[node, active, longest_chain, incoming_chain, current_chain, new_longest, nb_legal, i], E2])
                S.appendleft([(child, node.cat, new_longest, current_chain), E1])

    return RETVAL

def dfs(node, active, longest_chain, incoming_chain):
    """Perform a modified dfs on node

    Parameters
    ----------
    node : the node in question
    active : True if the parent of `node` has a cat
    longest_chain : longest chain of cats among parents of `node`
    incoming_chain : length of incoming chain of cats (0 if parent of `node`
    does not have a cat)

    """
# E1
    # debug_str = 'dfs(node={}, active={}, longest_chain={}, incoming_chain={}'
    # print debug_str.format(node.id, active, longest_chain, incoming_chain)

    current_chain = incoming_chain+1 if node.cat else 0
    new_longest = max(current_chain, longest_chain)
    if not node.children:
        return new_longest <= m
    else:
        nb_legal = 0
        i = 0
        while i < node.nb_child:
            child = node.children[i]
            nb_path = dfs(node=child, active=node.cat, longest_chain=new_longest, incoming_chain=current_chain)
# E2
            nb_legal += nb_path
            i += 1

        return nb_legal

if __name__ == '__main__':
    n, m = [int(num) for num in raw_input().split()]
    C = [int(num) for num in raw_input().split()]
    E = [[int(num) for num in raw_input().split()] for _ in range(n-1)]

    v_ids = set(v for v1, v2 in E for v in [v1, v2])
    V = {v_id: Node(v_id, bool(c)) for v_id, c in zip(sorted(v_ids), C)}

    G = defaultdict(list)
    for v1, v2 in E:
        G[v1].append(v2)
        G[v2].append(v1)

    T = defaultdict(list)
    Q = deque()
    Q.appendleft(1)
    F = {1: True} # "frontier" dict mirroring Q

    C = dict(zip(count(start=1), C))
    while Q:
        node_id = Q.popleft()
        del F[node_id]
        V[node_id].explored = True

        for neighbor in G[node_id]:
            if not V[neighbor].explored and neighbor not in F:
                V[node_id].children.append(V[neighbor]) # update children
                Q.appendleft(neighbor) # add to frontier
                F[neighbor] = True

    # print dfs(node=V[1], active=False, longest_chain=0, incoming_chain=0)
    print do_dfs(root=V[1], m=m)
