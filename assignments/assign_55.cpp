
// assignment 55

#include <iostream>
using namespace std;

int main()
{
	// declare floating number variables
	float celsius, faren;

	// get temp in celsius from user
	cout << "Enter temperature in celsius: ";
	cin >> celsius;

	// convert to farenheit
	faren = 9.0/5 * celsius + 32;

	// print temp in farenheit
	cout << "Temperature in fahrenheit: " << faren;

	// exit function by returning 0 integer
	return 0;
}
