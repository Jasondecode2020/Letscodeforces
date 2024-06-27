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
  n = I()
  d = defaultdict(set)
  for i in range(n):
    a, x = LI()
    if a == 1:
      d[1].add(x)
    elif a == 2:
      d[2].add(x)
    else:
      d[3].add(x)
  mn, mx = max(d[1]), min(d[2])
  res = mx - mn + 1
  for num in d[3]:
    if mn <= num <= mx:
      res -= 1
  arr.append(str(max(0, res)))
print('\n'.join(arr))