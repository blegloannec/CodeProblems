#include <cstdio>
#include <cmath>
using namespace std;

const int CMAX = 100000;
bool P[CMAX];
double Rad[CMAX];
double Log[CMAX];

void sieve() {
  for (int i=1; i<CMAX; ++i) {
    P[i] = true;
    Log[i] = log2(i);
    Rad[i] = Log[1];
  }
  for (int i=2; i<CMAX; ++i)
    if (P[i]) {
      Rad[i] = Log[i];
      for (int j=2*i; j<CMAX; j+=i) {
	Rad[j] += Log[i];
	P[j] = false;
      }
    }
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int comp(int C, double r) {
  double cr,cr2,rad_ac;
  int b,step;
  int res = 0;
  for (int c=3; c<C; ++c) {
    cr = r*Log[c];
    cr2 = cr-Log[2];
    if (Rad[c] >= cr2) continue;
    step = 2 - c%2;
    for (int a=1; a<=2; a+=step) {
      rad_ac = Rad[a]+Rad[c];
      if (rad_ac >= cr2) continue;
      b = c-a;
      if (rad_ac+Rad[b]<cr && gcd(a,b)==1) res += c;
    }
    //a>2
    if (step==1) {if (Log[6]+Rad[c] >= cr) continue;}
    else if (Log[15]+Rad[c] >= cr) continue;
    for (int a=3; a<=c/2; a+=step) {
      rad_ac = Rad[a]+Rad[c];
      if (rad_ac >= cr2) continue;
      b = c-a;
      if (rad_ac+Rad[b]<cr && gcd(a,b)==1) res += c;
    }
  }
  return res;
}

int main() {
  int T,L;
  double r;
  sieve();
  scanf("%d\n",&T);
  for (int t=0; t<T; ++t) {
    scanf("%lf %d\n",&r,&L);
    printf("%d\n",comp(L,r));
  }
  return 0;
}

/*
  Ici on passe tout aux log (pre-calcules) pour remplacer les
  multiplications de long long par des additions de double.
*/
