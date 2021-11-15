#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> g1;

	for (int i = 1; i <= 5; i++)
		g1.push_back(i);

	cout << "vector: ";
	for (auto i = g1.begin(); i != g1.end(); ++i)
		cout << *i << " ";

	// the iterator constructor can also be used to construct from arrays:
	int myints[] = {1, 2, 3, 4, 5};
	vector<int> myvector (myints, myints + sizeof(myints) / sizeof(int) );

	// iterate a vector
	cout << "\nvector in reverse order:";
	for (auto it = myvector.rbegin(); it != myvector.rend(); ++it) {
		cout << *it << ' ';
	}

	// without using explicit pointers
	cout << "\nvector easy loop:";
	for (int n : myvector) {
		cout << n << ' ';
	}

	return 0;
}
