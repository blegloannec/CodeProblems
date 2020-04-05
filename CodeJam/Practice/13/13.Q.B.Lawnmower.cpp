#include <iostream>
using namespace std;

#define SIZE 100

int T,N,M;
int a[SIZE][SIZE];
int maxl[SIZE];
int maxc[SIZE];

bool verif() {
  for (int i=0; i<N; ++i)
    for (int j=0; j<M; ++j)
      if (a[i][j]!=min(maxc[i],maxl[j])) return false;
  return true;
}

int main() {
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cin >> N >> M;
    for (int i=0; i<N; ++i) maxc[i] = -1;
    for (int j=0; j<M; ++j) maxl[j] = -1;
    for (int i=0; i<N; ++i) {
      for (int j=0; j<M; ++j) {
	cin >> a[i][j];
	if (a[i][j]>maxc[i]) maxc[i]=a[i][j];
	if (a[i][j]>maxl[j]) maxl[j]=a[i][j];
      }
    }
    if (verif()) cout << "Case #" << t << ": YES" << endl;
    else cout << "Case #" << t << ": NO" << endl;
  }
  return 0;
}
