#include <iostream>
#include <array>
using namespace std;

void different_Sum(const int (&array)[6]) // ������ ������ Ȱ���� �Լ� �Ķ���ͷ� �迭�� �Ѱ���
{
	int k = 0;
	for (int e : array) //�ݺ������� �迭�� �����ϴ� �� ����
		k += e;
	cout << k << endl; // ���� �� ���
}

int main()
{
	int array[6]{0}; 
	scanf_s("%d, %d, %d, %d, %d, %d", array, array + 1, array + 2, array + 3, array + 4, array + 5); //�迭�� �� ���ҿ� ���� �Է¹���
	different_Sum(array); //����� ������� �Լ� ȣ��
}