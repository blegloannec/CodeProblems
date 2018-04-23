/* 
   Randomized general mincut for standard edges and hyperedges of size 3.
   NB: this can be seen as a modified/generalized Karger's algorithm
   https://en.wikipedia.org/wiki/Karger%27s_algorithm
   
   NB post editorial: there was actually a very simple reduction to a
   standard graph general mincut, thus allowing the use of either
   the standard Karger's (randomized) algorithm or the Stoer-Wagner
   (deterministic) algorithm
   https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm
*/

#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

typedef long long ent;

int n,m;
vector< vector<int> > M;
vector<ent> F;

int find(vector<int> &T, int x) {
  if (T[x]<0) return x;
  T[x] = find(T,T[x]);
  return T[x];
}

void merge(vector<int> &T, int &C, int x, int y) {
  int x0 = find(T,x), y0 = find(T,y);
  if (x0!=y0) {
    T[y0] = x0;
    --C;
  }
}

void shuffle(vector<int> &A) {
  for (int i=(int)A.size()-1; i>0; --i)
    swap(A[i],A[rand()%i]);
}

ent random_maxpart() {
  vector<int> I(m);
  for (int i=0; i<m; ++i) I[i] = i;
  shuffle(I);
  vector<int> T(n,-1);
  int C = n;
  ent res = 0;
  for (int j=0; j<m; ++j) {
    int i = I[j];
    if (M[i].size()==2) {
      int u = M[i][0], v = M[i][1];
      if (find(T,u)==find(T,v)) res += F[i];
      else if (C>2) {
	merge(T,C,u,v);
	res += F[i];
      }
    }
    else {
      int u = M[i][0], v = M[i][1], w = M[i][2];
      int u0 = find(T,u), v0 = find(T,v), w0 = find(T,w);
      if (u0==v0 && v0==w0) res += F[i];
      else if (u0!=v0 && u0!=w0 && v0!=w0) {
	if (C>3) {
	  merge(T,C,u,v);
	  merge(T,C,u,w);
	  res += F[i];
	}
      }
      else if (u0!=v0) {
	if (C>2) {
	  merge(T,C,u,v);
	  res += F[i];
	}
      }
      else if (u0!=w0) {
	if (C>2) {
	  merge(T,C,u,w);
	  res += F[i];
	}
      }
      else if (v0!=w0) {
	if (C>2) {
	  merge(T,C,v,w);
	  res += F[i];
	}
      }
    }
  }
  return res;
}

int main() {
  srand(42);
  cin >> n >> m;
  M.resize(m);
  F.resize(m);
  vector<int> T(n,-1);
  int C = n;
  ent SF = 0;
  for (int i=0; i<m; ++i) {
    int k;
    cin >> k >> F[i];
    SF += F[i];
    int u0;
    for (int j=0; j<k; ++j) {
      int u;
      cin >> u; --u;
      M[i].push_back(u);
      if (j==0) u0 = u;
      else merge(T,C,u0,u);
    }
  }
  ent res = 0;
  if (C>1) res = SF;
  else for (int i=0; i<100000; ++i) res = max(res,random_maxpart());
  cout << res << endl;
  return 0;
}
