
class Solution(object):
   def letterCombinations(self, digits):
       """
       :type digits: str
       :rtype: List[str]
       """
       if not digits:
           return []
       hash={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
       res=[]
       comb=[]
       def try_comb(i):
           if i == len(digits):
               res.append("".join(comb))
               return
           pos_letters = hash[digits[i]]
           for letter in pos_letters:
               comb.append(letter)
               try_comb(i+1)
               comb.pop()
       try_comb(0)
       return res