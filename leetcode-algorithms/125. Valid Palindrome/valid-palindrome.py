"""
valid-palindrome
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.s_2(s)

    def s_2(self, s):
        s = [a.lower() for a in s if a.isalnum()]
        return "".join(s) == "".join(s[::-1])

    def two_points(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
