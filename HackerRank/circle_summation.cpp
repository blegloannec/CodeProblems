#include <iostream>
#include <vector>
using namespace std;

typedef long long scal;
typedef vector< vector<scal> > matrice;

const scal P = 1000000007;

struct Matrice {
  int m,n;
  matrice M;
  
  Matrice(matrice &M0) {
    M = M0; // attention, pas de copie profonde
    m = M.size();
    n = M[0].size();
  }

  Matrice(int m, int n) : m(m), n(n) {
    M.resize(m);
    for (int i=0; i<m; ++i) M[i].resize(n,0);
  }

  static Matrice id(int n) {
    Matrice I(n,n);
    for (int i=0; i<n; ++i) I.M[i][i] = 1;
    return I;
  }

  vector<scal> &operator[](int i) {
    return M[i];
  }
  
  Matrice operator*(const Matrice &A) const {
    //assert(n==A.m);
    Matrice C(m,A.n);
    for (int i=0; i<m; ++i)
      for (int k=0; k<n; ++k)
	for (int j=0; j<A.n; ++j) {
	  C.M[i][j] += (M[i][k] * A.M[k][j]) % P;
	  C.M[i][j] = ((C.M[i][j])%P + P) % P;
	}
    return C;
  }
  
  Matrice copy() const {
    matrice M0(n);
    for (int i=0; i<n; ++i) M0[i] = M[i]; // copy
    return Matrice(M0);
  }
  
  Matrice pow(int b) const {
    //assert(m==n);
    Matrice result = id(n);
    Matrice A = copy();
    while (b) {
      if (b&1) result = result*A;
      A = A*A;
      b >>= 1;
    }
    return result;
  }
};

// matrice correspondant a un tour complet de taille n partant de 0
Matrice game(int n) {
  Matrice M(n,n);
  M[0][0] = M[0][n-1] = M[0][1] = 1;
  for (int i=1; i<n; ++i) {
    M[i] = M[(i-1+n)%n];
    ++M[i][i];
    ++M[i][(i+1)%n];
  }
  // contrairement aux i<n-1, i=n-1 ferme la boucle et
  // prend donc la nouvelle valeur de 0, pas l'ancienne
  ++M[n-1][n-1];
  ++M[n-1][1];
  return M;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n,m;
    cin >> n >> m;
    vector<scal> A(n);
    for (int i=0; i<n; ++i) cin >> A[i];
    // matrice du jeu pour m/n tours complets, O(n^3 log m)
    Matrice M = game(n).pow(m/n);
    int r = m%n;  // etapes restantes
    // boucle de calcul en O(n^3)
    for (int i0=0; i0<n; ++i0) {
      // produit R = M*A en O(n^2) avec decalage de i0 dans R et A
      vector<scal> R(n,0);
      for (int i=0; i<n; ++i)
	for (int j=0; j<n; ++j)
	  R[(i0+i)%n] = (R[(i0+i)%n] + M[i][j]*A[(i0+j)%n]) % P;
      // etapes restantes realisees "a la main" en O(n)
      for (int k=0; k<r; ++k)
	R[(i0+k)%n] = (R[(i0+k)%n] + R[(i0+k-1+n)%n] + R[(i0+k+1)%n]) % P;
      // affichage
      for (int k=0; k<n; ++k) cout << R[k] << (k==n-1 ? '\n' : ' ');
    }
    if (t>0) cout << endl;
  }
  return 0;
}
