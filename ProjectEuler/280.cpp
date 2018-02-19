#include <cstdio>
#include <vector>
#include <unordered_map>
//#include <cassert>
using namespace std;

// classic markov-chain expectation block-tri-diagonal system
// similar for instance to ACM-ICPC SWERC 2008 First Knight
// runs in <1s with -O3 by optimized solving of a unique large system

typedef double scal;
typedef vector<scal> vec;
typedef vector<vec> matrix;

const int w = 5;  // grid size
int l;            // masks count
int s;            // system size
int n;            // system "diagonal width"
vector<int> mask;
unordered_map<int,int> mask_index;

const int seed = 1;
int bot[w],top[w];
int init_mask = 0, final_mask = 0;

vec B;
matrix M;

int P(int i, int j, int im) {
  return (i*w+j)*l + im;
}

int nb1(int x) {
  int o = 0;
  while (x) {
    if (x&1) ++o;
    x >>= 1;
  }
  return o;
}

void gen_system() {
  // masks (~> binom(11,5))
  for (int i=0; i<(1<<(2*w+1)); ++i)
    if (nb1(i)==w) mask.push_back(i);
  l = mask.size();
  for (int i=0; i<l; ++i) mask_index[mask[i]] = i;
  // masks auxiliary constants
  for (int i=0; i<w; ++i) {
    bot[i] = 1<<(i+1);
    top[i] = 1<<(i+w+1);
    init_mask |= bot[i];
    final_mask |= top[i];
  }
  // generating system
  s = w*w*l;
  n = w*l;
  vector< pair<int,int> > dV {make_pair(-1,0),make_pair(1,0),make_pair(0,-1),make_pair(0,1)};
  M.resize(s);
  for (int i=0; i<s; ++i) {
    M[i].resize(s,0.);
    M[i][i] = 1.;
  }
  B.resize(s,1.);
  for (int i=0; i<w; ++i)
    for (int j=0; j<w; ++j)
      for (int k=0; k<l; ++k) {
	int m = mask[k];
	if (i==w-1 && !(m&seed) && (m&bot[j])) {
	  // pick a seed
	  B[P(i,j,k)] = 0.;
	  M[P(i,j,k)][P(i,j,mask_index[m^seed^bot[j]])] = -1.;
	}
	else if (i==0 && (m&seed) && !(m&top[j])) {
	  // drop a seed
	  B[P(i,j,k)] = 0.;
	  M[P(i,j,k)][P(i,j,mask_index[m^seed^top[j]])] = -1.;
	}
	else if (i==0 && m==final_mask) {
	  // final state ~> sink
	  B[P(i,j,k)] = 0.;
	}
	else {
	  vector< pair<int,int> > V;
	  for (auto idv=dV.begin(); idv!=dV.end(); ++idv) {
	    int vi = i+idv->first, vj = j+idv->second;
	    if (0<=vi && vi<w && 0<=vj && vj<w)
	      V.push_back(make_pair(vi,vj));
	  }
	  double vs = V.size();
	  for (int iv=0; iv<vs; ++iv)
	    M[P(i,j,k)][P(V[iv].first,V[iv].second,k)] = -1./vs;
	}
      }
}


// linear system solver
const double EPS = 1e-8;
bool fzero(double x) {
  return (-EPS<x && x<EPS);
}

/* // NOT USED in this particular case (see comment in system_solve())
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
  // triangularization, O(s*n^2)
  for (int i=0; i<s; ++i) {
    /*/ NOT USED as in this particular case we always have j0 = i
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
      if (!fzero(a)) {
	line_diff(a,M,i,j);
	B[j] -= a*B[i];
      }
    }
  }
  // backwards substitutions optimized for block-width n, O(s*n)
  for (int i=s-1; i>=0; --i)
    for (int j=i+1; j<min(s,i+n+1); ++j)
      B[i] -= M[i][j]*B[j];
}


int main() {
  gen_system();
  system_solve(M,B);
  printf("%.7lf\n",B[P(w/2,w/2,mask_index[init_mask])]);
  return 0;
}
