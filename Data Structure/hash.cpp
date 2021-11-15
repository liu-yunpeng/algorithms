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
#include <unordered_map>
using namespace std;

typedef long long ll;

int main(int argc, char const *argv[])
{
	unordered_map<std::string, std::string> a_map;

	a_map["h"] = "e";
	a_map["l"] = "l";
	a_map["o"] = "w";

	for (auto i : a_map)
	{
		cout << i.first << i.second << endl;
	}

	if (a_map.find("h") != a_map.end())
	{
		cout << "found h in map! " << endl;
	}

	return 0;
}