#include <iostream>
using namespace std;

const int N = 121;
const int M = 16;
int R[N][M][M];
int C[N][M];

int main() {
  string name;
  while (cin >> name) {
    int n,m;
    cin >> n >> m;
    for (int r=0; r<n-1; ++r)
      for (int i=0; i<m; ++i)
	for (int j=0; j<m; ++j)
	  cin >> R[r][i][j];
    for (int i=0; i<m; ++i) C[0][i] = 0;
    for (int r=1; r<n; ++r)
      for (int i=0; i<m; ++i) {
	C[r][i] = 1<<30;
	for (int j=0; j<m; ++j)
	  C[r][i] = min(C[r][i],C[r-1][j]+R[r-1][j][i]+2);
      }
    int d = 1<<30;
    for (int i=0; i<m; ++i) d = min(d,C[n-1][i]);
    cout << name << endl;
    cout << d << endl;
  }
  return 0;
}
