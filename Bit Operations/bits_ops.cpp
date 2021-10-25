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

typedef long long ll;

int main(int argc, char const *argv[])
{
	int base = 2;
	// left shift doubles the int, right shift halves it
	for (int i = 0; i < 10; ++i)
	{
		base = base << 1;
		cout << (base) << endl;
	}

	int a, b;
	a = 2;
	b = 7;

	cout << (a & b) << endl;
	cout << (a | b) << endl;
	cout << (a ^ b) << endl;
	cout << (~ b) << endl;



	return 0;
}