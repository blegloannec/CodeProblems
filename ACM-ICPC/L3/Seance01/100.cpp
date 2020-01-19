#include <iostream>
#include <cstdio>
using namespace std;

int syracuse(int n) {
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
  int m,n;
  while (cin >> m >> n) {
    int res = 0;
    for (int i=min(m,n); i<=max(m,n); i++)
      res = max(res,syracuse(i));
    cout << m << ' ' << n << ' ' << res << endl;
  }

  return 0;
}
