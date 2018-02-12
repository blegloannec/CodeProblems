#include <iostream>
using namespace std;

const int NMAX = 100;
const int RMAX = 30;
const int PMAX = NMAX*RMAX;
int N,R;
int M[NMAX][NMAX];
double P[RMAX+1][NMAX+1][PMAX+1];
double C[RMAX+1][NMAX+1][PMAX+1];

void floyd_warshall() {
  for (int k=0; k<N; ++k)
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j)
	M[i][j] = min(M[i][j],M[i][k]+M[k][j]);
}

void init_dp() {
  for (int r=1; r<=RMAX; ++r) {
    P[r][0][0] = C[r][0][0] = 1.;
    for (int d=1; d<=NMAX; ++d) P[r][d][0] = C[r][d][0] = 0.;
    for (int m=1; m<=r*NMAX; ++m) {
      P[r][0][m] = 0.;
      C[r][0][m] = 1.;
    }
    for (int d=1; d<=NMAX; ++d)
      for (int m=1; m<=r*d; ++m)
	P[r][d][m] = C[r][d][m] = -1.;
  }
}

double dp_proba(int d, int m) {
  if (P[R][d][m]<0) {
    P[R][d][m] = 0.;
    for (int r=1; r<=R && r<=m; ++r)
      P[R][d][m] += dp_proba(d-1,m-r)/R;
  }
  return P[R][d][m];
}

double dp_cumul(int d, int m) {
  if (C[R][d][m]<0) C[R][d][m] = dp_proba(d,m)+dp_cumul(d,m-1);
  return C[R][d][m];
}

int main() {
  init_dp();
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cin >> N >> R;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j) {
	char c;
	cin >> c;
	M[i][j] = (c=='Y' ? 1 : N+1);
      }
    floyd_warshall();
    cout << "Case " << t << endl;
    int C;
    cin >> C;
    for (int c=0; c<C; ++c) {
      int a,b,m;
      cin >> a >> b >> m; --a; --b;
      double p;
      if (M[a][b]>N) p = 0.;
      else if (m>=R*M[a][b]) p = 1.;
      else p = dp_cumul(M[a][b],m);
      cout << p << endl;
    }
    cout << endl;
  }
  return 0;
}
