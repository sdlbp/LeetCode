class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        参考discuss
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []

        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2,5,7,9,33,22,10]))
