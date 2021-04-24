# Karatsuba Algorithm
https://en.wikipedia.org/wiki/Karatsuba_algorithm

This is a very clever designed recursion algorithm to convert multiplying two numbers into solving 3 half-sized sub problems. 

It breaks each multiplier into 2 half length numbers. If naively computing all operations on the total 4 sub numbers, complexity would not be improved, still O(n^2). By computing only 3 sub operations and deriving the fourth from them, it reduces the proliferation rate in the recursion and thus gives a better runtime. 

This connects to the brilliant Strassen algorithm in the same way that Strassen’s computes only 7 sub components out of 8 and reduces complexity in a surprisingly genius way! 


![image](https://user-images.githubusercontent.com/12473437/115944648-95bca400-a47c-11eb-946c-60e2327142eb.png)
