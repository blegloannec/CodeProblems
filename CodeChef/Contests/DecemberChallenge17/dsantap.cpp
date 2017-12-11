#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

typedef vector< vector< pair<double,int> > > vdist;

const int NMAX = 500;
int N,G,B,X0,Y0;
vector<int> P;
int X[NMAX+1],Y[NMAX+1],K[NMAX+1],L[NMAX+1];
int O[NMAX];
double Dist[NMAX+1][NMAX+1];
int pos;
double score,best_score;
vector< pair<int,int> > sol,best_sol;
vdist Dist2(NMAX+1),Dist3(NMAX+1);
vector<int> Cpt;

double dist(int i, int j) {
  int dx = X[j]-X[i], dy = Y[j]-Y[i];
  return sqrt(dx*dx+dy*dy);
}

void comm(int c, int i) {
  sol.push_back(make_pair(c,i));
}

void go(int i) {
  comm(1,i);
  score += Dist[pos][i];
  pos = i;
}

void pick(int i) {
  comm(2,i);
  ++Cpt[i];
}

void drop(int i) {
  comm(3,i);
  --Cpt[i];
}

void bfs(vdist &Dist2, int S) {
  vector<bool> seen(N+1,false);
  int u = 0;
  for (int i=0; i<N; ++i) {
    seen[u] = true;
    vector<int> V;
    int iv = 0;
    while (iv<N && (int)V.size()<S) {
      int v = Dist2[u][iv].second;
      if (!seen[v]) V.push_back(v);
      ++iv;
    }
    u = V[rand() % V.size()];
    O[i] = u;
  }
}

void route(vdist& Dist2, int S) {
  score = 0.;
  sol.clear();
  bfs(Dist2,S);
  pos = 0;
  int p = 0;
  while (p<N) {
    int wl = P[K[O[p]]];
    int w = max(P[L[O[p]]],wl);
    int j = 1;
    fill(Cpt.begin(),Cpt.end(),0);
    ++Cpt[K[O[p]]];
    vector<bool> Picks(1,true);
    while (p+j<N) {
      if (Cpt[L[O[p+j]]]>0) {
	wl += P[K[O[p+j]]] - P[L[O[p+j]]];
	w = max(w,wl);
	Picks.push_back(false);
	--Cpt[L[O[p+j]]];
	++Cpt[K[O[p+j]]];
      }
      else {
	wl += P[K[O[p+j]]];
	w = max(w+P[L[O[p+j]]],wl);
	Picks.push_back(true);
	++Cpt[K[O[p+j]]];
      }
      if (w>B) break;
      ++j;
    }
    fill(Cpt.begin(),Cpt.end(),0);
    for (int i=0; i<j; ++i)
      if (Picks[i]) pick(L[O[p+i]]);
    for (int i=0; i<j; ++i) {
      go(O[p+i]);
      drop(L[O[p+i]]);
      pick(K[O[p+i]]);
    }
    go(0);
    for (int i=1; i<=G; ++i)
      while (Cpt[i]>0) drop(i);
    p += j;
  }
  if (score<best_score) {
    best_score = score;
    best_sol = sol;
  }
}

int main() {
  srand(42);
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d %d %d %d %d",&N,&G,&B,&X0,&Y0);
    P.resize(G+1);
    Cpt.resize(G+1);
    for (int i=1; i<=G; ++i) scanf("%d",&P[i]);
    X[0] = X0; Y[0] = Y0;
    for (int i=1; i<=N; ++i)
      scanf("%d %d %d %d",&X[i],&Y[i],&K[i],&L[i]);
    for (int u=0; u<=N; ++u) {
      Dist2[u].clear();
      Dist3[u].clear();
      for (int v=0; v<=N; ++v)
	if (u!=v) {
	  Dist[u][v] = dist(u,v);
	  double d = Dist[u][v];
	  Dist2[u].push_back(make_pair(d,v));
	  if (u>0 && v>0 && L[v]==K[u]) d /= 3.5;
	  Dist3[u].push_back(make_pair(d,v));
	}
      sort(Dist2[u].begin(),Dist2[u].end());
      sort(Dist3[u].begin(),Dist3[u].end());
    }
    best_score = 1e30;
    for (int i=0; i<5000; ++i) route(Dist2,2);
    for (int i=0; i<2500; ++i) route(Dist3,2);
    for (int i=0; i<2500; ++i) route(Dist3,3);
    for (auto it=best_sol.begin(); it!=best_sol.end(); ++it)
      printf("%d %d\n",it->first,it->second);
    printf("0\n");
  }
  return 0;
}
