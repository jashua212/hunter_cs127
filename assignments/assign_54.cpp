
// assignment 54

#include <iostream>
using namespace std;

int main()
{
	// declare index variable for outer loop as an integer
	int r;

	// declare index variable for inner loop as an integer
	int c;

	// run outer loop 10 times
	for (r = 0; r < 10; r++)
	{
		// run inner loop 6 times
		for (c = 0; c < 6; c++)
		{
			// print out "10"
			cout << "10";
		}

		// add end line after each run of inner loop
		cout << endl;
	}

	// exit function by returning 0 integer
	return 0;
}
