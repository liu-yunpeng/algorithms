# -*- coding: utf-8 -*-


from timeit import repeat
from functools import lru_cache

@lru_cache()
#@lru_cache(maxsize=16)
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

setup_code = "from __main__ import Fibonacci"
stmt = "Fibonacci(35)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")

# Minimum execution time: 18.8847945999878 without cache


#print(Fibonacci.cache_info())

# Minimum execution time: 7.999915396794677e-07 with cache
# CacheInfo(hits=61, misses=35, maxsize=128, currsize=35)