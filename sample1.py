from cfinput import *

class Solution:
    
    def solve(self,a,b,N):
        return a+b,N

formart = "T,AB,NB"
for tp in cfinput(formart):
    sol = Solution()
    ans = sol.solve(*tp)
    sys.stdout.write(str(ans)+'\n')
    sys.stdout.flush()

'''
input sample:
2
1 1
3 2
1 2
1 9 1
2 2 8
'''