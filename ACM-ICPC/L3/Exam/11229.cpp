#include <cstdio>
#include <unordered_map>
#include <cmath>
using namespace std;

double P[2][3][3];

int get_cell(int C, int i, int j) {
  return (C>>(2*(3*i+j)))&3;
}

int set_cell(int C, int i, int j, int p) {
  return C|(p<<(2*(3*i+j)));
}

bool align(int C, int p) {
  for (int i=0; i<3; ++i)
    if ((get_cell(C,i,0)==p && get_cell(C,i,1)==p && get_cell(C,i,2)==p) ||
	(get_cell(C,0,i)==p && get_cell(C,1,i)==p && get_cell(C,2,i)==p))
      return true;
  return ((get_cell(C,0,0)==p && get_cell(C,1,1)==p && get_cell(C,2,2)==p) ||
	  (get_cell(C,0,2)==p && get_cell(C,1,1)==p && get_cell(C,2,0)==p));
}

unordered_map<int,double> memo[2];
double win(int C=0, int p=1) {
  if (memo[p-1].find(C)!=memo[p-1].end()) return memo[p-1][C];
  int o = 3-p;
  double res = 0.;
  if (align(C,p)) res = 1.;
  else if (align(C,o)) res = 0.;
  else {
    bool tie = true;
    for (int i=0; i<3; ++i)
      for (int j=0; j<3; ++j)
	if (get_cell(C,i,j)==0) {
	  tie = false;
	  res = max(res,P[p-1][i][j]*(1.-win(set_cell(C,i,j,p),o))+(1.-P[p-1][i][j])*(1.-win(set_cell(C,i,j,o),o)));
	}
    if (tie && p==2) res = 1.; // on compte les tie pour le player 2
  }
  memo[p-1][C] = res;
  return res;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1; t<=T; ++t) {
    for (int i=0; i<3; ++i)
      for (int j=0; j<3; ++j) {
	int p;
	scanf("%d",&p);
	P[0][i][j] = (double)p/100.;
      }
    for (int i=0; i<3; ++i)
      for (int j=0; j<3; ++j) {
	int p;
	scanf("%d",&p);
	P[1][i][j] = (double)p/100.;
      }
    double p = round(10000.*win())/100.;
    printf("Case #%d: %.2f\n",t,p);
    // cleaning
    memo[0].clear();
    memo[1].clear();
  }
  return 0;
}
