#include <iostream>
#include <string>

using namespace std;

string func(int l) {
	string row(l, '1');
	while (true) {
		int pos111 = row.find("111");
		if (pos111 == -1)
			break;
		row.replace(pos111, 3, "2");
		int pos222 = row.find("222");
		if (pos222 != -1)
			row.replace(pos222, 3, "11");
	}
	return row;
}

int main()
{
	int n = 61;
	while (true)
	{
		if (func(n) == "2211")
			break;
		else
			n++;
	}

	cout << n;

	return 0;
}
