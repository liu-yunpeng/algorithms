# Quick Sort

Quick Sort uses partition by pivot to set elements at pivot "in place". 

A well designed quick sort runs in O(nlogn). A bad designed quick sort puts all elements into 1 sub-problem in each recursion and ends up comparing n^2 times. 

To make sure that the quick sort does not get into that pitfall, need to either:
* make the selection of pivot random
* or use a 3 element sampling from the array (at start, at middle, and at end) and get the the median of the 3

Because of the "in place" property, quick sort has better space complexity than merge sort. 
However, if processing a linked-list, merge sort can perform better than quick sort. https://stackoverflow.com/questions/29218440/when-merge-sort-is-preferred-over-quick-sort







![image](https://user-images.githubusercontent.com/12473437/115944719-fd72ef00-a47c-11eb-9f79-53a7a5c0abb7.png)
