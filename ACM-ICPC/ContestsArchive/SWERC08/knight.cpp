#include <cstdio>
#include <vector>
//#include <cassert>
using namespace std;

/*
  the tavern is a sink so that it is simpler to consider
  expectancies to reach the tavern
  E(u) = expected nb of steps from vertex u to the tavern
  E(u) = sum_(u->v) P(u->v)*(1+E(v))
  E(u) = 1 + sum_(u->v) P(u->v)*E(v)
  and E(tavern) = 0
*/

typedef double scal;
typedef vector<scal> vec;
typedef vector<vec> matrix;

int m,n,s;
matrix M;

int U(int i, int j) {
  return i*n+j;
}

void read_matrix(int di, int dj) {
  for (int i=0; i<m; ++i)
    for (int j=0; j<n; ++j) {
      double p;
      scanf("%lf",&p);
      if (p>0.) M[U(i,j)][U(i+di,j+dj)] = -p;
    }
}

bool parse_input() {
  scanf("%d %d",&m,&n);
  if (m==0) return false;
  s = m*n;
  M.resize(s);
  for (int i=0; i<s; ++i) {
    M[i].resize(s);
    for (int j=0; j<s; ++j)
      M[i][j] = (i==j ? 1. : 0.);
  }
  read_matrix(1,0);
  read_matrix(0,1);
  read_matrix(-1,0);
  read_matrix(0,-1);
  return true;
}


// linear system solver
/* // NOT USED in this particular case (see comment in system_solve())
const double EPS = 1e-7;
bool fzero(double x) {
  return (-EPS<x && x<EPS);
}

void l_swap(matrix &M, int i, int j) {
  for (int k=0; k<s; ++k) swap(M[i][k],M[j][k]);
}

int first_non_zero(matrix &M, int j) {
  for (int i=j; i<s; ++i)
    if (!fzero(M[i][j])) return i;
  return -1;
}
*/

// line operations optimized for block-width n
void sline_prod(scal a, matrix &M, int i) {
  //for (int j=i; j<s; ++j) M[i][j] *= a;
  for (int j=i; j<min(s,i+n+1); ++j) M[i][j] *= a;
}

void line_diff(scal a, matrix &M, int i, int j) {
  //for (int k=i; k<s; ++k) M[j][k] -= a*M[i][k];
  for (int k=i; k<min(s,i+n+1); ++k) M[j][k] -= a*M[i][k];
}

void system_solve(matrix &M, vec &B) {
  // triangularization in O(s*n^2) = O(m*n^3)
  for (int i=0; i<s; ++i) {
    /* // NOT USED as in this particular case we always have j0 = i
    int j0 = first_non_zero(M,i);
    assert(j0>=0);
    if (j0>i) {
      l_swap(M,i,j0);
      swap(B[i],B[j0]);
    }
    */
    scal a = 1./M[i][i];
    sline_prod(a,M,i);
    B[i] *= a;
    // loop optimized for block-width n
    for (int j=i+1; j<min(s,i+n+1); ++j) {
      scal a = M[j][i];
      line_diff(a,M,i,j);
      B[j] -= a*B[i];
    }
  }
  // backwards substitutions optimized for block-width n
  // in O(s*n) = O(m*n^2)
  for (int i=s-1; i>=0; --i)
    for (int j=i+1; j<min(s,i+n+1); ++j)
      B[i] -= M[i][j]*B[j];
}


int main() {
  while (parse_input()) {
    // system constant part B = (1,1,...,1,0)
    vec B(s,1.);
    B[s-1] = 0.;
    system_solve(M,B);
    printf("%lf\n",B[0]);
  }
  return 0;
}
