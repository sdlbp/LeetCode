"""
min-stack
v1 和 v2 的区别仅仅是v2在push过程中求出了min
"""

class MinStack_v2:
    """
    56ms
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if len(self._stack) == 0:
            cur_min = x
        elif self.getMin() > x:
            cur_min = x
        self._stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[-1][1]


class MinStack:
    """
    1240
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self._stack)
