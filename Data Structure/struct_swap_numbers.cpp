#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>
using namespace std;

// Swap two numbers without using pointer or reference
// use a struct

void swap_funky(int x, int y)
{
    int temp = x;
    x = y;
    y = temp;
}
  
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}


struct twoNumbers {
  int first;
  int second;
};

struct twoNumbers swapNumbers(struct twoNumbers src)
{
  int tmp = src.first;
  src.first = src.second;
  src.second = tmp;
  return src;
}

int main() {
    
    int x, y;
    x = 3;
    y  =8;
    int* x_ptr = &x;
    int* y_ptr = &y;
    swap(x_ptr, y_ptr);

    cout << x <<" "<< y << endl;
    

    struct twoNumbers s = { 5, 42 };

    s = swapNumbers(s);

    cout << s.first <<" " << s.second << endl;
    
    return 0;
}
