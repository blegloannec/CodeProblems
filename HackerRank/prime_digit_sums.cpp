#include <cstdio>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

const vector<int> P {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43};
const int N = 400002;
const int MOD = 1000000007;

void addmod(int &a, int b) {
  a += b;
  if (a>=MOD) a -= MOD;
}

vector<int> digit_sums(int n, int k=5) {
  vector<int> D(k+1,0);
  for (int i=1; i<=k; ++i) {
    D[i] = n%10;
    n /= 10;
  }
  for (int i=1; i<=k; ++i) D[i] += D[i-1];
  return D;
}

vector<int> precomp() {
  // Transitions
  unordered_map<int,int> Num;
  vector< vector<int> > Trans;
  vector<int> Cnt;
  for (int x=0; x<100000; ++x) {
    auto D = digit_sums(x);
    bool valid = true;
    for (int s=3; valid && s<=5; ++s)
      for (int i=s; valid && i<=5; ++i)
	if (find(P.begin(),P.end(),D[i]-D[i-s])==P.end())
	  valid = false;
    if (valid) {
      int l = x/10;
      if (Num.find(l)==Num.end()) {
	Num[l] = Trans.size();
	Trans.resize(Trans.size()+1);
	Cnt.resize(Cnt.size()+1,0);
      }
      int r = x % 10000;
      if (Num.find(r)==Num.end()) {
	Num[r] = Trans.size();
	Trans.resize(Trans.size()+1);
	Cnt.resize(Cnt.size()+1,0);
      }
      Trans[Num[l]].push_back(Num[r]);
      if (x>=10000) ++Cnt[Num[r]];
    }
  }
  int K = Trans.size();
  // DP
  vector<int> DP {0, 9, 90, 303, 280};
  DP.resize(N,0);
  for (int i=5; i<N-1; ++i) {
    vector<int> NewCnt(K,0);
    for (int k=0; k<K; ++k)
      for (int l : Trans[k])
	addmod(NewCnt[l], Cnt[k]);
    for (int k=0; k<K; ++k)
      addmod(DP[i], Cnt[k]);
    Cnt = NewCnt;
  }
  return DP;
}

int main() {
  auto DP = precomp();
  int Q;
  scanf("%d", &Q);
  for (int t=0; t<Q; ++t) {
    int n;
    scanf("%d", &n);
    printf("%d\n", DP[n]);
  }
  return 0;
}
