#include <iostream>
#include <cmath>
using namespace std;

#define MAX 1441
#define MAXINT 2000000000

int arrive[MAX];
int tps[MAX]; 
int nbar[MAX]; 
int n,t;
// tps[i] le temps minimal pour faire passer les i premières voitures
// et revenir
// nbar retient en plus le nb d'allers-retours pour le meilleur score

int f(int i) {
  int tmp;
  if (tps[i]>=0) return tps[i];
  int res = MAXINT;
  int voy = MAXINT;
  int M = min(n,i);
  for (int k=1; k<=M; ++k) {
    tmp = max(f(i-k),arrive[i-1])+2*t;
    if (tmp < res) {
      res = tmp;
      voy = nbar[i-k]+1;
    }
    else if (tmp == res) 
      voy = min(voy,nbar[i-k]+1);
  }
  tps[i] = res;
  nbar[i] = voy;
  return res;
}

int main() {
  int cas,m;
  cin >> cas;
  tps[0] = 0;
  nbar[0] = 0;
  while (cas-->0) {
    cin >> n >> t >> m;
    for (int i=1; i<=m; ++i) {
      tps[i] = -1;
      nbar[i] = -1;
    }
    for (int i=0; i<m; ++i)
      cin >> arrive[i];
    int res = f(m)-t;
    cout << res << ' ' << nbar[m] << '\n';    
  }
  return 0;
}
