#include <iostream>
using namespace std;

#define MAX 101

int C;
int G[MAX][MAX];
int P[MAX][MAX];
int Q[MAX][MAX];
int arrivee[MAX];


void prod(int m[MAX][MAX], int s[MAX][MAX], int d[MAX][MAX]) {
  int coef;
  for (int i=1; i<=C; i++)
    for (int j=1; j<=C; j++) {
      coef = -1;
      for (int k=1; k<=C; k++) 
	coef = max(coef, s[i][k]+d[k][j]);
      m[i][j] = coef;
    }
}

void copy(int s[MAX][MAX], int d[MAX][MAX]) {
  for (int i=0; i<=C; i++)
    for (int j=0; j<=C; j++)
      d[i][j] = s[i][j];
}


int main () {
  int S,E,T,res;
  while (cin >> C >> S >> E >> T) {
    if ((C==0)&&(S==0)&&(E==0)&&(T==0)) return 0;
    for (int i=1; i<=C; i++)
      for (int j=1; j<=C; j++)
	cin >> G[i][j];
    for (int i=1; i<=E; i++) 
      cin >> arrivee[i];
    copy(G,P);
    //for (int k=1; k<=T-1; k++) {
      
      //prod(Q,P,G);
      //copy(Q,P);
    //}
    int k = T-1;
    while (k>=1) {
      if (k%2==0) {
	prod(Q,P,P);
	copy(Q,P);
	k = k/2;
      }
      else {
	prod(Q,P,G);
	copy(Q,P);
	--k;
      }
    }
    res = -1;
    for (int k=1; k<=E; k++)
      res=max(res,Q[S][arrivee[k]]);
    cout << res << '\n';
  }
  return 0;
}
