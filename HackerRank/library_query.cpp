/*
  O(Q log N log^2 M) approach with M ~ 10^3 based on 2D Fenwick tree
  (Q queries, log N log M for the Fenwick * log M for dicho search)
  NB: Could also be done through sqrt-decomposition, maintaining the sorted
      list of values of each block, and looking for the kth in a range of
      blocks combining the binary searches of a value in each block in
      O(sqrt(N) log(sqrt(N)) log M).
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;


/* == 2D Fenwick Trees == */
typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  ent range_sum(int i1, int i2) const;
  ent get(int i) const;
  
  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

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

ent Fenwick::range_sum(int i1, int i2) const {
  return prefix_sum(i2) - prefix_sum(i1-1);
}

ent Fenwick::get(int i) const {
  return range_sum(i,i);
}


struct Fenwick2D {
  vector<Fenwick> FT;

  void add(int i, int j, ent v);
  ent _prefix_sum(int i, int j1, int j2) const;
  ent range_sum(int i1, int j1, int i2, int j2) const;
  ent get(int i, int j) const;
  
  Fenwick2D(int ni, int nj) {
    FT.resize(ni+1, Fenwick(nj));
  }
};

void Fenwick2D::add(int i, int j, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i].add(j,v);
    i += i&-i;
  }
}

ent Fenwick2D::_prefix_sum(int i, int j1, int j2) const {
  ent s = 0;
  while (i>0) {
    s += FT[i].range_sum(j1,j2);
    i -= i&-i;
  }
  return s;
}

ent Fenwick2D::range_sum(int i1, int j1, int i2, int j2) const {
  return _prefix_sum(i2,j1,j2) - _prefix_sum(i1-1,j1,j2);
}

ent Fenwick2D::get(int i, int j) const {
  return range_sum(i,j,i,j);
}
/* ===== */


const int MAX = 1000;

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N,Q;
    cin >> N;
    vector<int> B(N+1);
    Fenwick2D F(N,MAX);
    for (int i=1; i<=N; ++i) {
      cin >> B[i];
      F.add(i,B[i],1);
    }
    cin >> Q;
    for (int i=0; i<Q; ++i) {
      int C;
      cin >> C;
      if (C==1) {
	int x,k;
	cin >> x >> k;
	F.add(x,B[x],-1);
	B[x] = k;
	F.add(x,k,1);
      }
      else {
	int x,y,k;
	cin >> x >> y >> k;
	int l = 1, r = MAX;
	while (l<r) {
	  int m = (l+r)/2;
	  if (F.range_sum(x,1,y,m)<k) l = m+1;
	  else r = m;
	}
	cout << l << endl;
      }
    }
  }
  return 0;
}
