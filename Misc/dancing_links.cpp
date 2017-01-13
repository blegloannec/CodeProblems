#include <cstddef>
#include <cassert>
#include <vector>
#include <iostream>
using namespace std;

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


// COUNTING SOLUTIONS
void solve_count(cell *header, int &sol) {
  if (header->R==header) {
    ++sol;
    return;
  }
  //cell *c = NULL;
  cell *c = header->R;
  /*while (j!=header) {
    if (c==NULL || j->S<c->S) c = j;
    j = j->R;
    }*/
  cover(c);
  cell *r = c->D;
  while (r!=c) {
    //sol.push_back(r->S);
    cell *j = r->R;
    while (j!=r) {
      cover(j->C);
      j = j->R;
    }
    solve_count(header,sol);
    j = r->L;
    while (j!=r) {
      uncover(j->C);
      j = j->L;
    }
    //sol.pop_back();
    r = r->D;
  }
  uncover(c);
}

int dancing_links_count(int size, subsets &sets) {
  cell *header = new cell(NULL,NULL,0,NULL);
  vector<cell*> col;
  for (int j=0; j<size; ++j)
    col.push_back(new cell(header,NULL,0,NULL));
  /*cell *j = header->R;
  while (j!=header) {
    cout << j->S << endl;
    j = j->R;
    }*/
  for (int i=0; i<(int)sets.size(); ++i) {
    cell *row = NULL;
    for (subset::iterator jt=sets[i].begin(); jt!=sets[i].end(); ++jt) {
      ++(col[*jt]->S);
      row = new cell(row,col[*jt],i,col[*jt]);
    }
  }
  int sol = 0;
  solve_count(header,sol);
  return sol;
}
