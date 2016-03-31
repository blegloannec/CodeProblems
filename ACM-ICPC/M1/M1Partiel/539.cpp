#include <iostream>
#include <cmath>
using namespace std;

#define MAX 26

int t[MAX][MAX];

int n;

int parcours(int start) {
  int res = 0;
  for (int i=0; i<n; ++i) {
    if (t[start][i] == 1) {
      t[start][i] = t[i][start] = 0;
      res = max(res,1+parcours(i));
      t[start][i] = t[i][start] = 1;
    }
  }
  return res;
}

int main() {
  int a,b,res,m;
  while (cin >> n >> m) {
    if (n==0 && m==0) return 0;
    for (int i=0; i<n; ++i)
      for (int j=0; j<n; ++j) 
        t[i][j] = 0;
    for (int i=0; i<m; ++i) {
      cin >> a >> b;
      t[a][b] = t[b][a] = 1;
    }
    res = 0;
    for (int i=0; i<n; ++i) {
      res = max(res,parcours(i));
    }
    cout << res << '\n';
  }
  return 0;
  
}
