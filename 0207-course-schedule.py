class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False

            if visited[node] == 2:
                return True

            visited[node] = 1

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
