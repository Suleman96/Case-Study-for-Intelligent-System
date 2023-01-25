import numpy
import math



def a(n, memo={}):
    global x
    if n in [0, 1, 2, 3]:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = a(n-1, memo) + a(n-2, memo) + a(n-3, memo) + a(n-4, memo)
        x = memo[n]
        return memo[n]
        print(x)

a(4)
