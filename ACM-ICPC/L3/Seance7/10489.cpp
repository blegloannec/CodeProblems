#include <iostream>
using namespace std;

int main() {
  int T,N,B,K,nb,v,res;
  
  cin >> T;
  while (T-->0) {
    cin >> N >> B;
    res = 0;
    for (int i=1; i<=B; i++) {
      nb = 1;
      cin >> K;
      for (int j=1; j<=K; j++) {
	cin >> v;
	nb = (nb*(v%N))%N;
      }
      res = (res+nb)%N;
    }
    cout << res << '\n';
  }

  return 0;
}
