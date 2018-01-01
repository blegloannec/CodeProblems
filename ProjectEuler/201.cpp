#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// runs in 4s with -O3

const int N = 100;
const int K = 50;
vector< unordered_map<int,int> > C(K+1);

int main() {
  C[0][0] = 1;
  for (int i=1; i<=N; ++i)
    for (int j=min(K,i)-1; j>=0; --j)
      for (auto it=C[j].begin(); it!=C[j].end(); ++it)
	C[j+1][it->first+i*i] += it->second;
  int res = 0;
  for (auto it=C[K].begin(); it!=C[K].end(); ++it)
    if (it->second==1) res += it->first;
  cout << res << endl;
  return 0;
}
