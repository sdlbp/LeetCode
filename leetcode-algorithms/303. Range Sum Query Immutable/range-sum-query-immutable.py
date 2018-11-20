class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.result = [0]
        for i in range(len(nums)):
            self.result.append(self.result[i] + nums[i])
        print(self.result)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.result[j + 1] - self.result[i]


if __name__ == "__main__":
    test = NumArray([1, 2, 3, 4])
    print(test.sumRange(2, 3))
