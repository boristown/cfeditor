# A - YES or YES?
# https://codeforces.com/contest/1703/problem/A

from bisect import *
from collections import *
from itertools import *
YES = 'YES'
Yes = 'Yes'
NO = 'NO'
No = 'No'

def cfinput(formats):
    ans = _cfinput(formats)
    if formats[0] == 'T':
        return ans
    else:
        return [ans]

def _cfinput(formats):
    '''
    cf input data smart loader
    formart definition.
    Number of samples: T
    Single variable：ABCDEFGHIJK
    Horizontal list: L
    numeric matrix: NX (X indicates the number of rows)
    Vertical list: VX (X indicates the number of rows)
    String: S
    String matrix: MX (X indicates the number of rows)
    Separator: Comma(,)
    '''
    def get_lines(vn):
        if vn in vmap:
            return vmap[vn]
        else:
            return int(vn)
    if formats[0] == 'T': #Number of samples: T
        test = int(input())
        ans = []
        for _ in range(test):
            ans.append(_cfinput(formats[2:]))
        return ans
    else:
        ans = []
        vmap = {}
        fs = formats.split(',')
        for line in fs:
            if line[0] in 'ABCDEFGHIJK': #Single variable：ABCDEFGHIJK
                vars = list(map(int, input().split()))
                for i,v in enumerate(vars):
                    vmap[line[i]]=v
                ans.extend(vars)
            elif line[0] == 'L': #Horizontal list: L
                L = list(map(int, input().split()))
                ans.append(L)
            elif line[0] == 'S': #String: S
                S = input()
                ans.append(S)
            elif line[0] == 'N': #numeric matrix: NX (X indicates the number of rows)
                N = []
                for _ in range(get_lines(line[1])):
                    L = list(map(int, input().split()))
                    N.append(L)
                ans.append(N)
            elif line[0] == 'M': #String matrix: MX (X indicates the number of rows)
                M = []
                for _ in range(get_lines(line[1])):
                    M.append(input())
                ans.append(M)
            elif line[0] == 'V': #Vertical list: VX (X indicates the number of rows)
                V = []
                for _ in range(get_lines(line[1])):
                    V.append(int(input()))
                ans.append(V)
        return ans

class Solution:
    def solve(self,s):
        if s.upper() == YES:
            return YES
        return NO

formart = "T,S"
for tp in cfinput(formart):
    sol = Solution()
    ans = sol.solve(*tp)
    print(ans)