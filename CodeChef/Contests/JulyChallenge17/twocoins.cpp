#include <cstdio>
#include <vector>
#include <unordered_map>
using namespace std;

// DP on a tree, slightly tricky on one case:
// if a vertex has one coin, but his dad and granddad have no coin,
// then taking a coin from a grandson should be considered
// but the trick is that if no son has a coin and there exists
// a grandson, then necessarily there exists a grandson that has a coin,
// so that case is actually "easy" because you don't actually have to check
// grandsons...

typedef long long ent;

int N;
vector< vector<int> > G;
const int inf = 5000000;
unordered_map<int,ent> memo;

int b2i(bool b) {
  return b ? 1 : 0;
}

int nbs(int u) {
  return G[u].size() - (u>0?1:0);
}

// d for dad and gd for granddad
ent dp(int u, int u0, bool me, bool d, bool gd) {
  int h = u | (b2i(me)<<25) | (b2i(d)<<26) | (b2i(gd)<<27);
  if (memo.find(h)!=memo.end()) return memo[h];
  ent res = 0;
  if (me) {
    // on a deja 1 + 1 avec d ou gd, pas de contrainte sur les fils
    int gs = 0;
    for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
      if (*iv!=u0) {
	res += min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
	gs += nbs(*iv);
      }
    if (!(d || gd) && gs==0) {
      if (nbs(u)<1) return inf;
      int mf = inf;
      for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
	if (*iv!=u0) {
	  int df = dp(*iv,u,true,me,d);
	  if (df<inf) df -= min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
	  mf = min(mf,df);
	}
      res += mf;
    }
  }
  // on a 0, gd est ignore, il nous faut d + 1 fils ou 2 fils
  else if (d) {
    // il nous faut 1 fils
    if (nbs(u)<1) return inf;
    int mf = inf;
    for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
      if (*iv!=u0) {
	int df = dp(*iv,u,true,me,d);
	if (df<inf) df -= min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
	mf = min(mf,df);
	res += min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
      }
    res += mf;
  }
  else {
    // il nous faut 2 fils
    if (nbs(u)<2) return inf;
    int mf1 = inf, mf2 = inf;
    for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
      if (*iv!=u0) {
	int df = dp(*iv,u,true,me,d);
	if (df<inf) df -= min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
	if (df<mf1) {
	  mf2 = mf1;
	  mf1 = df;
	}
	else if (df<mf2) mf2 = df;
	res += min(dp(*iv,u,false,me,d),dp(*iv,u,true,me,d));
      }
    res += mf1+mf2;
  }
  if (me) ++res;
  memo[h] = res;
  return res;
}
  
int main() {
  int T,u,v;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d",&N);
    G.resize(N);
    for (int i=0; i<N-1; ++i) {
      scanf("%d %d",&u,&v);
      --u; --v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    ent res = min(dp(0,-1,false,false,false),dp(0,-1,true,false,false));
    if (res>=inf) res = -1;
    printf("%lld\n",res);
    // cleaning
    G.clear();
    memo.clear();
  }
  return 0;
}
