#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

// cf. eg. https://threads-iiith.quora.com/Centroid-Decomposition-of-a-Tree

// Arbre
int N;
vector< vector<int> > G;


// ===== CENTROID DECOMPOSITION =====
vector<int> STSize;       // utilise uniquement pour le calcul de la decomposition
vector<bool> centroided;  // idem

int CentroidRoot;                   // centroid racine
vector< vector<int> > CentroidG;    // graphe des centroids
vector<int> CentroidP,CentroidLvl;  // parent et profondeur d'un centroid

// Calcul des tailles des sous-arbres de l'arbre enracine en u
int centroid_size_dfs(int u, int u0=-1) {
  STSize[u] = 1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && !centroided[*iv]) STSize[u] += centroid_size_dfs(*iv,u);
  return STSize[u];
}

// Calcul du centroid de l'arbre de taille n contenant u
// (supposant les tailles des sous-arbres calculees)
int centroid(int n, int u, int u0=-1) {
  if (n==1) return u;
  int maxS = 0, maxv = -1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && !centroided[*iv] && STSize[*iv]>maxS) {
      maxS = STSize[*iv];
      maxv = *iv;
    }
  if (maxS<=n/2) return u;
  else return centroid(n,maxv,u);
}

// Calcul du centroid de l'arbre de niveau l contenant u
int centroidize(int u=0, int l=0) {
  int n = centroid_size_dfs(u);
  int c = centroid(n,u);
  centroided[c] = true;
  CentroidLvl[c] = l;
  for (auto iv=G[c].begin(); iv!=G[c].end(); ++iv)
    if (!centroided[*iv]) {
      int d = centroidize(*iv,l+1);
      CentroidP[d] = c;
      CentroidG[c].push_back(d);
    }
  return c;
}

// Fonction a appeler pour calculer la decomposition de G
void centroid_comp() {
  centroided.resize(N,false);
  STSize.resize(N);
  CentroidG.resize(N);
  CentroidP.resize(N,-1);
  CentroidLvl.resize(N,0);
  CentroidRoot = centroidize();
}
// =====  =====


// ===== EXEMPLE D'UTILISATION =====
// CentroidDist[u][l] = dist. de u a son centroid ancetre de niveau l <= CentroidLvl[u]
vector< vector<int> > CentroidDist;

// DFS dans l'arbre de centroid c
void dfs_centroid(vector<int> &Z, int c, int u, int u0=-1, int d=0) {
  CentroidDist[u][CentroidLvl[c]] = d;
  Z.push_back(u);
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    // un voisin v est dans l'arbre de centroid c ssi CentroidLvl[v]>CentroidLvl[c]
    if (*iv!=u0 && CentroidLvl[*iv]>CentroidLvl[c])
      dfs_centroid(Z,c,*iv,u,d+1);
}

void precomp_dfs(int c) {
  vector<int> Z;
  dfs_centroid(Z,c,c);
  for (auto it=CentroidG[c].begin(); it!=CentroidG[c].end(); ++it)
    precomp_dfs(*it);
}

void precomp() {
  CentroidDist.resize(N);
  for (int u=0; u<N; ++u) CentroidDist[u].resize(CentroidLvl[u]+1,0);
  precomp_dfs(CentroidRoot);
}


int main() {
  return 0;
}
