#include <cstdio>
#include <vector>
using namespace std;

typedef pair<int,int> couple;

// modified lazy segment tree
struct Mod3SegmentTree {
  const couple NEUTRAL = couple(0,0); // neutre
  unsigned int N;
  // S contient les nbs d'elements = 0 et 1 mod 3
  vector<couple> S;
  vector<int> L;

  static inline couple cplus(const couple &a, const couple &b) {
    return couple(a.first+b.first,a.second+b.second);
  }
  
  Mod3SegmentTree(int t) {
    N = 1;
    while ((int)N<t) N <<= 1;
    S.resize(2*N,couple(1,0));
    L.resize(N,0); // lazy fields
    // les feuilles sont les elements >=N
    // les noeuds internes sont les elements de 1 a N-1
    for (int p=N-1; p>0; --p) S[p] = cplus(S[2*p],S[2*p+1]);
  }

  void _propagate(int p, int span) {
    // propagation de la lazy value de p,
    // mise a jour des valeurs des 2 fils
    if (L[p]==1) {
      S[2*p] = couple(span/2-S[2*p].first-S[2*p].second,S[2*p].first);
      S[2*p+1] = couple(span/2-S[2*p+1].first-S[2*p+1].second,S[2*p+1].first);
    }
    else { // L[p] == 2
      S[2*p] = couple(S[2*p].second,span/2-S[2*p].first-S[2*p].second);
      S[2*p+1] = couple(S[2*p+1].second,span/2-S[2*p+1].first-S[2*p+1].second);
    }
    if (2*p<(int)N) {
      // mise a jour des lazy values des 2 fils
      L[2*p] = (L[2*p]+L[p])%3;
      L[2*p+1] = (L[2*p+1]+L[p])%3;
    }
    L[p] = 0;
  }

  void _lazy_set_range(int p, int start, int span, int i, int j, int v) {
    if (start+span<=i || j<=start) return;
    else if (i<=start && start+span<=j) {
      // mise a jour des valeurs de p
      if (v==1)
	S[p] = couple(span-S[p].first-S[p].second,S[p].first);
      else // v==2
	S[p] = couple(S[p].second,span-S[p].first-S[p].second);
      if (p<(int)N) L[p] = (L[p]+v)%3;
    }
    else {
      if (p<(int)N && L[p]>0) _propagate(p,span);
      _lazy_set_range(2*p,start,span/2,i,j,v);
      _lazy_set_range(2*p+1,start+span/2,span/2,i,j,v);
      S[p] = cplus(S[2*p],S[2*p+1]);
    }
  }
  
  void range_add(int i, int j, int v=1) {
    v = (v%3+3)%3;
    if (v>0) _lazy_set_range(1,0,N,i,j+1,v);
  }

  // returns the op in t in the indexes [i,j) intersected
  // with [start,start+span)
  couple _range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    if (p<(int)N && L[p]>0) _propagate(p,span);
    couple left = _range(2*p,start,span/2,i,j);
    couple right = _range(2*p+1,start+span/2,span/2,i,j);
    return cplus(left,right);
  }
  
  // returns op{t[i], t[i+1], ..., t[j]}
  int range(int i, int j) {
    return _range(1,0,N,i,j+1).first;
  }
};

int main() {
  int N,Q,c,l,r;
  scanf("%d %d",&N,&Q);
  Mod3SegmentTree ST(N);
  for (int q=0; q<Q; ++q) {
    scanf("%d %d %d",&c,&l,&r);
    if (c==0) ST.range_add(l,r);
    else printf("%d\n",ST.range(l,r));
  }
  return 0;
}
