#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

/* 
   hardest "medium" problem ever...
   expected complexity O(n^3), yet too slow to pass every testcase
   it would require some more stupid optimizations...

   for sparse tables, see for instance:
   https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/#Sparse_Table_(ST)_algorithm
*/

int log2(int n) {
  int k = 0;
  while (n>1) {n >>= 1; ++k;}
  return k;
}

int LOG2[351];
int required[200];

typedef int elem;

// MAX sparse table, O(n log n) pre-computation and space, O(1) per request
struct SparseTable {
  int size, depth;
  vector<elem> A;
  vector< vector<elem> > T;
  
  SparseTable(vector<elem> &A0) {
    A = A0;  // copy
    size = A.size();
    depth = 0;
    while ((1<<depth)<=size) ++depth;
    T.resize(depth);
    T[0].resize(size);
    for (int i=0; i<size; ++i) T[0][i] = i;
    for (int k=1; k<depth; ++k) {
      int sizek = size+1-(1<<k), dk = 1<<(k-1);
      T[k].resize(sizek,0);
      for (int i=0; i<sizek; ++i) // MAX
        T[k][i] = A[T[k-1][i]] >= A[T[k-1][i+dk]] ? T[k-1][i] : T[k-1][i+dk];
    }
  }

  int range_index(int l, int r) {
    //assert(l<=r);
    int w = r-l+1; //, k = 0;
    //while (w>1) {w >>= 1; ++k;}
    int k = LOG2[w];
    int dk = 1<<k;
    return (A[T[k][l]] >= A[T[k][r-dk+1]] ? T[k][l] : T[k][r-dk+1]);  // MAX
  }

  elem range(int l, int r) {
    return A[range_index(l,r)];
  }
};

int main() {
  for (int n=0; n<351; ++n) LOG2[n] = log2(n);
  required[0] = 1;
  for (int k=1; k<200; ++k) required[k] = required[k-1] + (2*k+1)*(2*k+1);
  int q;
  scanf("%d",&q);
  for (int t=0; t<q; ++t) {
    int n,m,K;
    scanf("%d %d %d",&n,&m,&K);
    vector< vector<int> > H(n),R(n),C(m);
    for (int i=0; i<n; ++i) {
      H[i].resize(m);
      R[i].resize(m);
      for (int j=0; j<m; ++j) {
	scanf("%d",&H[i][j]);
	R[i][j] = H[i][j];
	C[j].push_back(H[i][j]);
      }
    }
    // on cree une table par ligne et colonne pour avoir le max
    // de tout intervalle en O(1)
    vector<SparseTable> SR,SC;
    for (int i=0; i<n; ++i) SR.push_back(SparseTable(R[i]));
    for (int j=0; j<m; ++j) SC.push_back(SparseTable(C[j]));
    // sommes prefixes pour la somme de tout intervalle en O(1)
    for (int i=0; i<n; ++i)
      for (int j=1; j<m; ++j) R[i][j] += R[i][j-1];
    for (int j=0; j<m; ++j)
      for (int i=1; i<n; ++i) C[j][i] += C[j][i-1];
    // on essaye tous les centres (i,j)
    int res = 0;
    for (int i=0; i<n; ++i)
      for (int j=0; j<m; ++j) {
	int minh = H[i][j];   // taille minimale d'une pyramide
	int blocs = H[i][j];  // nb de blocs deja places
	if (res==0 && minh<=1 && blocs+K>=1) res = 1;
	for (int k=1; 0<=i-k && i+k<n && 0<=j-k && j+k<m; ++k) {
	  // rayon k
	  blocs += R[i-k][j+k] - (j-k>0 ? R[i-k][j-k-1] : 0);
	  blocs += R[i+k][j+k] - (j-k>0 ? R[i+k][j-k-1] : 0);
	  blocs += C[j-k][i+k-1] - C[j-k][i-k];
	  blocs += C[j+k][i+k-1] - C[j+k][i-k];
	  if (required[k]>blocs+K) break;
	  minh = max(minh,k+max(SR[i-k].range(j-k,j+k),SR[i+k].range(j-k,j+k)));
	  minh = max(minh,k+max(SC[j-k].range(i-k,i+k),SC[j+k].range(i-k,i+k)));
	  if (res<k+1 && minh<=k+1) res = k+1;
	}
      }
    printf("%d\n",res);
  }
  return 0;
}
