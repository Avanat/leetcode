class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length

            if i == len(words) or len(line) == 1:
                result.append(" ".join(line).ljust(maxWidth))
            else:
                gaps = len(line) - 1
                base = spaces // gaps
                extra = spaces % gaps

                text = ""

                for j in range(gaps):
                    text += line[j]
                    text += " " * (base + (1 if j < extra else 0))

                text += line[-1]
                result.append(text)

        return result
