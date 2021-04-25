# Maintain Median with Heap

input.txt file gives a stream of data points. For each data update, calculate the current median of the queue. 

If using a naive method, this will take O(logn) to locate and O(n) to insert, results a O(n) time complexity overall. 

Heap data structure shouts out for such operations! Heap is used to repeatedly draw the minimum. By breaking the queue into 2 parts, we can use a min heap to digest half of all numbers above agerave, and a max heap for below average. 

Python heapq module only supports min heap. Though a common practice is to use an lambda function to flip the sign of numbers and convert a min to a max heap, I chose to design my own min heap and max heap. 

![image](https://user-images.githubusercontent.com/12473437/115999918-8c822300-a5b3-11eb-937b-bd03f39146b2.png)
