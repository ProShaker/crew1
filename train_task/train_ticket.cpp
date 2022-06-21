#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
	string line;
	ifstream file("TrainList.txt"); // example.txt 파일을 연다. 없으면 생성. 
	if (file.is_open()) {
		while (getline(file, line)) {
			cout << line << endl;
		}
		file.close(); // 열었떤 파일을 닫는다. 
	}
	else {
		cout << "Unable to open file";
		return 1;
	}
	return 0;
}