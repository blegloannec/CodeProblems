#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

typedef ll scal;
typedef vector< vector<scal> > matrice;

const ll MOD = 1000000000;

int N, S;
matrice M;
vector<char> X;
/*
  Codes:
   0  empty square
   1  1x1
   2  2x1 vertical domino
   3  1x2 horizontal domino to the left (previous state)
   4  1x2 horizontal domino to the right (next state)
*/
void backtrack(const int s0, int k=0) {
  if (k==0)  // init. X
    for (int i=0; i<N; ++i)
      X[i] = ((s0>>i)&1) ? 3 : 0;
  if (k==N) {  // end
    int s1 = 0;
    for (int i=0; i<N; ++i)
      if (X[i]==4) s1 |= 1<<i;
    ++M[s0][s1];
  }
  else if (X[k]!=0)
    backtrack(s0, k+1);
  else {  // setting X[k]
    {
      X[k] = 1;
      backtrack(s0, k+1);
      X[k] = 0;
    }
    if (k+1<N && X[k+1]==0) {
      X[k] = X[k+1] = 2;
      backtrack(s0, k+1);
      X[k] = X[k+1] = 0;
    }
    {
      X[k] = 4;
      backtrack(s0, k+1);
      X[k] = 0;
    }
  }
}

void gen_matrix() {
  /*
    a state is a bitstring of size N representing the border between
    the last 2 columns (indicating horizontal blocks that cross)
  */
  S = 1<<N;
  M.resize(S, vector<scal>(S, 0));
  X.resize(N);
  for (int s0=0; s0<S; ++s0)
    backtrack(s0);
}


struct Matrice {
  int m,n;
  matrice M;
  
  Matrice(matrice &M0) {
    M = M0; // attention, pas de copie profonde
    m = M.size();
    n = M[0].size();
  }
  
  Matrice(int m, int n, scal x=0) : m(m), n(n) {
    M.resize(m);
    for (int i=0; i<m; ++i) M[i].resize(n,x);
  }
  
  static Matrice id(int n) {
    Matrice M(n,n);
    for (int i=0; i<n; ++i) M[i][i] = 1;
    return M;
  }
  
  vector<scal> &operator[](int i) {
    return M[i];
  }
  
  const vector<scal> &operator[](int i) const {
    return M[i];
  }
  
  Matrice operator*(const Matrice &A) const {
    //assert(n==A.m);
    Matrice C(m,A.n);
    for (int i=0; i<m; ++i)
      for (int k=0; k<n; ++k)
	for (int j=0; j<A.n; ++j) {
	  C[i][j] += (M[i][k] * A[k][j]) % MOD;
	  if (C[i][j]>=MOD) C[i][j] -= MOD;
	}
    return C;
  }
  
  Matrice copy() const {
    Matrice C(m,n);
    for (int i=0; i<n; ++i) C[i] = M[i]; // copy
    return C;
  }
  
  Matrice pow(long long b) const {
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


int main() {
  cin >> N;
  ll m;
  cin >> m;
  gen_matrix();
  Matrice X(M);
  X = X.pow(m);
  cout << X[0][0] << endl;
  return 0;
}
