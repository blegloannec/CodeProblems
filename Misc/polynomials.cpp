/*
  (Modular) Polynomials
  Berlekamp's algorithm for factorization over a finite field
*/

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// GLOBAL MODULUS
const int M = 13; // prime


// ===== Basic modular stuff ===== //
int bezout(int a, int b, int &u, int &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  int u1,v1;
  int g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

int inv_mod(int a, int n) {
  int u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}


// ===== Polynomials ===== //
typedef vector<int> coeffs;
typedef vector< vector<int> > matrix;
struct Poly;
typedef vector< pair<Poly,int> > factors;

void matrix_print(const matrix &A) {
  for (int i=0; i<(int)A.size(); ++i) {
    for (int j=0; j<(int)A[i].size(); ++j)
      cout << A[i][j] << ' ';
    cout << endl;
  }
}

struct Poly {
  coeffs C;
  Poly() {} // zero constructor
  Poly(int a, int d=0) { // monomial constructor
    if (a!=0) {
      C.resize(d+1,0);
      C[d] = a;
    }
  }
  Poly(const coeffs &C0) {
    C = C0; // well, let's copy for now
    reduce();
  }
  Poly(const Poly &A) { // copy constructor
    C = A.C; // copy
  }
  inline int deg() const;
  inline void reduce();
  void print() const;
  //Poly& operator=(const Poly &B);
  int& operator[](const int i);
  const int& operator[](const int i) const;
  Poly& operator+=(const Poly &B);
  Poly& operator-=(const Poly &B);
  Poly operator+(const Poly &B) const;
  Poly operator-(const Poly &B) const;
  Poly operator*(const Poly &B) const;
  Poly operator/(const Poly &B) const;
  Poly operator%(const Poly &B) const;
  Poly D() const;
  Poly rootM() const;
  Poly exp(const int i) const;
  inline bool is_unit() const;
  inline int dom() const;
  Poly monic() const;
  static Poly gcd(const Poly &A, const Poly &B);
  void square_free_factorization(factors &F, int b) const;
  static matrix null_space(matrix &A);
  vector<Poly> berlekamp() const;
  factors factorization() const;
};

int Poly::deg() const {
  // -1 pour -inf
  //if (C.size()>0) assert(C[C.size()-1]!=0);
  return C.size()-1;
}

void Poly::reduce() {
  while (C.size()>0 && C[C.size()-1]==0) C.pop_back();
}

void Poly::print() const {
  if (C.size()==0) cout << 0;
  else
    for (int i=0; i<(int)C.size(); ++i)
      cout << C[i] << ' ';
  cout << endl;
}

/* the default operator does the same
Poly& Poly::operator=(const Poly &B) {
  if (this!=&B) C = B.C; // copy
  return *this;
}
*/

int& Poly::operator[](const int i) {
  return C[i];
}

const int& Poly::operator[](const int i) const {
  return C[i];
}

Poly& Poly::operator+=(const Poly &B) {
  if (deg()<B.deg())
    C.resize(B.deg()+1);
  for (int i=0; i<=B.deg(); ++i)
    C[i] = (C[i]+B[i])%M;
  reduce();
  return *this;
}

Poly Poly::operator+(const Poly &B) const {
  Poly S(C);
  S += B;
  return S;
}

Poly& Poly::operator-=(const Poly &B) {
  if (deg()<B.deg())
    C.resize(B.deg()+1);
  for (int i=0; i<=B.deg(); ++i)
    C[i] = (C[i]-B[i]+M)%M;
  reduce();
  return *this;
}

Poly Poly::operator-(const Poly &B) const {
  Poly S(C);
  S += B;
  return S;
}

// naive * in O(n^2) (not FFT in O(n log n))
Poly Poly::operator*(const Poly &B) const {
  Poly S;
  S.C.resize(deg()+B.deg()+1,0);
  for (int a=0; a<=deg(); ++a)
    for (int b=0; b<=B.deg(); ++b)
      S[a+b] = (S[a+b]+C[a]*B[b])%M;
  S.reduce();
  return S;
}

Poly Poly::operator/(const Poly &B) const {
  assert(B.deg()>=0);
  Poly R(C),Q;
  while (R.deg()>=B.deg()) {
    /*
      Poly T((R.dom()*inv_mod(B.dom(),M))%M,R.deg()-B.deg());
      R -= T*B;
      Q += T;
    */
    int x = (R.dom()*inv_mod(B.dom(),M))%M;
    int d = R.deg()-B.deg();
    if (Q.deg()<d) Q.C.resize(d+1,0);
    Q[d] = x;
    for (int i=0; i<=B.deg(); ++i)
      R[d+i] = (R[d+i] - (x*B[i])%M + M)%M;
    R.reduce();
  }
  return Q;
}

Poly Poly::operator%(const Poly &B) const {
  assert(B.deg()>=0);
  Poly R(C);
  while (R.deg()>=B.deg()) {
    int x = (R.dom()*inv_mod(B.dom(),M))%M;
    int d = R.deg()-B.deg();
    for (int i=0; i<=B.deg(); ++i)
      R[d+i] = (R[d+i] - (x*B[i])%M + M)%M;
    R.reduce();
  }
  return R;
}

// derivative
Poly Poly::D() const {
  Poly Q;
  for (int i=1; i<=deg(); ++i)
    Q += Poly((C[i]*i)%M,i-1);
  Q.reduce();
  return Q;
}

// compute R such that R^M = *this
// x -> x^M is Frobenius morphism
// Warning: the only non-zero coefficients of *this
//          must be of a multiple of M degree
Poly Poly::rootM() const {
  // sanity check
  /*for (int i=0; i<=deg(); ++i)
    assert(i%M==0 || C[i]==0);*/
  Poly R;
  for (int i=0; i<=deg(); i += M)
    R.C.push_back(C[i]);
  return R;
}

Poly Poly::exp(const int i) const {
  if (i==0) return Poly(1);
  else if (i%2==0) return ((*this)*(*this)).exp(i/2);
  else return (*this)*((*this)*(*this)).exp((i-1)/2);
}

bool Poly::is_unit() const {
  return (deg()==0 && C[0]==1);
}

int Poly::dom() const {
  if (deg()<0) return 0;
  else return C[deg()];
}

// returns a monic polynomial from *this
Poly Poly::monic() const {
  //assert(deg()>=0);
  return C[deg()]==1 ? *this : (*this)*Poly(inv_mod(dom(),M));
}

Poly Poly::gcd(const Poly &A, const Poly &B) {
  if (B.deg()<0) return A.monic();
  else return gcd(B,A%B);
}

// Berlekamp factorization
// Ref.: Knuth TAOCP 2 (p439)
// https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields
void Poly::square_free_factorization(factors &F, int b=1) const {
  // *this should be monic
  int i = 1;
  Poly g = this->D();
  if (g.deg()>=0) {
    Poly c = gcd(*this,g);
    Poly w = *this/c;
    while (!w.is_unit()) {
      Poly y = gcd(w,c);
      Poly z = w/y;
      if (!z.is_unit())
	F.push_back(make_pair(z,b*i));
      ++i;
      w = y;
      c = c/y;
    }
    if (!c.is_unit())
      c.rootM().square_free_factorization(F,b*M);
  }
  else this->rootM().square_free_factorization(F,b*M);
}

// triangularization
matrix Poly::null_space(matrix &A) {
  matrix B;
  int n = A.size();
  vector<int> C(n,-1);
  //int r = 0;  // kernel dimension
  for (int k=0; k<n; ++k) {
    int j = 0;
    while (j<n && !(A[k][j]!=0 && C[j]<0)) ++j;
    if (j<n) {
      int a = (M-inv_mod(A[k][j],M))%M;
      for (int l=k; l<n; ++l) A[l][j] = (A[l][j]*a)%M;
      for (int i=0; i<n; ++i)
	if (i!=j) {
	  a = A[k][i];
	  for (int l=k; l<n; ++l)
	    A[l][i] = (A[l][i] + a*A[l][j])%M;
	}
      C[j] = k;
    }
    else {
      vector<int> V(n,0);
      V[k] = 1;
      for (int s=0; s<n; ++s)
	if (C[s]>=0) V[C[s]] = A[k][s];
      B.push_back(V);
      //++r;
    }
  }
  // matrix rank is n-r = n-B.size()
  return B;
}

vector<Poly> Poly::berlekamp() const {
  // *this should be squarefree
  int d = this->deg();
  matrix A;
  /* Inefficient matrix computation
  for (int k=0; k<d; ++k) {
    A.push_back((Poly(1,k*M)%P).C);
    if ((int)A[k].size()<d) A[k].resize(d,0);
    A[k][k] = (A[k][k]-1+M)%M;
  }*/
  // Efficient version
  vector<int> L(d,0);
  A.push_back(L);
  L[0] = 1;
  for (int k=1; k<=(d-1)*M; ++k) {
    int t = L[d-1];
    for (int i=d-1; i>0; --i)
      L[i] = (L[i-1]-t*(*this)[i]+M*M)%M;
    L[0] = (M*M-t*(*this)[0])%M;
    if (k%M==0) {
      A.push_back(L);
      A[k/M][k/M] = (A[k/M][k/M]-1+M)%M;
    }
  }
  matrix B = null_space(A);
  int r = B.size(); // kernel dimension
  int k = 1;
  vector<Poly> F;
  F.push_back(*this);
  while ((int)F.size()<r) {
    vector<Poly> F0;
    Poly Q(B[k]);
    for (vector<Poly>::iterator it=F.begin(); it!=F.end(); ++it)
      for (int s=0; s<M; ++s) {
	Poly G = gcd(*it,Q-Poly(s));
	if (!G.is_unit())
	  F0.push_back(G);
      }
    F = F0;
    ++k;
  }
  return F;
}

factors Poly::factorization() const {
  factors SFF,F;
  this->square_free_factorization(SFF);
  for (factors::iterator it=SFF.begin(); it!=SFF.end(); ++it) {
    vector<Poly> V = (it->first).berlekamp();
    for (vector<Poly>::iterator jt=V.begin(); jt!=V.end(); ++jt)
      F.push_back(make_pair(*jt,it->second));
  }
  return F;
}
// ===== End of Polynomials ===== //


// ===== MAIN ===== //
int main() {
  coeffs A = {8,2,8,10,10,0,1,0,1};
  Poly P(A);
  factors F = P.factorization();
  for (factors::iterator it=F.begin(); it!=F.end(); ++it) {
    (it->first).print();        // factor
    cout << it->second << endl; // power
  }
  return 0;
}
