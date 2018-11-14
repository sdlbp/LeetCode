"""
https://leetcode-cn.com/problems/unique-morse-code-words/description/
"""
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        w_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s_set = set()
        for word in words:
            ss = ""
            for s in word:
                m = w_map[ord(s) - ord("a")]
                ss = ss + m
            s_set.add(ss)
        return len(s_set)


if __name__ == "__main__":
    t = Solution()
    ans = t.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(ans)
