#include <iostream>
using namespace std;

#define MAX 51

int box[MAX][MAX];
int n,m,dr,dg,db,pr,pg,pb;
int d[4];
int p[4];
int nb[4];
int haut[MAX];
bool test[4];

bool libre(int i, int j) {
  if (i==1) return (box[2][j]==0);
  else if (i==n) return (box[n-1][j]==0);
  else return (box[i-1][j]==0)&&(box[i+1][j]==0);
}

bool MAJ() {
  int i;
  i = 1;
  for (int j=1; j<=m-2; j++) {
    if ((box[i][j+2]>0)&&(libre(i,j))&&(libre(i,j+1))) {
      box[i+1][haut[i+1]] = box[i][j+2];
      ++(haut[j+1]);
      box[i][j+2] = 0;
      --(haut[i]);
      return true;
    }
  }
  for (i=2; i<n; i++) {
    for (int j=1; j<=m-2; j++) {
      if ((box[i][j+2]>0)&&(libre(i,j))&&(libre(i,j+1))) {
	box[i-1][haut[i-1]] = box[i][j+2];
	++(haut[i-1]);
	box[i][j+2] = 0;
	box[i+1][haut[i+1]] = box[i][j+1];
	++(haut[i+1]);
	box[i][j+1] = 0;
	haut[i] -= 2;
	return true;
      }
    }
  }
  i = n;
  for (int j=1; j<=m-2; j++) {
    if ((box[i][j+2]>0)&&(libre(i,j))&&(libre(i,j+1))) {
      box[i-1][haut[i-1]] = box[i][j+2];
      ++(haut[i-1]);
      box[i][j+2] = 0;
      --(haut[i]);
      return true;
    }
  }
  return false;
}

void MAJg() {
  while (MAJ()) {}
}

void drop(int c) {
  if (test[c]) {
    ++(nb[c]);
    --(nb[0]);
    box[p[c]][haut[p[c]]] = c;
    ++(haut[p[c]]);
    MAJg();
  }
}

int main() {
  int cas = 1;

  while (cin >> n >> m >> d[1] >> d[2] >> d[3] >> p[1] >> p[2] >> p[3]) {
    if (n==0) return 0;
    int t = 0;
    for (int c=1; c<=3; c++) {
      test[c] = true;
      nb[c] = 0;
    }
    nb[0] = n*m;
    for (int i=1; i<=n; i++) {
      haut[i] = 1;
      for (int j=1; j<=m; j++)
	box[i][j] = 0;
    }
    while (test[1]||test[2]||test[3]) {
      for (int c=1; c<=3; c++)
	if (t%d[c]==0) {
	  drop(c);
	  test[c] = (haut[p[c]]<m);
	}
      ++t;
    }
    cout << "Case " << cas++ << ": " << nb[1] << ' ' << nb[2] << ' ' << nb[3] << ' ' << nb[0] << '\n';
  }
  
  return 0;
}
