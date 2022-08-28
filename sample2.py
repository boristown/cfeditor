from cfinput import *

class Solution:
    def solve(self,a,M):
        return a,M
        
formart = 'T,A,MA'
if formart[0] == 'T':
    for tp in cfinput(formart):
        sol = Solution()
        ans = sol.solve(*tp)
        print(ans)
else:
    tp = cfinput(formart)
    sol = Solution()
    ans = sol.solve(*tp)
    print(ans)
    
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