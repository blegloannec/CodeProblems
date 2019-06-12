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


// COUNTING SOLUTIONS
void solve_count(cell *header, vector<int> &sol_tmp, vector<int> &sol, int &sol_cnt) {
  if (header->R==header) {
    if (sol_cnt==0) sol = sol_tmp;
    ++sol_cnt;
    return;
  }
  if (sol_cnt>1) return;  // for this pb only
  cell *c = NULL;
  cell *j = header->R;
  while (j!=header) {
    if (c==NULL || j->S<c->S) c = j;
    j = j->R;
  }
  cover(c);
  cell *r = c->D;
  while (r!=c) {
    sol_tmp.push_back(r->S);
    cell *j = r->R;
    while (j!=r) {
      cover(j->C);
      j = j->R;
    }
    solve_count(header,sol_tmp,sol,sol_cnt);
    j = r->L;
    while (j!=r) {
      uncover(j->C);
      j = j->L;
    }
    sol_tmp.pop_back();
    r = r->D;
  }
  uncover(c);
}

int dancing_links_count(int size, subsets &sets, vector<int> &sol) {
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
  vector<int> sol_tmp;
  int sol_cnt = 0;
  solve_count(header,sol_tmp,sol,sol_cnt);
  return sol_cnt;
}


// REDUCTION Sudoku --> Exact Cover
typedef vector< vector<int> > grid;

subset pack_subset(int i, int j, int d) {
  subset S(4);
  --d;                    // digit d from 1-9 to 0-8
  int k = 3*(i/3) + j/3;  // block
  S[0] = 9*i + j;         // cell (i,j)
  S[1] = 9*(i+ 9) + d;    // digit d in line i
  S[2] = 9*(j+18) + d;    // digit d in column j
  S[3] = 9*(k+27) + d;    // digit d in block k
  return S;
}

void unpack_subset(const subset &S, int &i, int &j, int &d) {
  i = S[0]/9;
  j = S[0]%9;
  d = S[1]%9 + 1;
}

int sudoku_solve(grid &G) {
  subsets S;
  for (int i=0; i<9; ++i)
    for (int j=0; j<9; ++j) {
      if (G[i][j]!=0)
	S.push_back(pack_subset(i,j,G[i][j]));
      else
	for (int d=1; d<=9; ++d)
	  S.push_back(pack_subset(i,j,d));
    }
  int size = 4*9*9;
  vector<int> Sol;
  int cnt = dancing_links_count(size, S, Sol);
  if (cnt==1)
    for (int k: Sol) {
      int i,j,d;
      unpack_subset(S[k],i,j,d);
      G[i][j] = d;
    }
  return cnt;
}


// MAIN
int main() {
  bool first = true;
  grid G(9, vector<int>(9));
  while (true) {
    for (int i=0; i<9; ++i)
      for (int j=0; j<9; ++j)
	if (!(cin >> G[i][j])) return 0;
    if (first) first = false;
    else cout << endl;
    int res = sudoku_solve(G);
    if (res==1) {
      for (int i=0; i<9; ++i)
	for (int j=0; j<9; ++j)
	  cout << G[i][j] << (j==8 ? '\n' : ' ');
    }
    else if (res==0) cout << "Find another job" << endl;
    else cout << "Non-unique" << endl;
  }
  return 0;
}
