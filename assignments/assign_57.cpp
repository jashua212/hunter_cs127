
// assignment 57

#include <iostream>
using namespace std;

int main()
{
	// declare 'hours' integer variable
	int hours;

	// get 'hours' integer from user
	cout << "Enter number of credit hours taken: ";
	cin >> hours;

	// if-else decision tree
	if (hours < 28)
		cout << "freshman";
	else if (hours < 61)
		cout << "sophomore";
	else if (hours < 94)
		cout << "junior";
	else if (hours >= 94)
		cout << "senior";

	// exit function by returning 0 integer
	return 0;
}
