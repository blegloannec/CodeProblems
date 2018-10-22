#include <iostream>
#include <unordered_map>
using namespace std;

int A,B,C;
unordered_map<int,int> memo;

int dp(int a, int b, int i=0, int r=0) {
  if (C>>i==0) return a+b+r==0 ? 1 : 0;
  int K = a | (b<<5) | (i<<10) | (r<<15);
  if (memo.find(K)!=memo.end()) return memo[K];
  int c = (C>>i)&1;
  int res = 0;
  for (int x=0; x<=min(1,a); ++x)
    for (int y=0; y<=min(1,b); ++y) {
      int z = x+y+r;
      if ((z&1)==c) res += dp(a-x,b-y,i+1,z>>1);
    }
  memo[K] = res;
  return res;
}

int cnt1(int A) {
  int o = 0;
  while (A) {
    o += A&1;
    A >>= 1;
  }
  return o;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> A >> B >> C;
    cout << dp(cnt1(A),cnt1(B)) << endl;
    memo.clear();
  }
  return 0;
}
