from cfinput import *

class Solution:
    def solve(self,a,b,N):
        return a+b,N
        
for tp in cfinput('T,AB,NB'):
    sol = Solution()
    ans = sol.solve(*tp)
    print(ans)
