#include <iostream>
#include <vector>
#include <cassert>
using namespace std;


/* ===== DLX ===== */
typedef vector<int> subset;
typedef vector<subset> subsets;

// STRUCTURES
struct cell {
  int S;
  cell *C;
  cell *L,*R,*U,*D;

  cell(cell *H, cell *V, int S, cell *C) : S(S), C(C) {
    if (H!=NULL) {
      L = H->L;
      R = H;
      L->R = this;
      R->L = this;
    }
    else {
      L = this;
      R = this;
    }
    if (V!=NULL) {
      U = V->U;
      D = V;
      U->D = this;
      D->U = this;
    }
    else {
      U = this;
      D = this;
    }
  }

  void hide_v() {
    U->D = D;
    D->U = U;
  }

  void unhide_v() {
    D->U = this;
    U->D = this;
  }

  void hide_h() {
    L->R = R;
    R->L = L;
  }
  
  void unhide_h() {
    R->L = this;
    L->R = this;
  }
};

void cover(cell *c) {
  assert(c->C==NULL);
  c->hide_h();
  cell *i = c->D;
  while (i!=c) {
    cell *j = i->R;
    while (j!=i) {
      j->hide_v();
      --(j->C->S);
      j = j->R;
    }
    i = i->D;
  }
}

void uncover(cell *c) {
  assert(c->C==NULL);
  cell *i = c->U;
  while (i!=c) {
    cell *j = i->L;
    while (j!=i) {
      ++(j->C->S);
      j->unhide_v();
      j = j->L;
    }
    i = i->U;
  }
  c->unhide_h();
}


// SOLVER
bool solve(cell *header, vector<int> &sol) {
  if (header->R==header) return true;
  cell *c = NULL;
  cell *j = header->R;
  while (j!=header) {
    if (c==NULL || j->S<c->S) c = j;
    j = j->R;
  }
  cover(c);
  cell *r = c->D;
  while (r!=c) {
    sol.push_back(r->S);
    cell *j = r->R;
    while (j!=r) {
      cover(j->C);
      j = j->R;
    }
    if (solve(header,sol)) return true;
    j = r->L;
    while (j!=r) {
      uncover(j->C);
      j = j->L;
    }
    sol.pop_back();
    r = r->D;
  }
  uncover(c);
  return false;
}

bool dancing_links(int size, subsets &sets, vector<int> &sol) {
  cell *header = new cell(NULL,NULL,0,NULL);
  vector<cell*> col;
  for (int j=0; j<size; ++j)
    col.push_back(new cell(header,NULL,0,NULL));
  for (int i=0; i<(int)sets.size(); ++i) {
    cell *row = NULL;
    for (subset::iterator jt=sets[i].begin(); jt!=sets[i].end(); ++jt) {
      ++(col[*jt]->S);
      row = new cell(row,col[*jt],i,col[*jt]);
    }
  }
  return solve(header,sol);
}
/* ===== ===== */


int main() {
  int n;
  cin >> n;
  subsets Sets;
  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j) {
      int v;
      cin >> v;
      if (v==0) {
	for (int d=0; d<n; ++d) {
	  subset S {i*n+j, n*n+n*i+d, n*n+n*n+n*j+d};
	  Sets.push_back(S);
	}
      }
      else {
	int d = v-1;
	subset S {i*n+j, n*n+n*i+d, n*n+n*n+n*j+d};
	Sets.push_back(S);
      }
    }
  }
  int siz = 3*n*n;
  vector<int> Sol;
  if (dancing_links(siz, Sets, Sol)) {
    vector< vector<int> > G(n, vector<int>(n));
    for (int s : Sol) {
      int i = Sets[s][0]/n, j = Sets[s][0]%n, v = Sets[s][1]%n;
      G[i][j] = v+1;
    }
    for (int i=0; i<n; ++i)
      for (int j=0; j<n; ++j)
	cout << G[i][j] << (j==n-1 ? '\n' : ' ');
  }
  else cout << "No solution\n";
  return 0;
}
