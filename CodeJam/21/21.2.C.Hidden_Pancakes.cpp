/*
  Implemented this approach in Python during the contest...
  ...but got RE because of a really stupid beginner's mistake:
  the possibly too high (for Python) recursion depth of cnt()
  below...
*/
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;
using ll = long long;

const ll P = 1000000007LL;
const int NMAX = 100001;
vector<ll> Fact(NMAX, 1LL);

ll expmod(ll x, ll n) {
  if (!n) return 1LL;
  if (!(n&1)) return expmod((x*x)%P,n>>1);
  return (x*expmod((x*x)%P,n>>1))%P;
}

ll invmod(ll n) {
  return expmod(n, P-2LL);
}

ll binom(int n, int p) {
  assert(0<=p && p<=n);
  return (Fact[n]*invmod((Fact[p]*Fact[n-p])%P))%P;
}


/* ===== BEGIN SegmentTree ===== */
struct elem {
  int v,i;
  elem(int v=NMAX, int i=-1) : v(v), i(i) {}
  bool operator<(const elem &B) const {
    return (v<B.v || (v==B.v && i>B.i));
  }
};

struct SegmentTree {
  const elem NEUTRAL = elem(); // neutre pour l'operation
  unsigned int N = 0;
  vector<elem> S;

  // operation utilisee, ici min
  static elem op(const elem &a, const elem &b) {
    return min(a,b);
  }

  SegmentTree() {}

  void init(unsigned int n);
  void init(const vector<elem> &T);

  elem _range(int p, int start, int span, int i, int j) const;
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
};

void SegmentTree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  S.resize(2*N,NEUTRAL);
}

void SegmentTree::init(const vector<elem> &T) {
  init(T.size());
  for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
  for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
}

elem SegmentTree::_range(int p, int start, int span, int i, int j) const {
  // returns the minimum in t in the indexes [i,j) intersected
  // with [start,start+span)
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p];
  elem left = _range(2*p,start,span/2,i,j);
  elem right = _range(2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== END SegmentTree ===== */


int N;
vector<int> V;
SegmentTree RMQ;


/*
  Counts the number of orders to get [x-d for v in V[l:r]]
  as a valid visibility array.
*/
ll cnt(int l, int r, int d=0) {
  assert(l<=r);
  if (r-l==0) return 1LL;
  if (r-l==1) return V[l]-d==1 ? 1LL : 0LL;
  /*
    Look for the rightmost 1 in V[l:r]-d.
    This has to be the largest element's position,
    hence we can split there and treat separately
    the left part and the right part - 1 (since that
    element is always visible from the right).
  */
  elem vi = RMQ.range(l,r-1);
  if (vi.v-d!=1) return 0LL;
  int i = vi.i;
  ll cl = cnt(l,i, d);
  ll cr = cnt(i+1,r, d+1);
  return (binom(r-l-1, i-l) * ((cl * cr)%P)) % P;
}

int main() {
  // precomp. fact. mod.
  for (ll n=2; n<NMAX; ++n) Fact[n] = (n*Fact[n-1])%P;
  int T;
  scanf("%d", &T);
  for (int t=1; t<=T; ++t) {
    scanf("%d", &N);
    V.resize(N);
    vector<elem> V1;
    for (int i=0; i<N; ++i) {
      scanf("%d", &V[i]);
      V1.push_back(elem(V[i], i));
    }
    RMQ.init(V1);
    printf("Case #%d: %lld\n", t, cnt(0,N));
  }
  return 0;
}
