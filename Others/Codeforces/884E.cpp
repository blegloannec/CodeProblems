#include <cstdio>
#include <vector>
using namespace std;

int n,m,C;
vector<bool> M[2];
vector< pair<int,int> > T[2];

int H(char c) {
  return c<='9' ? c-'0' : c-'A'+10;
}

pair<int,int> find(int c, int j) {
  int c0 = T[c][j].first, j0 = T[c][j].second;
  if (!(c0==c && j0==j)) T[c][j] = find(c0,j0);
  return T[c][j];
}

void uni(int c1, int j1, int c2, int j2) {
  auto x1 = find(c1,j1), x2 = find(c2,j2);
  if (x1!=x2) {
    T[x2.first][x2.second] = x1;
    --C;
  }
}
  
int main() {
  scanf("%d %d",&n,&m);
  for (int i=0; i<2; ++i) {
    M[i].resize(m);
    T[i].resize(m);
  }
  int c = 0;
  char s[m/4];
  for (int i=0; i<n; ++i) {
    scanf(" %s",s);
    for (int j=0; j<m/4; ++j) {
      int v = H(s[j]);
      for (int k=0; k<4; ++k) M[c][4*j+3-k] = (v>>k)&1;
    }
    for (int j=0; j<m; ++j)
      if (M[c][j]) {
	if (j>0 && M[c][j-1]) T[c][j] = T[c][j-1];
	else {
	  ++C;
	  T[c][j] = make_pair(c,j); 
	}
      }
    if (i>0)
      for (int j=0; j<m; ++j)
	if (M[c][j] && M[c^1][j]) uni(c,j,c^1,j);
    c ^= 1;
  }
  printf("%d\n",C);
  return 0;
}
