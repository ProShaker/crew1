#include <iostream>
#include <array>
using namespace std;

void different_Sum(const int (&array)[6]) // 참조로 전달을 활용해 함수 파라미터로 배열을 넘겨줌
{
	int k = 0;
	for (int e : array) //반복문으로 배열에 존재하는 값 더함
		k += e;
	cout << k << endl; // 더한 값 출력
}

int main()
{
	int array[6]{0}; 
	scanf_s("%d, %d, %d, %d, %d, %d", array, array + 1, array + 2, array + 3, array + 4, array + 5); //배열의 각 원소에 값을 입력받음
	different_Sum(array); //결과물 출력위해 함수 호출
}