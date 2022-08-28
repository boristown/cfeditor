from cfinput import *

class Solution:
    def solve(self,a,b,N):
        return a+b,N

formart = "'T,AB,NB'"
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
2
1 1
3 2
1 2
1 9 1
2 2 8
'''