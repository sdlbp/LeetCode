"""
unique-email-addresses
"""
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        return self.v_2(emails)

    def v_2(self, emails):
        ans = list(set([item.split('@')[1] for item in emails]))
        return len(ans)

    def v_1(self, emails):
        e_set = set()
        for email in emails:
            a, _, c = email.partition("@")
            if "+" in a:
                a = a[:a.index("+")]
            e_set.add(a.replace('.', '') + '@' + c)
        return len(e_set)


if __name__ == "__main__":
    t = Solution()
    a = t.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com","teste1mail+david@lee.tcode.com"])
    print(a)