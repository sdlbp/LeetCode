"""
https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/


"""
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        s = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for h, p in s:
            res.insert(p, (h, p))
        return res




if __name__ == "__main__":
    test = Solution()
    data = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    a = test.reconstructQueue(data)
    print(a)

