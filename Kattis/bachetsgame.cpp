#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N;
  while (cin >> N) {
    int M;
    cin >> M;
    vector<int> S(M);
    for (int i=0; i<M; ++i) cin >> S[i];
    vector<bool> Win(N+1,false);
    for (int i=1; i<=N; ++i) {
      for (int m : S)
	if (i>=m && !Win[i-m]) {
	  Win[i] = true;
	  break;
	}
    }
    cout << (Win[N] ? "Stan" : "Ollie") << " wins\n";
  }
  return 0;
}
