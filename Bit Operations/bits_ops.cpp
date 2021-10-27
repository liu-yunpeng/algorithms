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

int highestPowerof2(int n) {
	/* n should be a positive integar */
	int i = 1;
	while ((i << 1) <= n) {
		i = i << 1;
	}

	return i;
}


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


	cout << "highestPowerof2(10) " << highestPowerof2(10) << endl;
	cout << "highestPowerof2(16) " << highestPowerof2(16) << endl;
	cout << "highestPowerof2(25) " << highestPowerof2(25) << endl;
	cout << "highestPowerof2(125) " << highestPowerof2(125) << endl;



	return 0;
}


