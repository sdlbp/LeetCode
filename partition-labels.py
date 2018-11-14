"""
https://leetcode-cn.com/problems/partition-labels/description/

解: 每个序列最后一个字母是当前序列最大数字
"""

class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


if __name__ == "__main__":
    test = Solution()
    data = "ababcbacadefegdehijhklij"
    a = test.partitionLabels(data)
    print(a)
