#include <cstdio>
#include <vector>
using namespace std;

typedef int elem;

// modified lazy segment tree
struct FlipSegmentTree {
  const elem NEUTRAL = 0; // neutre
  unsigned int N;
  vector<elem> S;
  vector<bool> L0; // L0[p] ssi flip non propage dans l'intervalle de p

  FlipSegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    L0.resize(N,false);
    // les feuilles sont les elements >=N
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    // les noeuds internes sont les elements de 1 a N-1
    for (int p=N-1; p>0; --p) S[p] = S[2*p] + S[2*p+1];
  }

  void propagate(int p, int span) {
    //assert(p<(int)N && L0[p]);
    S[2*p] = span/2 - S[2*p];
    S[2*p+1] = span/2 - S[2*p+1];
    if (2*p<(int)N) {
      L0[2*p] = !L0[2*p];
      L0[2*p+1] = !L0[2*p+1];
    }
    L0[p] = false;
  }

  void _lazy_flip_range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return;
    else if (i<=start && start+span<=j) {
      S[p] = span - S[p];
      if (p<(int)N) L0[p] = !L0[p];
    }
    else {
      if (p<(int)N && L0[p]) propagate(p,span);
      _lazy_flip_range(2*p,start,span/2,i,j);
      _lazy_flip_range(2*p+1,start+span/2,span/2,i,j);
      S[p] = S[2*p] + S[2*p+1];
    }
  }
  
  void flip_range(int i, int j) {
    _lazy_flip_range(1,0,N,i,j+1);
  }

  // returns the sum in t in the indexes [i,j) intersected
  // with [start,start+span)
  elem _range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    if (p<(int)N && L0[p]) propagate(p,span);
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return left+right;
  }
  
  // returns sum{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) {
    return _range(1,0,N,i,j+1);
  }
};

int main() {
  int N,Q,c,r,l;
  scanf("%d %d",&N,&Q);
  vector<elem> T(N,0);
  FlipSegmentTree FST(T);
  for (int q=0; q<Q; ++q) {
    scanf("%d %d %d",&c,&l,&r);
    if (c==0) FST.flip_range(l,r);
    else printf("%d\n",FST.range(l,r));
  }
  return 0;
}
