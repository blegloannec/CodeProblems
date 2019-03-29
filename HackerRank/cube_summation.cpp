/*
  As M ~ 10^3, this problem can naively be solved in O(M^2) by iterating
  and filtering through all the defined points at each request.
  However this was not the intended solution (M should have been ~ 10^5)
  and the problem can be solved in O(M log^3 N) using 3D Fenwick trees
  (i.e. Fenwick tree of (Fenwick tree of Fenwick tree)).
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef long long ent;


/* == 1D, 2D & 3D Fenwick Trees == */
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


struct Fenwick3D {
  vector<Fenwick2D> FT;

  void add(int i, int j, int k, ent v);
  ent _prefix_sum(int i, int j1, int k1, int j2, int k2) const;
  ent range_sum(int i1, int j1, int k1, int i2, int j2, int k2) const;
  ent get(int i, int j, int k) const;
  
  Fenwick3D(int ni, int nj, int nk) {
    FT.resize(ni+1, Fenwick2D(nj,nk));
  }
};

void Fenwick3D::add(int i, int j, int k, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i].add(j,k,v);
    i += i&-i;
  }
}

ent Fenwick3D::_prefix_sum(int i, int j1, int k1, int j2, int k2) const {
  ent s = 0;
  while (i>0) {
    s += FT[i].range_sum(j1,k1,j2,k2);
    i -= i&-i;
  }
  return s;
}

ent Fenwick3D::range_sum(int i1, int j1, int k1, int i2, int j2, int k2) const {
  return _prefix_sum(i2,j1,k1,j2,k2) - _prefix_sum(i1-1,j1,k1,j2,k2);
}

ent Fenwick3D::get(int i, int j, int k) const {
  return range_sum(i,j,k,i,j,k);
}
/* ===== */


int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N,M;
    cin >> N >> M;
    Fenwick3D F(N,N,N);
    for (int i=0; i<M; ++i) {
      string C;
      cin >> C;
      if (C=="UPDATE") {
	int x,y,z; ent v;
	cin >> x >> y >> z >> v;
	v -= F.get(x,y,z);
	F.add(x,y,z,v);
      }
      else {
	int x1,y1,z1,x2,y2,z2;
	cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
	cout << F.range_sum(x1,y1,z1,x2,y2,z2) << endl;
      }
    }
  }
  return 0;
}
