#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 100000001;
vector<bool> P(N,true);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

int main() {
  sieve();
  vector<int> L(1,2);
  for (int p=3; p<N; p+=2)
    if (P[p]) L.push_back(p);
  int T,M;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> M;
    int cpt = 0;
    int i = 0;
    while (L[i]*L[i]<M) {
      int j = distance(L.begin(),upper_bound(L.begin(),L.end(),(M-1)/L[i]));
      cpt += j-i;
      ++i;
    }
    cout << cpt << endl;
  }
  return 0;
}
