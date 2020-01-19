#include <iostream>
#include <cmath>
using namespace std;

const int N = 101;
double P[N][N],Binom[N][N];

int main() {
  for (int n=0; n<N; ++n) {
    Binom[n][0] = 1.;
    for (int p=1; p<=n; ++p)
      Binom[n][p] = Binom[n-1][p-1]+Binom[n-1][p];
  }
  for (int c=0; c<N; ++c) P[0][c] = 0.;
  for (int b=1; b<N; ++b) {
    P[b][0] = 1.;
    for (int c=1; c<N; ++c) {
      if (b>c) P[b][c] = 1.;
      else {
	P[b][c] = pow(1.-1./b,c);
	for (int d=1; d<=c; ++d)
	  P[b][c] += Binom[c][d]*P[b-1][c-d]*pow(1./b,d)*pow(1.-1./b,c-d);
      }
    }
  }
  int k=1,b,c;
  while (scanf("%d %d",&c,&b)==2)
    printf("Case %d: %.7f\n",k++,P[b][c]);
  return 0;
}
