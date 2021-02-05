#include <cstdio>
using namespace std;

const int NMAX = 2000;

int N;
int X[NMAX], Y[NMAX];
bool Peg[NMAX][NMAX];

int main() {
  scanf("%d", &N);
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j)
      Peg[i][j] = false;
  for (int i=0; i<N; ++i) {
    scanf("%d %d", &X[i], &Y[i]);
    Peg[X[i]][Y[i]] = true;
  }
  
  int cnt = 0;
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j) {
      if (i==j) continue;
      int dx = X[j]-X[i], dy = Y[j]-Y[i];
      int nx = -dy, ny = dx;
      int x3 = X[i]+nx, y3 = Y[i]+ny;
      int x4 = X[j]+nx, y4 = Y[j]+ny;
      if (0<=x3 && x3<N && 0<=y3 && y3<N && Peg[x3][y3] &&
	  0<=x4 && x4<N && 0<=y4 && y4<N && Peg[x4][y4]) ++cnt;
    }
  printf("%d\n", cnt/4);
  return 0;
}
