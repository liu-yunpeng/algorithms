# Quick Sort

Quick Sort uses partition by pivot to set elements at pivot "in place". 

A well designed quick sort runs in O(nlogn). A bad designed quick sort puts all elements into 1 sub-problem in each recursion and ends up comparing n^2 times. 

To make sure that the quick sort does not fall into that pitfall, need to either:
* make the selection of pivot random
* or use a 3 element sampling from the array (at start, at middle, and at end) and get the the median of the 3

