#include <iostream>
using namespace std;

int main()
{
	int array[6]{ 0 }, x, y, iTemp;
	scanf_s("%d %d %d %d %d %d", array, array + 1,
		array + 2, array + 3, array + 4, array + 5);	// 배열의 각 원소에 값을 입력받음

	for (x = 1 ; x < 6 ; ++x)							// x는 전체반복횟수
		for (int y = 0; y < 5; ++y)						// y는 배열의 첨자
		{
			if (array[y] > array[y + 1])
			{
				iTemp = array[y];
				array[y] = array[y + 1];			    //swap구문을 활용해 거품 정렬 구현
				array[y + 1] = iTemp;
			}		
		}

	cout << '[' << array[0];
	for (x = 1; x < 6; ++x)						        //출력예시대로 출력하기 위한 
		cout << ", " << array[x];
	cout << ']' << endl;
		
}