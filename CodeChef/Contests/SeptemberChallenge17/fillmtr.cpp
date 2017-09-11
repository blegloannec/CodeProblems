#include <cstdio>
#include <vector>
#include <unordered_map>
using namespace std;

/*
  Un 0 dans la matrice signifie que 2 indices du tableau portent des
  valeurs egales. On commence par traiter les 0 avec de l'union-find
  pour former les classes d'indices portant des valeurs egales.
  Un 1 dans la matrice signifie que les 2 indices portent des valeurs
  qui different de +/-1. On contruit un graphe dont les sommets sont les
  classes issues des 0 et les aretes correspondent aux 1 de la matrice
  et relient 2 classes dont les valeurs different de +/-1.
  Une CN evidente est que le graphe ne contienne pas de cycle impair car tout
  cycle doit contenir autant de 1 que de -1 pour revenir a la valeur initiale.
  pas de cycle impair <=> 2-coloriable <=> biparti
  C'est clairement une CNS car si le graphe est biparti, choisir une
  valeur arbitraire pour l'une des deux composantes et cette valeur +/-1 pour
  l'autre produit une affectation valide.
  Il suffit donc de verifier par un simple parcours que le graphe est
  2-coloriable.
*/

int n,N;
unordered_map<int,int> Num;
vector<int> Tarj;
vector< pair<int,int> > R;
vector< vector<int> > G;
vector<int> C;

int find(int x) {
  if (Tarj[x]<0) return x;
  Tarj[x] = find(Tarj[x]);
  return Tarj[x];
}

void uni(int x, int y) {
  int x0 = find(x), y0 = find(y);
  Tarj[y0] = x0;
}

bool build_graph() {
  G.resize(N);
  for (unsigned int r=0; r<R.size(); ++r) {
    int i = find(R[r].first), j = find(R[r].second);
    if (i==j) return false;
    // on aura potentiellement des aretes en double, pas grave
    G[i].push_back(j);
    G[j].push_back(i);
  }
  return true;
}

bool dfs_color2(int u) {
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv) {
    if (C[*iv]<0) {
      C[*iv] = 1-C[u];
      if (!dfs_color2(*iv)) return false;
    }
    else if (C[*iv]==C[u]) return false;
  }
  return true;
}

bool color2() {
  C.resize(N,-1);
  for (int i=0; i<N; ++i)
    if (find(i)==i && C[i]<0) {
      C[i] = 0;
      if (!dfs_color2(i)) return false;
    }
  return true;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int Q;
    scanf("%d %d",&n,&Q);
    N = 0;
    for (int q=0; q<Q; ++q) {
      int i,j,val;
      scanf("%d %d %d",&i,&j,&val);
      if (Num.find(i)==Num.end()) {
	Num[i] = N++;
	Tarj.push_back(-1);
      }
      if (Num.find(j)==Num.end()) {
	Num[j] = N++;
	Tarj.push_back(-1);
      }
      i = Num[i]; j = Num[j];
      if (val==1) R.push_back(make_pair(i,j));
      else if (find(i)!=find(j)) uni(i,j);
    }
    if (build_graph() && color2()) printf("yes\n");
    else printf("no\n");
    // cleaning
    Num.clear();
    Tarj.clear();
    R.clear();
    G.clear();
    C.clear();
  }
  return 0;
}
