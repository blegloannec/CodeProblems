#include <cstdio>
#include <vector>
#include <queue>
//#include <cassert>
using namespace std;

/*
  En chaque sommet u du cycle sont enracinees des chaines, un nouveau sommet
  dans les chaines de u est toujours ajoute soit en u, soit sur le sommet le
  plus profond et recent (au bout d'une plus longue chaine). Inutile de
  maintenir la structure des chaines, il suffit de maintenir un tas-max Q[u]
  contenant les sommets des chaines tries par (distance a u, temps d'insertion).
  On maintient par ailleurs un max segment tree ST tel que ST[u] contient
  le couple (dist(0,racine(Q[u])), temps_insertion(racine(Q[u])))
  pour 0 le premier sommet du cycle.
  ST[u] identifie donc le sommet plus lointain de 0 parmi les chaines de u.
  Le sommet le plus lointain de u (sommet du cycle) est donc identifie par
  max( ST.range_max(0,u-1)+dist(u,0), ST.range_max(u,n-1)-dist(0,u) )
  --> O(log N) par requete
  (NB: l'edito propose une approche sqrt-decomp plus elementaire mais moins
       efficace)
*/

typedef long long ent;
typedef pair<ent,int> elem;  // (dist, vertex)

/* ===== BEGIN SegmentTree ===== */
struct SegmentTree {
  const elem NEUTRAL = make_pair(-1,-1); // neutre pour l'operation
  unsigned int N;
  vector<elem> S;

  // operation utilisee
  static elem op(const elem &a, const elem &b) {
    return max(a,b);
  }

  SegmentTree() {}
  SegmentTree(const vector<elem> &T) {
    init(T);
  }

  void init(const vector<elem> &T);

  elem get(int i) const {
    return S[N+i];
  }

  void set(int i, const elem &v);

  elem _range(int p, int start, int span, int i, int j) const;
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
};

void SegmentTree::init(const vector<elem> &T) {
  N = 1;
  while (N<T.size()) N <<= 1;
  S.resize(2*N,NEUTRAL);
  for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
  for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
}

void SegmentTree::set(int i, const elem &v) {
  unsigned int p = N+i;
  S[p] = v;
  p >>= 1;
  while (p>0) {
    S[p] = op(S[2*p],S[2*p+1]);
    p >>= 1;
  }
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

int n;
vector<ent> DistFrom0;
vector< priority_queue<elem> > Q;
SegmentTree ST;
vector<int> Root;

elem farthest(int x) {
  auto res = ST.range(x,n-1);
  res.first -= DistFrom0[x];
  if (x>0) {
    auto bef = ST.range(0,x-1);
    bef.first += DistFrom0[n]-DistFrom0[x];
    res = max(res,bef);
  }
  //assert(Q[Root[res.second]].top().second==res.second);
  return res;
}

void updateST(int x) {
  //assert(!Q[x].empty());
  ST.set(x,make_pair(DistFrom0[x]+Q[x].top().first,Q[x].top().second));
}

int main() {
  scanf("%d",&n);
  DistFrom0.resize(n+1,0);
  for (int i=1; i<=n; ++i) {
    scanf("%lld",&DistFrom0[i]);
    DistFrom0[i] += DistFrom0[i-1];
  }
  vector<elem> T;
  for (int i=0; i<n; ++i) T.push_back(make_pair(DistFrom0[i],i));
  ST.init(T);
  int m;
  scanf("%d",&m);
  Q.resize(n);
  for (int i=0; i<n; ++i) Q[i].push(make_pair(0,i));
  Root.resize(n+m,-1);
  for (int i=0; i<n; ++i) Root[i] = i;
  for (int q=n; q<n+m; ++q) {
    int c,x;
    scanf("%d %d",&c,&x); --x;
    if (c==1) {
      ent w;
      scanf("%lld",&w);
      int ry = Root[farthest(x).second];
      Q[ry].push(make_pair(Q[ry].top().first+w,q));
      updateST(ry);
      Root[q] = ry;
    }
    else if (c==2) {
      ent w;
      scanf("%lld",&w);
      Q[x].push(make_pair(w,q));
      updateST(x);
      Root[q] = x;
    }
    else if (c==3) {
      int ry = Root[farthest(x).second];
      Q[ry].pop();
      updateST(ry);
    }
    else printf("%lld\n",farthest(x).first);
  }
  return 0;
}
