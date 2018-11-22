class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        return self.v_1(ops)

    def v_1(self, ops):
        """
        72ms 3.71%
        没有更好的解决方式,排名低估计是bug
        :param ops:
        :return:
        """
        num = []
        for o in ops:
            if o == "+":
                if len(num) > 1:
                    num.append(num[-1] + num[-2])
                elif len(num) > 0:
                    num.append([num[-1]])
            elif o == "D":
                if len(num) > 0:
                    num.append(num[-1] * 2)
            elif o == "C":
                if len(num) > 0:
                    num.pop()
            else:
                num.append(int(o))
        return sum(num)


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["+","5","2","C","D","+"]))