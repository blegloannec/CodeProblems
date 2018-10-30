#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N,M,K,L;
vector<int> A;

int mintime() {
  sort(A.begin(),A.end());
  A.push_back(K);
  /* Il est toujours optimal d'entrer soit a t = A[i]
     (juste avant le i-eme client), soit a t = K. */
  int res = 1<<30;
  for (int i=0; i<N+1; ++i) {
    int m = M+i - A[i]/L;
    /* m = nb de personnes dans la file
           - nb de places liberees
	   sur l'intervalle t < A[i] */
    if (m<0) return 0;  // on rentre sans attendre
    int dt = ((A[i]+L)/L)*L + m*L - A[i];
    // dt = tps d'attente avant d'entrer si on arrive a t = A[i]
    res = min(res,dt);
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> M >> K >> L;
    A.resize(N);
    for (int i=0; i<N; ++i) cin >> A[i];
    cout << mintime() << endl;
  }
  return 0;
}
