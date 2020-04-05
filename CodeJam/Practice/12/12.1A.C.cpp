#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define NMAX 50
#define GMAX (NMAX*NMAX)
#define L 5.0
#define INFINI 1E+30

struct Itvl { 
  /* type intervalle (de temps) de croisement des voitures va et vb
     va la voiture de reference */
  double debut,fin;
  int va,vb;
  char voiea;
  Itvl(double d, double f, int va, int vb) : debut(d), fin(f), va(va), vb(vb), voiea('X') {}
  Itvl(double d, double f, int va, int vb, char la) : debut(d), fin(f), va(va), vb(vb), voiea(la) {}
};

bool comp(Itvl I, Itvl J) {
  return (I.debut<J.debut);
}

int T,N,nb;
char C[NMAX];
int S[NMAX];
int P[NMAX];
vector<Itvl> itvls;
int G[GMAX][GMAX];
bool visite[GMAX];
char coul[GMAX];

void calcul_intersect() {
  /* calcule l'intervalle de temps de croisement de chaque paire de voitures
     on les trie par ordre croissant de debut */
  int va,vb;
  double deb,fin;
  itvls.clear();
  for (int v1=0; v1<N-1; ++v1)
    for (int v2=v1+1; v2<N; ++v2) {
      va = v1; vb = v2;
      if (S[v1]>S[v2]) {va = v2; vb = v1;}
      deb = -INFINI;
      fin = -INFINI;
      if (S[va]==S[vb]) {
	if (abs(P[va]-P[vb])<L) fin = INFINI;
      }
      else {
	deb = (P[va]-P[vb]-L)/(S[vb]-S[va]);
	fin = (P[va]+L-P[vb])/(S[vb]-S[va]);
      }
      if (fin>0) {
	if (deb<0) itvls.push_back(Itvl(deb,fin,va,vb,C[va]));
	else itvls.push_back(Itvl(deb,fin,va,vb));
      }
    }
  sort(itvls.begin(),itvls.end(),comp);
  nb = (int)itvls.size();
}

char inv(char voie) {return (voie=='R'?'L':'R');}

void graphe() {
  /* calcule le graphe d'intersection avec aretes 1
     entre 2 intervalles pour lesquels les voitures de reference
     doivent partager la meme voie et -1 si elles
   */
  int j;
  for (int i=0; i<nb; ++i)
    for (int j=0; j<nb; ++j)
      G[i][j] = 0;
  for (int i=0; i<nb-1; ++i) {
    j = i+1;
    while (j<nb && itvls[j].debut<itvls[i].fin) {
      if (itvls[i].va==itvls[j].va || itvls[i].vb==itvls[j].vb)
	{G[i][j] = 1; G[j][i] = 1;}
      else if (itvls[i].va==itvls[j].vb || itvls[i].vb==itvls[j].va)
	{G[i][j] = -1; G[j][i] = -1;}
      ++j;
    }
  }
}

bool colorie(int imax, int i) {
  if (!visite[i]) {
    visite[i] = true;
    if (coul[i]=='X') coul[i]='L';
    for (int j=0; j<=imax; ++j) {
      if (G[i][j]==1) {
	if (coul[j]=='X') {
	  coul[j] = coul[i];
	  if (!colorie(imax,j)) return false;
	}
	else if (coul[j]!=coul[i])
	  return false;
      }
      else if (G[i][j]==-1) {
	if (coul[j]=='X') {
	  coul[j] = inv(coul[i]);
	  if (!colorie(imax,j)) return false;
	}
	else if (coul[j]==coul[i])
	  return false;
      }
    }
  }
  return true;
}

bool coloration(int imax) {
  int i;
  bool test = true;
  for (int i=0; i<=imax; ++i) {
    visite[i] = false;
    coul[i] = itvls[i].voiea;
  }
  i = 0;
  while (i<=imax && test)
    test = colorie(imax,i++);
  return test;
}

int main() {
  int imax;
  int test;
  cin >> T;
  for (int c=1; c<=T; ++c) {
    cin >> N;
    for (int i=0; i<N; ++i)
      cin >> C[i] >> S[i] >> P[i];
    calcul_intersect();
    graphe();
    imax = 1;
    test = true;
    while (imax<nb && test)
      test = coloration(imax++);
    if (test)
      cout << "Case #" << c << ": Possible" << endl;
    else
      cout << "Case #" << c << ": " << max(0.0,itvls[imax-1].debut) << endl;
  }
  return 0;
}
