from collections import defaultdict, deque

class Tree(object):
    def __init__(self, root):
        self.root = root

    @property
    def longest_chain(self):
        """Compute chain with the longest length"""

        stack = deque()
        stack.appendleft([self.root, 1])

        max_depth = 0
        while stack:
            node, depth = stack.popleft()
            for child in node.children:
                stack.appendleft([child, depth+1])

            max_depth = max(depth, max_depth)

        return max_depth

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

    def __repr__(self):
        s = 'id:{}'.format(str(self.id))
        if self.children:
            s += '->{}'.format(self.children)

        return s


if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(raw_input()) for _ in range(n)]

    # Compute children in reverse order. i.e. if A is a supervisor of B is
    # represented as A -> B.
    children, root_ids = defaultdict(list), []
    for id, num in enumerate(nums):
        if num == -1:
            root_ids.append(id)
            continue
        children[num-1].append(id) # zero-indexing

    nodes = {id: Node(id) for id in range(n)}
    for id, child_ids in children.items():
        nodes[id].children = [nodes[child_id] for child_id in child_ids]

    roots = [nodes[root_id] for root_id in root_ids]
    trees = [Tree(root) for root in roots]

    longest_chain = 0
    for tree in trees:
        longest_chain = max(tree.longest_chain, longest_chain)

    print longest_chain
