#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void Calc(const string & fileName)
{
    int n;
    ifstream ifs(fileName);
    ifs >> n;
    vector<int> bins(n);
    for (size_t i = 0; i < bins.size(); i++)
    {
        ifs >> bins[i];
    }


    int64_t minRingPrice = INT64_MAX;
    int minFactoryPos = 0;

    for (int factoryPos = 0;  factoryPos < n; factoryPos++)
    {
        int64_t ringPrice = 0;
        for (int binPos = 0;  binPos < n; binPos++)
        {
            int directWay = abs(binPos - factoryPos);
            int shortWay = min(directWay, n - directWay);
            ringPrice += shortWay * bins[binPos];
        }

        if (ringPrice < minRingPrice)
        {
            minRingPrice = ringPrice;
            minFactoryPos = factoryPos; //индексация от 0!
        }
    }

    cout << minFactoryPos + 1 << endl;
}

int main()
{
    Calc("27-A.txt");
    return 0;
}
