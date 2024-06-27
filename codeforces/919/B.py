standard_input, packages = 1, 1

if 1:
  if standard_input:
    import io, os, sys
    input = lambda: sys.stdin.readline().strip()

    import math
    inf = math.inf

    def S(): # string
      return input()
    
    def I(): # int
      return int(input())

    def II(): # iterate int from a list
      return map(int, input().split())

    def LS(): # list of string
      return list(input().split())

    def LI(): # list of int
      return list(map(int, input().split()))

    def LF(): # list of float
      return list(map(float, input().split()))

    def M10(): # iterate of 1 to 0
      return map(lambda x: int(x) - 1, input().split())

    def L10(): # list of 1 to 0
      return list(map(lambda x: int(x) - 1, input().split()))

  if packages:
    import random
    import bisect
    import typing
    from collections import Counter, defaultdict, deque
    from copy import deepcopy
    from functools import cmp_to_key, lru_cache, reduce
    from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
    from itertools import accumulate, combinations, permutations, count, product
    from operator import add, iand, ior, itemgetter, mul, xor
    from string import ascii_lowercase, ascii_uppercase, ascii_letters

q = I()
arr = []
for _ in range(q):
  n, k, x = LI()
  a = LI()
  a.sort(reverse = True)
  a += [0] * k
  pre = list(accumulate(a, initial = 0))
  ans, res, nn = 0, 2 * pre[x], -1 # used k instead of x, made mistakes in test2
  for i in range(k):
    ans += a[i]
    temp = ans + 2 * (pre[i + x + 1] - pre[i + 1])
    if temp < res:
      res = temp
      nn = i 
  final_res = -(pre[nn + 1 + x] - pre[nn + 1]) + pre[-1] - pre[nn + 1 + x]
  arr.append(str(final_res))
print('\n'.join(arr))
