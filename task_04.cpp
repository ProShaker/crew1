#include <iostream>
using namespace std;

int main()
{
	int array[6]{ 0 }, x, y, iTemp;
	scanf_s("%d %d %d %d %d %d", array, array + 1,
		array + 2, array + 3, array + 4, array + 5);	// �迭�� �� ���ҿ� ���� �Է¹���

	for (x = 1 ; x < 6 ; ++x)							// x�� ��ü�ݺ�Ƚ��
		for (int y = 0; y < 5; ++y)						// y�� �迭�� ÷��
		{
			if (array[y] > array[y + 1])
			{
				iTemp = array[y];
				array[y] = array[y + 1];			    //swap������ Ȱ���� ��ǰ ���� ����
				array[y + 1] = iTemp;
			}		
		}

	cout << '[' << array[0];
	for (x = 1; x < 6; ++x)						        //��¿��ô�� ����ϱ� ���� 
		cout << ", " << array[x];
	cout << ']' << endl;
		
}