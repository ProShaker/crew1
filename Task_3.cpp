#include <iostream>
#include <array>
using namespace std;

void different_Sum(const int (&array)[6])
{
	int k = 0;
	for (int e : array)
		k += e;
	cout << k << endl;
}

int main()
{
	int array[6]{0};
	scanf_s("%d, %d, %d, %d, %d, %d", array, array + 1, array + 2, array + 3, array + 4, array + 5);
	different_Sum(array);
}