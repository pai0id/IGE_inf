#include <iostream>
#include <string>

using namespace std;

// https://inf-ege.sdamgia.ru/problem?id=10504

int main()
{
    string row(1000, '9');
    while (true)
    {
        int pos999 = row.find("999");
        int pos888 = row.find("888");

        if (pos999 == -1 && pos888 == -1)
        {
            break;
        }

        if (pos888 != -1)
        {
            row.replace(pos888, 3, "9");
        }
        else
        {
            row.replace(pos999, 3, "8");
        }
    }

    cout << row;

    return 0;
}
