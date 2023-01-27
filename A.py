_local_debug_ = True

import time

is_debug = '_local_debug_' in globals()

def solve():
    print('Yes')

t = int(input())
for i in range(1, t + 1):
    if is_debug: start = time.time()
    solve()
    if is_debug:
        end = time.time()
        print('Case #{}: {} ms'.format(i, (end - start) * 1000))