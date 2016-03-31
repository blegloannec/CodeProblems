// Cutting sticks

#include <iostream>
using namespace std;

#define MAX 51
#define INTMAX 5000000

int n,l;
int t[MAX];
int mem[MAX][MAX];

void clearmem() {
  for (int i=0; i<=n+1; i++) 
    for (int j=0; j<=n+1; j++)
      mem[i][j] = -1;
}

int calcul(int x, int y) { // cout minimal de la coupe du segment [x,y]
  if (y-x<=1) return 0;
  int m = mem[x][y];
  if (m>=0) return m;
  int res = INTMAX;
  for (int i=x+1; i<y; i++) 
    res = min(res,(t[y]-t[x])+calcul(x,i)+calcul(i,y));
  mem[x][y] = res;
  return res;
}

int main() {
  t[0] = 0;

  while (cin >> l) {
    if (l==0) return 0;
    cin >> n;
    clearmem();
    for (int i=1; i<=n; i++) 
      cin >> t[i];
    t[n+1] = l;

    cout << "The minimum cutting is " << calcul(0,n+1) << ".\n";

  }

  return 0;
}
