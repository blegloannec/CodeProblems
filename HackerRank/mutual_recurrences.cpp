#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef long long scal;
typedef vector< vector<scal> > matrice;
const scal P = 1000000000;

struct Matrice {
  int m,n;
  matrice M;
  
  Matrice(matrice &M0) {
    M = M0; // attention, pas de copie profonde
    m = M.size();
    n = M[0].size();
  }
  
  static Matrice full(int m, int n, scal v) {
    matrice M0(m);
    for (int i=0; i<m; ++i) M0[i].resize(n,v);
    return Matrice(M0);
  }
  
  static Matrice zero(int m, int n) {
    return full(m,n,0);
  }
  
  static Matrice id(int n) {
    Matrice M = zero(n,n);
    for (int i=0; i<n; ++i) M.M[i][i] = 1;
    return M;
  }
  
  Matrice operator*(const Matrice &A) const {
    assert(n==A.m);
    Matrice C = zero(m,A.n);
    for (int i=0; i<m; ++i)
      for (int k=0; k<n; ++k)
	for (int j=0; j<A.n; ++j) {
	  C.M[i][j] += (M[i][k]*A.M[k][j]) % P;
	  if (C.M[i][j]>=P)  C.M[i][j] %= P;
	  else if (C.M[i][j]<0) C.M[i][j] = (C.M[i][j]%P) + P;
	}
    return C;
  }

  vector<scal> &operator[](int i) {
    return M[i];
  }
  
  Matrice copy() const {
    matrice M0(m);
    for (int i=0; i<m; ++i) {
      M0[i].resize(n);
      for (int j=0; j<n; ++j) M0[i][j] = M[i][j]; // copy
    }
    return Matrice(M0);
  }
  
  Matrice pow(long long b) const {
    assert(m==n);
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


int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int a,b,c,d,e,f,g,h;
    long long n;
    cin >> a >> b >> c >> d >> e >> f >> g >> h >> n;
    int xs = max(a,max(f,g));
    int ys = max(b,max(c,e));
    int S = xs+ys+4;
    // matrix
    Matrice M = Matrice::zero(S,S);
    // si u(n) = n*d^n alors u(n) = 2*d*u(n-1) - d^2*u(n-2)
    M[S-4][S-4] = 2*d;
    M[S-4][S-3] = -d*d;
    M[S-3][S-4] = 1;
    // idem pour v(n) = n*h^n
    M[S-2][S-2] = 2*h;
    M[S-2][S-1] = -h*h;
    M[S-1][S-2] = 1;
    // x(n) = x(n-a) + y(n-b) + y(n-c) + u(n)
    M[0][a-1] = M[0][xs+b-1] = M[0][S-4] = 1;
    M[0][xs+c-1] += 1;                         // b==c est possible
    for (int i=1; i<xs; ++i) M[i][i-1] = 1;
    // y(n) = y(n-e) + x(n-f) + y(n-g) + v(n)
    M[xs][xs+e-1] = M[xs][f-1] = M[xs][S-2] = 1;
    M[xs][g-1] += 1;                           // f==g est possible
    for (int i=xs+1; i<xs+ys; ++i) M[i][i-1] = 1;
    // init vector
    Matrice X = Matrice::full(S,1,1);
    X[0][0] = X[xs][0] = 3;
    X[S-4][0] = d;
    X[S-2][0] = h;
    X[S-3][0] = X[S-1][0] = 0;
    // solution
    Matrice X0 = M.pow(n) * X;
    cout << X0[0][0] << ' ' << X0[xs][0] << endl;
  }
  return 0;
}
