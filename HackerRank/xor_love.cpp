/*
  O(N + Q log B) computing the sum by computing it over each bit of the
  numbers (and multiplying by the associated power of 2).
  To compute the sum over 1 bit, we only need to know the count of 0s and 1s
  over the interval and the value of the corresponding bit of K.
*/
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

const ll MOD = 1000000007;
const int B = 21;

int N;
vector<int> BitCnt[B];

ll query(int K, int P, int R) {
  if (P==R) return 0;
  ll res = 0, p2 = 1;
  for (int b=0; b<B; ++b) {
    ll cnt1 = BitCnt[b][R] - (P==0 ? 0 : BitCnt[b][P-1]);
    ll cnt0 = R-P+1 - cnt1;
    ll cnt;
    if (((K>>b)&1)==0) cnt = cnt0*cnt1;
    else cnt = (cnt0*(cnt0-1))/2 + (cnt1*(cnt1-1))/2;
    cnt %= MOD;
    res += (cnt*p2) % MOD;
    res %= MOD;
    p2 <<= 1;
  }
  return res;
}

int main() {
  cin >> N;
  for (int b=0; b<B; ++b) {
    BitCnt[b].resize(N+1);
    BitCnt[b][0] = 0;
  }
  for (int i=1; i<=N; ++i) {
    int a;
    cin >> a;
    for (int b=0; b<B; ++b)
      BitCnt[b][i] = BitCnt[b][i-1] + ((a>>b)&1);
  }
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    int K,P,R;
    cin >> K >> P >> R;
    cout << query(K,P,R) << '\n';
  }
  return 0;
}
