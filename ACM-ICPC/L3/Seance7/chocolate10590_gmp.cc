#include <iostream>
#include <gmpxx.h>
using namespace std;

#define MAX 5001

typedef mpz_class ent;

ent p[MAX][MAX];

ent traite(int n, int m){
  if (p[n][m] != -1L) return p[n][m];
  else
    {
      if (m == 1) {
	p[n][m] = 1;
	return 1;
      }
      else
	{
	  ent cpt = 0L;
	  for(int i = 0; i <= n/m; ++i)
	    {
	      cpt = cpt + traite(n - i*m,m-1);
	    }
	  p[n][m] = cpt;
	  return cpt;
	}
    }
}
  

void input()
{
  int n;
  //while(scanf("%d",&n) != EOF)
  //int *t = (int*)100;
  //while (cin >> n)
  for (n=0; n<=5000; n++)
    {
      //if (n>4900) *t = 1;
      //printf("%d\n",traite(n,n));
      cout << '"' << traite(n,n) << "\",";
    }

}

int main(void)
{
  for(int i=0; i<MAX; i++)
    for(int j=0; j<MAX; j++)
      {
	p[i][j] = -1L;
      }
  p[0][0] = 0;
  input();
  return 0;
}
