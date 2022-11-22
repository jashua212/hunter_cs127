
// assignment 59

#include <iostream>
using namespace std;

int main()
{
	// declare float variables
	float budget, expense, monExpense;

	// declare integer variable
	int i;

	// get 'budget' integer from user
	cout << "Input your annual budget: ";
	cin >> budget;

	// get 'expense' integer from user
	cout << "Input your month expense: ";
	cin >> expense;

	// print column headings
	cout << "month   expense remaining balance of budget\n";

	// run loop - each iteration prints one line
	for (i = 1; i < 13; i++)
	{
		// set monExpense
		if (i <= 6)
			monExpense = expense;
		else
			monExpense = expense * 1.15;

		// calculate remaining budget
		budget = budget - monExpense;

		// print line
		printf("%5d\t%7.2f\t%27.2f\n", i, monExpense, budget);
	}

	// print if budget is negative
	if (budget < 0)
		cout << "need higher budget";

	// exit function by returning 0 integer
	return 0;
}
