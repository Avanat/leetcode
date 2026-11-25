class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        for ch in s + '+':
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == ' ':
                continue

            else:
                if op == '+':
                    stack.append(num)

                elif op == '-':
                    stack.append(-num)

                elif op == '*':
                    stack[-1] *= num

                elif op == '/':
                    prev = stack[-1]
                    stack[-1] = abs(prev) // num * (1 if prev >= 0 else -1)

                num = 0
                op = ch

        return sum(stack)
