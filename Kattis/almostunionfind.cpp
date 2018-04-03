#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

typedef long long ent;

int N;
vector<int> T,Nb;
vector<ent> Sum;

void init() {
  int M = 2*(N+1);
  T.resize(M);
  Nb.resize(M);
  Sum.resize(M);
  for (int i=0; i<=N; ++i) T[i] = i+N+1;
  for (int i=N+1; i<M; ++i) {
    /*
      Representants virtuels (>N), subissant les "redirections" de union,
      mais ne pouvant subir de move (sous peine de briser l'arbre).
      Les elements standard (<=N) sont ainsi toujours des feuilles
      et peuvent etre deplaces sans casser la structure.
      NB: espace non optimise ici, les cases <=N de Nb et Sum sont inutiles.
    */
    T[i] = i;
    Nb[i] = 1;
    Sum[i] = i-N-1;
  }
}

int find(int x) {
  if (T[x]!=x) T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) {
    T[y0] = x0;
    Nb[x0] += Nb[y0];
    Sum[x0] += Sum[y0];
  }
}

void move(int x, int y) {
  //assert(x<=N);
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) {
    --Nb[x0];
    Sum[x0] -= x;
    T[x] = y0;
    ++Nb[y0];
    Sum[y0] += x;
  }
}

int main() {
  int Q;
  while (scanf("%d %d",&N,&Q)==2) {
    init();
    for (int q=0; q<Q; ++q) {
      int c,a;
      scanf("%d %d",&c,&a);
      if (c==3) {
	int a0 = find(a);
	printf("%d %lld\n",Nb[a0],Sum[a0]);
      }
      else {
	int b;
	scanf("%d",&b);
	if (c==1) merge(a,b);
	else move(a,b);
      }
    }
  }
  return 0;
}
