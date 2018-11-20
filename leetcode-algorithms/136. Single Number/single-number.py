class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.v_3(nums)

    def v_3(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def v_2(self, nums):
        """
        28ms
        :param nums:
        :return:
        """
        f_set = set()
        for n in nums:
            if n not in f_set:
                f_set.add(n)
            else:
                f_set.remove(n)
        return f_set.pop()

    def v_1(self, nums):
        """
        56ms
        :param nums:
        :return:
        """
        f_dic = {}
        for n in nums:
            if str(n) not in f_dic:
                f_dic[str(n)] = n
            else:
                f_dic.pop(str(n))
        return list(f_dic.values())[0]


if __name__ == "__main__":
    t = Solution()
    ans = t.singleNumber([2,3,2,3,1,4,4,5,6,5,6])
    print(ans)
