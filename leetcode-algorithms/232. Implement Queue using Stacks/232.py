class MyQueue:
    """
    重点在于_move方法,把先进入栈中元素,依次移入另一个栈中,从而达到先进先出的效果
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._move()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self._move()
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.in_stack) and (not self.out_stack)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()