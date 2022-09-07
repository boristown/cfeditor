from cfinput import *

class Solution:
    def solve(self,a,b,c,N):
        return a,b,c,N
        
formart = 'ABC,NB'
for tp in cfinput(formart):
    sol = Solution()
    ans = sol.solve(*tp)
    sys.stdout.write(str(ans)+'\n')
    sys.stdout.flush()
    
'''
input sample:
1 2 3
4 4
3 1
'''