/*
  Offline sqrt-decomposition of the h-sorted sumos in O((N+Q) sqrt N log N)
  See also HackerRank/starfleet.cpp for a similar approach
*/
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

typedef long long ent;

int N, K, Q, S;
ent CurrPairs;
vector<int> H, Hsorted;


/* === Fenwick Trees === */
typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  ent range_sum(int i, int j) const;

  void init(int n) {
    FT.resize(n+1,0);
  }

  void clear() {
    fill(FT.begin(), FT.end(), 0);
  }
};

void Fenwick::add(int i, ent v=1) {
  ++i;
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ++i;
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

ent Fenwick::range_sum(int i, int j) const {
  assert(i<=j);
  return prefix_sum(j) - prefix_sum(i-1);
}
/* ===== */


Fenwick Counter;

struct sumo {
  int h, hi, li, ri;
  
  sumo(int h) : h(h) {
    hi = distance(Hsorted.begin(), lower_bound(Hsorted.begin(), Hsorted.end(), h));
    li = distance(Hsorted.begin(), lower_bound(Hsorted.begin(), Hsorted.end(), h-K));
    ri = distance(Hsorted.begin(), upper_bound(Hsorted.begin(), Hsorted.end(), h+K))-1;
  }
};

vector<sumo> Sumos;

struct query {
  int q, l, r, bl;
  ent res;
  
  query(int q, int l, int r) : q(q), l(l), r(r) {
    bl = l/S;  // initial block
  }
  
  bool operator<(const query &B) const {
    return bl<B.bl || (bl==B.bl && r<B.r);
  }
  
  void process() {
    /*
      Computing the result of the query in O(sqrt N log N)
      When this is called, Counter is assumed to already count the occurrences
      of the sumos h-values from block bl+1 to index r.
      Here we simply take into account the initial missing segment.
    */
    res = CurrPairs;
    if (r<(bl+1)*S) {
      for (int i=l; i<=r; ++i) {
	res += Counter.range_sum(Sumos[i].li, Sumos[i].ri);
	Counter.add(Sumos[i].hi);
      }
      for (int i=l; i<=r; ++i) Counter.add(Sumos[i].hi,-1);
    }
    else {
      for (int i=l; i<(bl+1)*S; ++i) {
	res += Counter.range_sum(Sumos[i].li, Sumos[i].ri);
	Counter.add(Sumos[i].hi);
      }
      for (int i=l; i<(bl+1)*S; ++i) Counter.add(Sumos[i].hi,-1);
    }
  }
};

vector<query> Queries;

void process_queries() {
  sort(Queries.begin(), Queries.end());
  int q = 0;
  for (int bl=0; bl<=N/S && q<Q; ++bl) {
    CurrPairs = 0;
    for (int r=bl*S; r<=N && q<Q && Queries[q].bl==bl; ++r) {
      if (r>=(bl+1)*S) {
	CurrPairs += Counter.range_sum(Sumos[r].li, Sumos[r].ri);
	Counter.add(Sumos[r].hi);
      }
      // processing queries starting in bl and ending at r
      while (q<Q && Queries[q].bl==bl && Queries[q].r==r) Queries[q++].process();
    }
    Counter.clear();
  }
}

int main() {
  scanf("%d %d", &N, &K);
  S = (int)sqrt(N)+1;
  H.resize(N);
  for (int i=0; i<N; ++i) scanf("%d", &H[i]);
  set<int> Hset(H.begin(),H.end());  // using aux. set to sort+unique
  Hsorted.assign(Hset.begin(), Hset.end());
  for (int i=0; i<N; ++i) Sumos.push_back(sumo(H[i]));
  scanf("%d", &Q);
  for (int q=0; q<Q; ++q) {
    int l,r;
    scanf("%d %d", &l, &r);
    Queries.push_back(query(q,l,r));
  }
  Counter.init(Hsorted.size());
  process_queries();
  vector<ent> Results(Q);
  for (int q=0; q<Q; ++q) Results[Queries[q].q] = Queries[q].res;
  for (int q=0; q<Q; ++q) printf("%lld\n", Results[q]);
  return 0;
}
