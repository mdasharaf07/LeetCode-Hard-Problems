class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        nums = list(range(1, n + 1))
        fact = factorial(n) // n
        k -= 1
        res = []
        while nums:
            res.append(str(nums[k // fact]))
            nums.pop(k // fact)
            if not nums:
                break
            k %= fact
            fact //= len(nums)
        return "".join(res)