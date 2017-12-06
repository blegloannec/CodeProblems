#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 1001

int t[MAX][MAX];
char a[MAX];
char b[MAX];

int main() {
  int sa,sb,res;
  cin >> noskipws;
  while (cin.getline(a,MAX)&&cin.getline(b,MAX)) {
    sa = sb = 0;
    while (a[sa]!=0 && sa<=1000) ++sa;
    while (b[sb]!=0 && sb<=1000) ++sb;
    for (int i=0; i<=sa; ++i)
      t[i][0] = 0;
    for (int i=0; i<=sb; ++i)
      t[0][i] = 0;
    for (int i=1; i<=sa; ++i)
      for (int j=1; j<=sb; ++j) {
        res = max(t[i][j-1],t[i-1][j]);
        if (a[i-1]==b[j-1]) res = max(res,t[i-1][j-1]+1); 
        t[i][j] = res;
      }
    cout << t[sa][sb] << '\n';
  }
    
  return 0;
}
