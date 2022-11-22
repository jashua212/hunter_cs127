
// assignment 60
// convert integer into two's complement notation

#include <iostream>
using namespace std;

int main()
{
	// declare integer variables
	int n, num, rem, size, delta, i;

	// declare and initialize string variable
	string result = "";

	// get 'n' integer from user
	cout << "Enter an int in [-128, 127]: ";
	cin >> n;

	// set 'num' to equal 'n'
	num = n;

	// if 'num' is negative, make it positive and subtract 1
	if (num < 0)
		num = (-1 * num) - 1;

	// while 'num' is greater than 0,
	// divide 'num' by 2 to get 'rem',
	// prepend 'rem' to 'result' string, and
	// divide 'num' by 2 for use in next iteration
	while (num > 0)
	{
		rem = num % 2;
		result = to_string(rem) + result;
		num = num/2;
	}

	// prepend 0s to fill out 'result' string to be 8 bits/characters
	size = 8;
	delta = size - result.length();
	for (i = 0; i < delta; i++)
		result = '0' + result;

	// flip 0s and 1s of 'result' string if 'n' is negative
	if (n < 0)
	{
		for (i = 0; i < size; i++)
		{
			if (result[i] == '0')
				result[i] = '1';
			else
				result[i] = '0';
		}
	}

	// print 'result'
	cout << "binary string: " << result;

	// exit function by returning 0 integer
	return 0;
}
