#include <iostream>
#include <climits>
using namespace std;

const int MAX = 50;

int n,m;
int d[4], p[4], B[MAX][MAX], H[MAX], T[4], nb[4];
bool feed[4];

bool libre(int x) {
  int y = H[x];
  return (0<x && x<n-1 && y>=3 &&
	  B[x-1][y-1]==0 && B[x-1][y-2]==0 && B[x-1][y-3]==0 &&
	  B[x+1][y-1]==0 && B[x+1][y-2]==0 && B[x+1][y-3]==0);
}

bool libre_left(int x) {
  int y = H[x];
  return (0<x && y>=3 &&
	  B[x-1][y-1]==0 && B[x-1][y-2]==0 && B[x-1][y-3]==0);
}

bool libre_right(int x) {
  int y = H[x];
  return (x<n-1 && y>=3 &&
	  B[x+1][y-1]==0 && B[x+1][y-2]==0 && B[x+1][y-3]==0);
}

bool drop(int c, int x) {
  if (H[x]==m) return false;
  B[x][H[x]] = c;
  ++H[x];
  if (libre(x)) {
    int d = B[x][H[x]-2];
    B[x][H[x]-1] = 0;
    B[x][H[x]-2] = 0;
    H[x] -= 2;
    drop(c,x-1);
    drop(d,x+1);
  }
  else if (libre_left(x)) {
    B[x][H[x]-1] = 0;
    --H[x];
    drop(c,x-1);
  }
  else if (libre_right(x)) {
    B[x][H[x]-1] = 0;
    --H[x];
    drop(c,x+1);
  }
  return true;
}

void affiche() {
  for (int j=m-1; j>=0; --j) {
    for (int i=0; i<n; ++i)
      if (B[i][j]>0) cout << B[i][j];
      else cout << ' ';
    cout << endl;
  }
}

int main() {
  int cas = 1;
  while (true) {
    cin >> n >> m >> d[1] >> d[2] >> d[3] >> p[1] >> p[2] >> p[3];
    if (n==0) break;
    // init
    for (int i=0; i<n; ++i) {
      H[i] = 0;
      for (int j=0; j<m; ++j)
	B[i][j] = 0;
    }
    for (int c=1; c<=3; ++c) {
      nb[c] = 0;
      if (d[c]==0) {
	feed[c] = false;
	T[c] = INT_MAX;
      }
      else {
	feed[c] = true;
	T[c] = 0;
      }
    }
    // simulation
    int t = 0;
    while (feed[1]||feed[2]||feed[3]) {
      for (int c=1; c<=3; ++c) {
	if (feed[c] && t==T[c]) {
	  if (!drop(c,p[c])) {
	    feed[c] = false;
	    T[c] = INT_MAX;
	  }
	  else {
	    ++nb[c];
	    T[c] += d[c];
	  }
	  //affiche();
	}
      }
      t = min(T[1],min(T[2],T[3]));
    }
    int nb0 = n*m-nb[1]-nb[2]-nb[3];
    cout << "Case " << cas++ << ": " << nb[1] << ' ' << nb[2] << ' ' << nb[3] << ' ' << nb0 << endl;
  }
  return 0;
}
