class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        colset=set() #to store used columns
        lud=set() #to store left upper diagonal 
        rud=set() #to store right upper diagonal 
        def backtrack(row):
            nonlocal res 
            if row==n:
                res+=1
                return
            for col in range(n):
                if col in colset or row-col in lud or row+col in rud:
                    continue
                
                colset.add(col)
                lud.add(row-col)
                rud.add(row+col)

                backtrack(row+1)
                
                colset.remove(col)
                lud.remove(row-col)
                rud.remove(row+col)
        backtrack(0)
        return res