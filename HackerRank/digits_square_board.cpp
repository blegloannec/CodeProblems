#include <iostream>
#include <vector>
using namespace std;

const int MEXMAX = 50;
const int M = 31;
int N;
int A[M][M], Memo[M][M][M][M];

int grundy(int i0, int j0, int i1, int j1) {
  if (Memo[i0][j0][i1][j1]<0) {
    int p = A[i1][j1] - A[i1][j0-1] - A[i0-1][j1] + A[i0-1][j0-1];
    int g = 0;
    if (p>0) {
      vector<bool> G(MEXMAX,false);
      for (int i=i0; i<i1; ++i)
	G[grundy(i0,j0,i,j1)^grundy(i+1,j0,i1,j1)] = true;
      for (int j=j0; j<j1; ++j)
	G[grundy(i0,j0,i1,j)^grundy(i0,j+1,i1,j1)] = true;
      while (G[g]) ++g;
    }
    Memo[i0][j0][i1][j1] = g;
  }
  return Memo[i0][j0][i1][j1];
}

int main() {
  for (int i=0; i<M; ++i)
    A[i][0] = A[0][i] = 0;
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    for (int i=1; i<=N; ++i)
      for (int j=1; j<=N; ++j) {
	int a;
	cin >> a;
	A[i][j] = (int)(a!=2 && a!=3 && a!=5 && a!=7);
      }
    for (int i=1; i<=N; ++i) {
      int l = 0;
      for (int j=1; j<=N; ++j) {
	l += A[i][j];
	A[i][j] = l + A[i-1][j];
      }
    }
    for (int i0=1; i0<=N; ++i0)
      for (int j0=1; j0<=N; ++j0)
	for (int i1=1; i1<=N; ++i1)
	  for (int j1=1; j1<=N; ++j1)
	    Memo[i0][j0][i1][j1] = -1;
    cout << (grundy(1,1,N,N)==0 ? "Second" : "First") << '\n';
  }
  return 0;
}
