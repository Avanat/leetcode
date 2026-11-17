class Solution(object):
    def findWords(self, board, words):
        trie = {}

        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node:
                return

            node = node[char]
            word = node.pop('$', None)

            if word:
                result.append(word)

            board[r][c] = '#'

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result
