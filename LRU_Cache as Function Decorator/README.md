# LRU Cache

Every time the script calls the function, instead of computing an answer from scratch, LRU_Cache will check if function call with the same parameter has been previously called.
If so it will return the correct result directly from memory. This reduces massive duplicate branches in recursion and improves performance significantly. 


An example on a simple fibonacci algorithm shows that: 
* Minimum execution time: 18.8847945999878 without cache
* Minimum execution time: 7.999915396794677e-07 with cache
* CacheInfo(hits=61, misses=35, maxsize=128, currsize=35)
