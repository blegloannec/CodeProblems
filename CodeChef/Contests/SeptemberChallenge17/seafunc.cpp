#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int OT = 100;
const int K = 3;

/*
  Methode simpliste (~40 pts)
  On ne considere ici que des segments de pentes -K a K.
  On utilise une prog. dyn. simple pour compter la taille maximale
  d'un segment de 1 de pente donnee demarrant en chaque point de
  la matrice (et se poursuivant vers le bas).
  On trie les segments par longueur et on les prend dans l'ordre
  jusqu'a ce qu'il reste moins de OT 1.
  On neglige ici les degres 2 ou 3, ainsi que la possibilite de renvoyer
  un 1 a un emplacement 0 de la matrice demandee (autrement dit l'ensemble
  de 1 produit est inclus dans l'ensemble demande, on ne s'autorise pas
  d'erreur dans l'autre sens).
*/

struct seg {
  int i,j,d,l;
  seg(int i, int j, int d, int l) : i(i), j(j), d(d), l(l) {}
  bool operator<(const seg &B) const {
    return (this->l < B.l || (this->l == B.l && abs(this->d)>abs(B.d)));
  }
};

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int N;
    scanf("%d",&N);
    vector< vector<bool> > A(N);
    int O = 0;
    for (int i=0; i<N; ++i) {
      A[i].resize(N);
      for (int j=0; j<N; ++j) {
	char c;
	scanf(" %c",&c);
	A[i][j] = (c=='1');
	if (A[i][j]) ++O;
      }
    }
    vector< vector< vector<int> > > P(2*K+1);
    vector<seg> S;
    for (int k=0; k<2*K+1; ++k) {
      P[k].resize(N);
      int d = k-K;
      for (int i=N-1; i>=0; --i) {
	P[k][i].resize(N,0);
	for (int j=0; j<N; ++j) {
	  if (A[i][j]) {
	    P[k][i][j] = 1;
	    if (i+1<N && 0<=j+d && j+d<N) P[k][i][j] += P[k][i+1][j+d];
	    S.push_back(seg(i,j,d,P[k][i][j]));
	  }
	}
      }
    }
    sort(S.begin(),S.end());
    O -= OT;
    int s = S.size()-1;
    vector< vector<int> > res;
    while (O>0) {
      int i = S[s].i, j = S[s].j, d = S[s].d, l = S[s].l;
      if (A[i][j]) {
	if (!(-N<=j+1-(i+1)*d && j+1-(i+1)*d<=N)) {
	  --s;
	  continue;
	}
	for (int k=0; k<l; ++k)
	  if (A[i+k][j+k*d]) {
	    A[i+k][j+k*d] = false;
	    --O;
	  }
	res.push_back({d,j+1-(i+1)*d,i+1,i+l});
      }
      --s;
    }
    printf("%d\n",(int)res.size());
    for (unsigned int i=0; i<res.size(); ++i)
      printf("0 1 0 1 %d 1 %d %d %d\n",res[i][0],res[i][1],res[i][2],res[i][3]);
  }
  return 0;
}
