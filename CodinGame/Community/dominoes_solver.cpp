/*
  That's an Exact Cover problem, so let's have fun with Dancing Links!
  (even though that's clearly overkill considering the input size)
  See main() for the (pretty straightforward) reduction to EC.
*/

#include <cstddef>
#include <cassert>
#include <vector>
#include <iostream>
using namespace std;


/* ====== DANCING LINKS ====== */
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


/* ====== PROBLEM CODE ====== */
int N, H, W, Size;
vector<string> G;

int num(char c) {
  return (int)c - (int)'0';
}

int cell(int i, int j) {
  return i*W + j;
}

int domi(int a, int b) {
  if (a<b) swap(a,b);
  return H*W + a*(a+1)/2 + b;
}

int main() {
  cin >> N;
  cin >> H >> W;
  G.resize(H);
  for (int i=0; i<H; ++i) cin >> G[i];
  Size = H*W + (N+1)*(N+2)/2;
  subsets SS;
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j) {
      if (j+1<W) SS.push_back(subset {cell(i,j), cell(i,j+1), domi(num(G[i][j]),num(G[i][j+1]))});
      if (i+1<H) SS.push_back(subset {cell(i,j), cell(i+1,j), domi(num(G[i][j]),num(G[i+1][j]))});
    }
  vector<int> Sol;
  assert(dancing_links(Size,SS,Sol));
  for (auto it=Sol.begin(); it!=Sol.end(); ++it) {
    int x1 = SS[*it][0]/W, y1 = SS[*it][0]%W;
    int x2 = SS[*it][1]/W, y2 = SS[*it][1]%W;
    G[x1][y1] = G[x2][y2] = (x1==x2 ? '=' : '|');
  }
  for (int i=0; i<H; ++i) cout << G[i] << endl;
  return 0;
}
