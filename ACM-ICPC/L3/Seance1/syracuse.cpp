#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int syracuse(int n) {//, vector<int> *t, int *s) {
  //if (n > )
  int u = n;
  int i = 1;
  while (u != 1) {
    if (u%2 == 0) u = u/2;
    else u = 3*u+1;		 
    i++;
  }
  return i;
}

int main(void) {
  //vector<int> t;
  //  s = -1;
  int m,n;
  while (cin >> m >> n) {
    int c = m;
    m = min(m,n);
    n = max(c,n);
    int res;
    res = 0;
    for (int i=m; i<=n; i++) {
      res = max(res,syracuse(i));
    }
    cout << m << ' ' << n << ' ' << res << endl;
  }

  return 0;
}
