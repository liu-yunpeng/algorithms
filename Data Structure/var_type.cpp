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

#include <type_traits>
#include <typeinfo>
#ifndef _MSC_VER
#   include <cxxabi.h>
#endif
#include <memory>
#include <string>
#include <cstdlib>

template <class T>
std::string
type_name()
{
	typedef typename std::remove_reference<T>::type TR;
	std::unique_ptr<char, void(*)(void*)> own
	(
#ifndef _MSC_VER
	    abi::__cxa_demangle(typeid(TR).name(), nullptr,
	                        nullptr, nullptr),
#else
	    nullptr,
#endif
	    std::free
	);
	std::string r = own != nullptr ? own.get() : typeid(TR).name();
	if (std::is_const<TR>::value)
		r += " const";
	if (std::is_volatile<TR>::value)
		r += " volatile";
	if (std::is_lvalue_reference<T>::value)
		r += "&";
	else if (std::is_rvalue_reference<T>::value)
		r += "&&";
	return r;
}

int main(int argc, char const *argv[])
{
	unordered_map<std::string, std::string> a_map;

	a_map["h"] = "e";
	a_map["l"] = "l";
	a_map["o"] = "w";

	for (auto i : a_map)
	{
		cout << i.first << i.second << endl;
		// cout << typeid(i).name() << endl;
		cout << type_name<decltype(i)>() << endl;
	}

	return 0;
}