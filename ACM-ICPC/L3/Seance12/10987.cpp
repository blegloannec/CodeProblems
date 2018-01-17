#include <iostream>
using namespace std;

const int N = 100;
int n;
int W[N][N];
bool G[N][N];

int reverse_floyd_warshall() {
  for (int i=0; i<n; ++i)
    for (int j=i+1; j<n; ++j)
      G[i][j] = true;
  int m = n*(n-1)/2;
  for (int i=0; i<n; ++i)
    for (int j=i+1; j<n; ++j)
      for (int k=0; k<n; ++k) {
	if (k==i || k==j) continue;
	if (W[i][j]>W[i][k]+W[k][j]) return -1;
	if (W[i][j]==W[i][k]+W[k][j]) {
	  G[i][j] = false;
	  --m;
	  break;
	}
      }
  return m;
}

int main() {
  int Cas;
  cin >> Cas;
  for (int t=1; t<=Cas; ++t) {
    cin >> n;
    for (int i=1; i<n; ++i)
      for (int j=0; j<i; ++j) {
	cin >> W[i][j];
	W[j][i] = W[i][j];
      }
    cout << "Case #" << t << ":" << endl;
    int m = reverse_floyd_warshall();
    if (m<0) cout << "Need better measurements." << endl;
    else {
      cout << m << endl;
      for (int i=0; i<n; ++i)
	for (int j=i+1; j<n; ++j)
	  if (G[i][j]) cout << i+1 << ' ' << j+1 << ' ' << W[i][j] << endl;
    }
    cout << endl;
  }
  return 0;
}
