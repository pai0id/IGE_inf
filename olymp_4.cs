using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//не получилось(

namespace _4
{
    class Program
    {
        static string Rev (string x, int y)
        {
            char[] wrd = new char[y];
            for (int n = 0; n < y; n++)
            {
                char f = x[n];
                wrd[n] = f;
            }
            Array.Reverse(wrd);
            string fin="";
            for (int k = 0; k < y; k++)
            {
                char h = wrd[k];
                fin[k] = h;
            }
            return fin;
        }
        static void Main(string[] args)
        {
            string world = Console.ReadLine();
            int leng = world.Length;
            if (leng % 2 == 0)
            {
                int hleng = leng / 2;
                world = world.Insert(hleng, " ");
                string str1 = world.Remove(world.IndexOf(' '));
                string str2 = world.Substring(world.IndexOf(' ')+1);
                int j = str2.Length;
                if (String.Equals(str1, Rev(str2, j))) 
                {
                    Console.WriteLine(0);
                }
            }
            Console.ReadKey(true);
        }
    }
}
