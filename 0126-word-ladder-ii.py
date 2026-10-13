from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            words -= level
            next_level = set()

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in words:
                            next_level.add(new_word)
                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        result = []

        def backtrack(word, path):
            if word == beginWord:
                result.append([beginWord] + path[::-1])
                return

            for parent in parents[word]:
                backtrack(parent, path + [word])

        backtrack(endWord, [])
        return result
