
// assignment 58

#include <iostream>
using namespace std;

int main()
{
	// declare integer variables
	int num, i, n, m, spaceCount;

	// declare character variable
	char symbol;

	// get 'num' integer from user
	cout << "Enter an integer: ";
	cin >> num;

	// get 'symbol' character from user
	cout << "Enter a symbol other than space: ";
	cin >> symbol;

	// run loop - each iteration prints one line
	for (i = 0; i < num; i++)
	{
		// initiate variables for this line
		n = i + 1;
		m = 0;
		spaceCount = 0;

		// print spaces
		while (n < num)
		{
			cout << " ";
			n = n + 1;
			spaceCount = spaceCount + 1;
		}

		// print symbols
		while (m < (num - spaceCount))
		{
			cout << symbol;
			m = m + 1;
		}

		// print endl to start next line
		cout << endl;
	}

	// exit function by returning 0 integer
	return 0;
}
