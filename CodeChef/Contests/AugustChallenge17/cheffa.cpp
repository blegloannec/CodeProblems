#include <cstdio>
#include <vector>
#include <unordered_map>
using namespace std;

typedef unsigned long long ent;

const int P = 1000000007;
int N;
vector<int> A;

unordered_map<ent,int> memo;

int dp(int a0, int a1, int i=0) {
  if (i+2>=N && (a0==0 || a1==0)) return 1;
  ent K = ((ent)a0<<24) | ((ent)a1<<12) | i;
  if (memo.find(K)!=memo.end()) return memo[K];
  int res = 0;
  int a2 = i+2<N ? A[i+2] : 0;
  for (int k=0; k<=min(a0,a1); ++k) {
    res += dp(a1-k,a2+k,i+1);
    if (res>=P) res -= P;
  }
  memo[K] = res;
  return res;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d",&N);
    A.resize(N);
    for (int i=0; i<N; ++i) scanf("%d",&A[i]);
    printf("%d\n",dp(A[0],N>1?A[1]:0));
    // cleaning
    memo.clear();
  }
  return 0;
}
