
// assignment 56

#include <iostream>
using namespace std;

int main()
{
	// declare integer variables
	int i, start, end;

	// get 'start' integer from user
	cout << "Enter start: ";
	cin >> start;

	// get 'end' integer from user
	cout << "Enter end: ";
	cin >> end;

	// run loop
	for (i = start; i < (end+1); i++)
	{
		if (i % 2 == 0)
			cout << i << endl;
	}

	// exit function by returning 0 integer
	return 0;
}
