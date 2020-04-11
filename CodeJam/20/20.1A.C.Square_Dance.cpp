#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

struct Cell;

int R, C;
vector< vector<Cell> > G;
long long Score;
vector<int> Elim;
unordered_set<int> Update;

struct Cell {
  int i, j, s;
  int iU, iD, jL, jR;
  bool eliminated;
  
  Cell(int i, int j, int s) : i(i), j(j), s(s) {
    iU = i-1; iD = i+1;
    jL = j-1; jR = j+1;
    eliminated = false;
  }
  
  void update() {
    int deg = 0, scr = 0;
    if (iU>=0) {
      ++deg;
      scr += G[iU][j].s;
    }
    if (iD<R) {
      ++deg;
      scr += G[iD][j].s;
    }
    if (jL>=0) {
      ++deg;
      scr += G[i][jL].s;
    }
    if (jR<C) {
      ++deg;
      scr += G[i][jR].s;
    }
    if (deg*s<scr) {
      Score -= s;
      Elim.push_back(i*C+j);
    }
  }
  
  void eliminate() {
    eliminated = true;
    if (iU>=0) {
      G[iU][j].iD = iD;
      Update.insert(iU*C+j);
    }
    if (iD<R) {
      G[iD][j].iU = iU;
      Update.insert(iD*C+j);
    }
    if (jL>=0) {
      G[i][jL].jR = jR;
      Update.insert(i*C+jL);
    }
    if (jR<C) {
      G[i][jR].jL = jL;
      Update.insert(i*C+jR);
    }
  }
};

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    Score = 0;
    cin >> R >> C;
    G.resize(R);
    for (int i=0; i<R; ++i)
      for (int j=0; j<C; ++j) {
	int s;
	cin >> s;
	G[i].push_back(Cell(i,j,s));
	Score += s;
	Update.insert(i*C+j);
      }
    long long TotalScore = 0;
    while (!(Update.empty() && Elim.empty())) {
      TotalScore += Score;
      for (int u : Elim) {
	int i = u/C, j = u%C;
	G[i][j].eliminate();
      }
      Elim.clear();
      for (int u : Update) {
	int i = u/C, j = u%C;
	if (!G[i][j].eliminated)
	  G[i][j].update();
      }
      Update.clear();
    }
    cout << "Case #" << t << ": " << TotalScore << endl;
    // cleaning
    G.clear();
  }
  return 0;
}
