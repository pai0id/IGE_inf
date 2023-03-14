using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3
{
    class Program
    {
        static void Main(string[] args)
        {
            long A = long.Parse(Console.ReadLine());
            long B = long.Parse(Console.ReadLine());
            long Bres = B;
            long Ares = A;
            long polk1 = 1;
            long polk2 = 1;
            int k = 0;
            Random rnd = new Random();
            long[] arr = new long[5];
            do
            {
                A *= polk1;
                B *= polk2;
                ++A;
                --B;
                if(A == B)
                {
                    arr[k] = A;
                    if(k == 4)
                    {
                        A = arr.Min();
                        break;
                    }
                    k++;
                }
                int H = rnd.Next(0, 1);
                if(H == 0)
                {
                    ++polk1;
                    B = Bres;
                    A = Ares;
                }
                else
                {
                    ++polk2;
                    B = Bres;
                    A = Ares;
                }
                if(polk1>100   && polk2 > 100)
                {
                    polk1 = 1;
                    polk2 = 1;
                    B = Bres;
                    A = Ares;
                }
            }
            while (true);
            Console.WriteLine(A);
            Console.ReadKey(true);
        }
    }
}
