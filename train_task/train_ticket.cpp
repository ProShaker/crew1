#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
	string line;
	ifstream file("TrainList.txt"); // example.txt ������ ����. ������ ����. 
	if (file.is_open()) {
		while (getline(file, line)) {
			cout << line << endl;
		}
		file.close(); // ������ ������ �ݴ´�. 
	}
	else {
		cout << "Unable to open file";
		return 1;
	}
	return 0;
}