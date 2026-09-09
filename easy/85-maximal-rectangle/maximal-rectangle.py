class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n = len(matrix[0])
        height = [0] * n
        res = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            stack = []
            for i in range(n + 1):
                h = 0 if i == n else height[i]
                while stack and h < height[stack[-1]]:
                    top = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, height[top] * width)
                stack.append(i)
        return res