#include <iostream>
#include <vector>
#include <cassert>
#include <set>
using namespace std;

/*
  For "science", two methods implemented:
   - the first one uses a Fenwick tree as buckets for the current window of
     size k and dicho search to find medians
     O(n log^2 k)
   - the second one maintains 2 multisets (balanced BST) for the K/2 lowest
     and K/2 highest elements of the current window
     O(n log k)
  The second method is theoretically better but structurally heavier.
    first method runs in 5.5s with -O3
    second method runs in 10s with -O3
*/

typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

const int N = 10000000;
const int K = 100000;
const int M = 10007;

vector<int> P;
Fenwick FT(2*M);
vector<int> S(N+1);

ent expmod(ent x, ent n, ent m=M) {
  if (n==0) return 1;
  if (n%2==0) return expmod((x*x)%m,n/2,m);
  return (x*expmod((x*x)%m,(n-1)/2,m))%m;
}

void sieve_list(int N) {
  vector<bool> P0(N,true);
  for (int i=2; i<N; ++i)
    if (P0[i]) {
      P.push_back(i);
      for (int k=2*i; k<N; k+=i)
	P0[k] = false;
    }
}

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}

int lower_median() {
  int l = 0, r = 2*M;
  while (l<r) {
    int m = (l+r)/2;
    if (FT.prefix_sum(m)<K/2) l = m+1;
    else r = m;
  }
  return l;
}

int upper_median() {
  int l = 0, r = 2*M;
  while (r>l) {
    int m = (l+r+1)/2;
    if (K-FT.prefix_sum(m-1)<K/2) r = m-1;
    else l = m;
  }
  return r;
}

long long method0() {
  for (int i=1; i<=K; ++i) FT.add(S[i],1);
  long long res = lower_median()+upper_median();
  for (int i=K+1; i<=N; ++i) {
    FT.add(S[i],1);
    FT.add(S[i-K],-1);
    res += lower_median()+upper_median();
  }
  return res;
}

long long method1() {
  multiset<int> L,R;
  for (int i=1; i<=K; ++i) R.insert(S[i]);
  for (int i=0; i<K/2; ++i) {
    L.insert(*R.begin());
    R.erase(R.begin());
  }
  long long res = *L.rbegin() + *R.begin();
  for (int i=K+1; i<=N; ++i) {
    if (*R.begin()<=S[i]) R.insert(S[i]);
    else L.insert(S[i]);
    if (*R.begin()<=S[i-K]) R.erase(R.find(S[i-K]));
    else L.erase(L.find(S[i-K]));
    while (L.size()!=R.size()) { // O(1)
      if (L.size()<R.size()) {
	L.insert(*R.begin());
	R.erase(R.begin());
      }
      else {
	auto l = L.end(); --l;
	R.insert(*l);
	L.erase(l);
      }
    }
    res += *L.rbegin() + *R.begin();
  }
  return res;
}

int main() {
  sieve_list(18*N);
  for (int k=1; k<=N; ++k) S[k] = expmod(P[k-1]%M,k);
  for (int k=N; k>0; --k) S[k] += S[k/10000+1];
  long long res = method0();
  //long long res = method1();
  cout << res/2 << (res%2==0?".0":".5") << endl;
  return 0;
}
