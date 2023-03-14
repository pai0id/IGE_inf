#include <iostream>
#include <cmath>
using namespace std;

bool HasFiveOddDels(int x)
{
    //for (; x % 2 == 0; x/=2);

    int cnt = 0;
    int root = sqrt(x);
    if (root*root == x)
    {
        if (root % 2 == 1)  { cnt++; }
        for (int del1 = 2; del1 < root; del1++)
        {
            if (x % del1 == 0)
            {
                int del2 = x / del1;
                if (del1 % 2 == 1) { cnt++; }
                if (del2 % 2 == 1) { cnt++; }
            }
            if (cnt > 5) { break; }
        }
    }
    else
    {
        for (int del1 = 2; del1 <= root; del1++)
        {
            if (x % del1 == 0)
            {
                int del2 = x / del1;
                if (del1 % 2 == 1) { cnt++; }
                if (del2 % 2 == 1) { cnt++; }
            }
            if (cnt > 5) { break; }
        }
    }

    return (1 + cnt + (x % 2 == 1 ? 1 : 0)) == 5;

    //return cnt == 5;
}


int main()
{
    for (int x = 35000000; x <= 40000000; x++)
    {
        if (HasFiveOddDels(x))
        {
            cout << x << endl;
        }
    }

    return 0;
}
