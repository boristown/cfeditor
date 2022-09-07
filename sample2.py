from cfinput import *

class Solution:
    def solve(self,a,M):
        return a,M
        
formart = 'T,A,MA'
for tp in cfinput(formart):
    sol = Solution()
    ans = sol.solve(*tp)
    sys.stdout.write(str(ans)+'\n')
    sys.stdout.flush()
    
'''
input sample:
3
2
qweqwe
adsfsaf
1
qweqweqwe
3
q
aa
sss
'''