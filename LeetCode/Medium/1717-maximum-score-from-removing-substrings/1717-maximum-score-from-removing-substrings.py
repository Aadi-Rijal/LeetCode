class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.s = s
        op = 'ab' if x > y else 'ba'

        def solve(op):
            res = 0
            stack = []
            for i in range(len(self.s)):
                if self.s[i] == op[1] and stack and stack[-1] == op[0]:
                    stack.pop()
                    res += x if op =='ab' else y
                else:
                    stack.append(self.s[i])
            self.s = "".join(stack)
            return res
        out = solve(op)
        op = 'ab' if op == 'ba' else 'ba'
        out += solve(op)
        return out