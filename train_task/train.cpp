#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

//txt ���Ϸ� �ҷ��� ��������
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
	cout << "<<�޴� ȭ��>>" << endl << endl;
	cout << "1. ���� �ð� ���� �˻� �� ����" << endl;
	cout << "2. ��ü ���� ����Ʈ ���" << endl;
	cout << "3. ���� ��Ȳ ��� �� ���� ���" << endl;
	cout << "4. ���α׷� ����" << endl<<endl;
	cout << "���Ͻô� ��ȣ�� �������ּ���.";

	cin >> menu_numb;
	cout << endl;

	switch (menu_numb)
	{
	case 1:
		cout << menu_numb << "���� �����ϼ̽��ϴ�. \n";

		break;
	default:
		cout << "�޴��� ���� ��ȣ�Դϴ�.\n";
	}

	
}

train_func::~train_func()
{
}
