from cfinput import *

class Solution:
    def solve(self,a,b,c,N):
        return a,b,c,N
        
formart = 'ABC,NB'
for tp in cfinput(formart):
    sol = Solution()
    ans = sol.solve(*tp)
    print(ans)
    
'''
input sample:
1 2 3
4 4
3 1
'''