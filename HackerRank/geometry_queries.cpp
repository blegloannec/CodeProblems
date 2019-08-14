/*
  Sqrt-decomposition approach in O(sqrt(N) log sqrt(N)) per query.
  See also editorial https://www.hackerrank.com/challenges/geometry-queries/editorial
  and http://wcipeg.com/wiki/Convex_hull_trick
  NB: testcases are weak, naive approach in O(N) per query can pass.
*/
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
using ll = long long;

struct line {
  ll a,b;  // y = ax + b
  line(ll a, ll b) : a(a), b(b) {}
  bool operator<(const line &L) const {
    return a<L.a || (a==L.a && b>L.b);
  }
  bool under(ll x, ll y) const {
    return a*x+b>y;
  }
  double xinter(const line &L) const {
    assert(a!=L.a);
    return (L.b-b) / (double)(a-L.a);
  }
};

int N,BS,BC;
vector<line> Lines;
vector< vector<line> > Blines;
vector< vector<double> > Bx;

// precomp. the upper hull of the lines of the block
void block_upper_hull(int b) {
  int l = b*BS, r = min((b+1)*BS,N);
  vector<line> TmpL;
  for (int i=l; i<r; ++i) TmpL.push_back(Lines[i]);
  sort(TmpL.begin(), TmpL.end());
  Blines[b].push_back(TmpL[0]);
  for (int i=1; i<(int)TmpL.size(); ++i) {
    if (TmpL[i].a==TmpL[i-1].a) continue;
    while (!Bx[b].empty() && Blines[b].back().xinter(TmpL[i])<=Bx[b].back()) {
      Blines[b].pop_back();
      Bx[b].pop_back();
    }
    Bx[b].push_back(Blines[b].back().xinter(TmpL[i]));
    Blines[b].push_back(TmpL[i]);
  }
}

bool block_query(int b, ll x, ll y) {
  int i = distance(Bx[b].begin(), lower_bound(Bx[b].begin(), Bx[b].end(), (double)x));
  return Blines[b][i].under(x,y);
}

bool range_query(int L, int R, ll x, ll y) {
  for (int i=L; i<=R; ++i)
    if (Lines[i].under(x,y)) return true;
  return false;
}

bool query(int L, int R, ll x, ll y) {
  int bl = (L+BS-1)/BS, br = R/BS;
  for (int b=bl; b<br; ++b)
    if (block_query(b,x,y)) return true;
  return range_query(L,min(bl*BS-1,R),x,y) || range_query(max(L,br*BS),R,x,y);
}

int main() {
  scanf("%d", &N);
  BS = (int)sqrt(N)+1;  // blocks size
  BC = (N+BS-1)/BS;     // blocks count
  for (int i=0; i<N; ++i) {
    ll a,b;
    scanf("%lld %lld", &a, &b);
    Lines.push_back(line(a,b));
  }
  // block upper hulls precomp
  Blines.resize(BC);
  Bx.resize(BC);
  for (int b=0; b<BC; ++b) block_upper_hull(b);
  // queries
  int Q;
  scanf("%d", &Q);
  for (int i=0; i<Q; ++i) {
    int L,R; ll x,y;
    scanf("%d %d %lld %lld", &L, &R, &x, &y);
    --L; --R;
    printf(query(L,R,x,y) ? "YES\n" : "NO\n");
  }
  return 0;
}
