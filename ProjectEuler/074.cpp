#include <iostream>
using namespace std;

const int N = 1000001;

int fact[10] = {1,1,2,6,24,120,720,5040,40320,362880};

int f(int n) {
  int res = 0;
  while (n>0) {
    res += fact[n%10];
    n/=10;
  }
  return res;
}

int floyd(int n) {
  // attention a l'init !
  int x = f(n);
  int y = f(f(n));
  while (x!=y) {
    x = f(x);
    y = f(f(y));
  }
  int l0 = 0;
  x = n;
  while (x!=y) {
    x = f(x);
    y = f(y);
    ++l0;
  }
  int l1 = 1;
  y = f(y);
  while (x!=y) {
    y = f(y);
    ++l1;
  }
  return l0+l1;
}

int main() {
  int res = 0;
  for (int i=1; i<N; ++i)
    if (floyd(i)==60) res +=1;
  cout << res << endl;
  return 0;
}
