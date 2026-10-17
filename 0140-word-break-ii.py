class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for suffix in backtrack(end):
                        result.append(word + (" " + suffix if suffix else ""))

            memo[start] = result
            return result

        return backtrack(0)
