#include <iostream>
using namespace std;
/*
* ������ �ٽ�: �����Ǵ� ���� ��Ģ�� ã�ƶ�
* 
*	������ ���տ� ���Ե� 2�� ����   0(111..)	1(211..)	2(2211..)	3(2221...)           ������ ����� ��
*					������ ����                                                                  
*						3				1           2                      						 3
*						4				1           3           1           			         5	(1���� + 1����)
*						5				1           4           3           			         8	(1���� + 2����)
*						6				1           5           6           1			         13	(1���� + 3���� + 1����)
*						7				1           6           10          4			         21	(1���� + 4���� + 4����)
*						. 
*						.
*						.
*/
int main() {
	int n_pizza, number_Of_Separations = 3;
	int i = 2, j = 1;
	cout << "���ڰ� ���������� �˷��ּ���. : ";
	cin >> n_pizza;

	for (; n_pizza > 3; n_pizza--, i += j,j += 1) {
		number_Of_Separations += i;
	}
	
	cout << number_Of_Separations << endl;
}