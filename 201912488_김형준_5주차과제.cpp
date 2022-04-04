#include <iostream>
using namespace std;
/*
* 과제의 핵심: 증가되는 수의 규칙을 찾아라
* 
*	조각의 조합에 포함된 2의 개수   0(111..)	1(211..)	2(2211..)	3(2221...)           나누는 방법의 수
*					피자의 조각                                                                  
*						3				1           2                      						 3
*						4				1           3           1           			         5	(1증가 + 1증가)
*						5				1           4           3           			         8	(1증가 + 2증가)
*						6				1           5           6           1			         13	(1증가 + 3증가 + 1증가)
*						7				1           6           10          4			         21	(1증가 + 4증가 + 4증가)
*						. 
*						.
*						.
*/
int main() {
	int n_pizza, number_Of_Separations = 3;
	int i = 2, j = 1;
	cout << "피자가 몇조각인지 알려주세요. : ";
	cin >> n_pizza;

	for (; n_pizza > 3; n_pizza--, i += j,j += 1) {
		number_Of_Separations += i;
	}
	
	cout << number_Of_Separations << endl;
}