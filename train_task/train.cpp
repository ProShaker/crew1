#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

//txt 파일로 불러온 열차정보
class train_inform
{
	friend class train_func;
	string train_time = "";
	string train_depart = "";
	string train_arrival = "";
	string train_type = "";
	int train_seat = 0;

	train_inform* next = nullptr;
};

class train_func
{
public:
	train_func()
	{
		train_inform* start_node = new train_inform;
		train_inform* head = start_node;
		train_inform* tail = start_node;
	};

	~train_func();



};

void train_menu(int menu_numb);

int main()
{
	
	return 0;
}

void train_menu(int menu_numb)
{
	system("cls");
	cout << "<<메뉴 화면>>" << endl << endl;
	cout << "1. 빠른 시간 기차 검색 및 예매" << endl;
	cout << "2. 전체 기차 리스트 출력" << endl;
	cout << "3. 예매 현황 출력 및 예매 취소" << endl;
	cout << "4. 프로그램 종료" << endl<<endl;
	cout << "원하시는 번호를 선택해주세요.";

	cin >> menu_numb;
	cout << endl;

	switch (menu_numb)
	{
	case 1:
		cout << menu_numb << "번을 선택하셨습니다. \n";

		break;
	default:
		cout << "메뉴에 없는 번호입니다.\n";
	}

	
}

train_func::~train_func()
{
}
