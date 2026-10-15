
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        from collections import deque

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]
