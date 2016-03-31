// 256
#include <cstdio>
#include <cmath>
using namespace std;

#define SQR(X) (X)*(X)

int main() {
  int n,m,r;
  while (scanf("%d", &n)==1) {
    r = (int)pow((double)10,(double)n/2);
    m = r*r;
    for (int i=0; i<m; i++)
      if (SQR(i%r + i/r)==i) printf("%0*d\n",n,i);
  }
  return 0;
}
