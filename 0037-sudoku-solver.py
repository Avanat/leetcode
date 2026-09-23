class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    box = (i // 3) * 3 + (j // 3)
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)

        def solve():
            if not empty:
                return True

            best = -1
            best_options = None

            for k in range(len(empty)):
                i, j = empty[k]
                box = (i // 3) * 3 + (j // 3)

                options = set("123456789") - rows[i] - cols[j] - boxes[box]

                if not options:
                    return False

                if best_options is None or len(options) < len(best_options):
                    best = k
                    best_options = options

                    if len(options) == 1:
                        break

            i, j = empty.pop(best)
            box = (i // 3) * 3 + (j // 3)

            for num in best_options:
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

                if solve():
                    return True

                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box].remove(num)

            empty.insert(best, (i, j))
            return False

        solve()
