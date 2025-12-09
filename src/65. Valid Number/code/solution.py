class Solution:
    def isNumber(self, s: str) -> bool:
        isdot, ise, nums = False, False, False
        for i, c in enumerate(s):
            if c.isdigit():
                nums = True
            elif c in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif c in "eE":
                if ise or not nums:
                    return False
                ise, nums = True, False
            elif c == ".":
                if isdot or ise:
                    return False
                isdot = True
            else:
                return False
        return nums