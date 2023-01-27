_local_debug_ = True

import time

def debug():
    return '_local_debug_' in globals()

def solve():
    print('Yes')

t = int(input())
for i in range(1, t + 1):
    if debug():
        start = time.time()
    solve()
    if debug():
        end = time.time()
        print('Case #{}: {} ms'.format(i, (end - start) * 1000))