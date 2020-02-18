/*
  Reduction to Exact Cover
  Dancing Links
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;


/* ===== BEGIN DLX ===== */
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
/* ===== END DLX ===== */


struct position {
  int i,j,l;
  position(int i, int j, int l) : i(i), j(j), l(l) {}
};

int main() {
  int H,W,N;
  cin >> H >> W;
  vector<string> Grid(H);
  for (int i=0; i<H; ++i) cin >> Grid[i];
  cin >> N;
  vector<string> Words(N);
  for (int i=0; i<N; ++i) cin >> Words[i];
  // scanning words positions
  //   horizontal
  vector< vector<bool> > HCov(H,vector<bool>(W,false));
  vector<position> HPos;
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j)
      if (Grid[i][j]=='.' && !HCov[i][j]) {
	int j0 = j;
	while (j<W && Grid[i][j]=='.') HCov[i][j++] = true;
	int l = j-j0;
	if (l>1) HPos.push_back(position(i,j0,l));
	else HCov[i][j0] = false;
      }
  //   vertical
  vector< vector<bool> > VCov(H,vector<bool>(W,false));
  vector<position> VPos;
  for (int j=0; j<W; ++j)
    for (int i=0; i<H; ++i)
      if (Grid[i][j]=='.' && !VCov[i][j]) {
	int i0 = i;
	while (i<H && Grid[i][j]=='.') VCov[i++][j] = true;
	int l = i-i0;
	if (l>1) VPos.push_back(position(i0,j,l));
	else VCov[i0][j] = false;
      }
  int NH = HPos.size(), NV = VPos.size();
  assert(NH+NV==N);
  // numbering H & V covered positions
  vector< vector<int> > NumHVCov(H,vector<int>(W,-1));
  int hvcnt = 0;
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j)
      if (HCov[i][j] && VCov[i][j])
	NumHVCov[i][j] = hvcnt++;
  // generating subsets
  subsets sets;
  for (int w=0; w<N; ++w) {
    // horizontal
    for (int p=0; p<NH; ++p)
      if (HPos[p].l==(int)Words[w].size()) {
	vector<int> S {w, N+p};  // word idx & pos idx
	for (int k=0; k<HPos[p].l; ++k)
	  if (NumHVCov[HPos[p].i][HPos[p].j+k]>=0) {
	    int c = Words[w][k] - 'A';  // char code 0-25
	    for (int b=0; b<5; ++b)  // 5 bits
	      if (((c>>b)&1)==1)  // bin. 1s of the char code
		S.push_back(N + N + 5*NumHVCov[HPos[p].i][HPos[p].j+k] + b);
	  }
	sets.push_back(S);
      }
    // vertical
    for (int p=0; p<NV; ++p)
      if (VPos[p].l==(int)Words[w].size()) {
	vector<int> S {w, N+NH+p}; // word idx & pos idx
	for (int k=0; k<VPos[p].l; ++k)
	  if (NumHVCov[VPos[p].i+k][VPos[p].j]>=0) {
	    int c = Words[w][k] - 'A';  // char code
	    for (int b=0; b<5; ++b)
	      if (((c>>b)&1)==0)  // bin. 0s of char code (comp. of horiz.)
		S.push_back(N + N + 5*NumHVCov[VPos[p].i+k][VPos[p].j] + b);
	  }
	sets.push_back(S);
      }
  }
  // solving
  vector<int> sol;
  int size = 2*N + 5*hvcnt;
  assert(dancing_links(size, sets, sol));
  // output solution
  for (int s : sol) {
    int w = sets[s][0], p = sets[s][1];
    if (p<N+NH) {
      p -= N;
      for (int k=0; k<HPos[p].l; ++k)
	Grid[HPos[p].i][HPos[p].j+k] = Words[w][k];
    }
    else {
      p -= N+NH;
      for (int k=0; k<VPos[p].l; ++k)
	Grid[VPos[p].i+k][VPos[p].j] = Words[w][k];
    }
  }
  for (int i=0; i<H; ++i) cout << Grid[i] << endl;
  return 0;
}
