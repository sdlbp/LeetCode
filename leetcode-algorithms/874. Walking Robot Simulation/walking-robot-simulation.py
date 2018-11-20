class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        """
        v2
        """

        x, y = 0, 0
        arrow = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles_set = set(map(tuple, obstacles))
        max_length = 0
        for command in commands:
            if command == -1:
                arrow += 1
            elif command == -2:
                arrow -= 1
            else:
                arrow %= 4

            for k in range(command):
                if (x + dx[arrow], y + dy[arrow]) not in obstacles_set:
                    x += dx[arrow]
                    y += dy[arrow]
                    max_length = max(max_length, x*x + y*y)
        return max_length

