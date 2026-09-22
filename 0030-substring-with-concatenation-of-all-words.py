class Solution(object):
    def findSubstring(self, s, words):
        if not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        required = {}

        for word in words:
            required[word] = required.get(word, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            valid = True

            for j in range(i, i + total_len, word_len):
                word = s[j:j + word_len]

                if word not in required:
                    valid = False
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > required[word]:
                    valid = False
                    break

            if valid and seen == required:
                result.append(i)

        return result
