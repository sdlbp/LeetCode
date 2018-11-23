"""
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""
class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        return self.v_2(T)

    def v_2(self, T):
        stack = []  # [i,....]
        ans = [0] * len(T)
        for i in range(len(T)):
            while len(stack) and T[stack[-1]] < T[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

    def v_1(self, T):
        stack = []  # [[i, v],....]
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while len(stack) and stack[-1][1] < t:
                j = stack.pop()[0]
                ans[j] = i - j
            stack.append([i, t])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
