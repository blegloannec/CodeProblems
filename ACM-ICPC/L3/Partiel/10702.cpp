#include <iostream>
using namespace std;

#define MAX 101
#define MAXD 1001
#define INF -100000000

int C;
int t[MAXD][MAX];
int G[MAX][MAX];
int arrivee[MAX];


int main () {
  int S,E,T,res;
  while (cin >> C >> S >> E >> T) {
    if ((C==0)&&(S==0)&&(E==0)&&(T==0)) return 0;
    for (int i=1; i<=C; i++)
      for (int j=1; j<=C; j++)
	cin >> G[i][j];
    for (int j=1; j<=C; j++)
      t[T+1][j] = INF;
    for (int i=1; i<=E; i++) {
      cin >> arrivee[i];
      t[T+1][arrivee[i]] = 0;
    }
    for (int i=T; i>0; i--) {
      for (int j=1; j<=C; j++) {
	res = INF;
	for (int k=1; k<=C; k++) 
	  res = max(res,G[j][k]+t[i+1][k]);
	t[i][j] = res;
      }
    }
    cout << t[1][S] << '\n';
  }
  return 0;
}
