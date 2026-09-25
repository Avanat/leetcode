class Solution(object):
    def totalNQueens(self, n):
        import itertools

        count = 0

        for perm in itertools.permutations(range(n)):
            valid = True

            for i in range(n):
                for j in range(i + 1, n):
                    if abs(perm[i] - perm[j]) == abs(i - j):
                        valid = False
                        break

                if not valid:
                    break

            if valid:
                count += 1

        return count
