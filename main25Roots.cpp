#include <iostream>
#include <cmath>
using namespace std;
//https://inf-ege.sdamgia.ru/problem?id=29673
void Check(int x)
{
    int cntRoot = 0;
    int maxDel = 0;
    for (int del = 2; del <= x/2; del++)
    {
        if (x % del == 0)
        {
            cntRoot++;
            maxDel = del;
        }
        if (cntRoot > 3) { return; }
    }

    if (cntRoot == 3) { cout << x << " " << maxDel << endl; }
}

void CheckByRoot(int root)
{
    const int x = pow(root, 2);
    int cntRoot = 0;
    int maxDel = 0;
    for (int del = 2; del < root; del++)
    {
        if (x % del == 0)
        {
            cntRoot++;
            maxDel = x / del;
        }
        if (cntRoot > 1) { return; }
    }

    if (cntRoot == 1) { cout << x << " " << maxDel << endl; }
}

int main()
{
    cout << sqrt(123456789) << endl
         << sqrt(223456789) << endl;

    for (int root = 11112; root <= 14948; root++)
    {
        //Check(pow(root, 2));
        CheckByRoot(root);
    }
    return 0;
}
