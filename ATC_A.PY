_local_debug_ = True

import time

import sys

input = sys.stdin.readline

is_debug = '_local_debug_' in globals()

#int input
def inp():
    return(int(input()))

#list input
def inlt():
    return(list(map(int,input().split())))

#string input
def insr():
    s = input()
    return(list(s[:len(s) - 1]))

#variables input
def invr():
    return(map(int,input().split()))

#matrix input
def inmt(n):
    return [inlt() for _ in range(n)]

def solve():
    print('Yes')

if is_debug: start = time.time()
solve()
if is_debug:
    end = time.time()
    print('Time: {} ms'.format((end - start) * 1000))