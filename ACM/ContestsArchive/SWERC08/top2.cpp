#include <iostream>
using namespace std;

/* matrice circulante -> puissances circulantes
   produit en n^2 (on ne calcule qu'une colonne) 
   algo en n^2*log(S) */

typedef long long ent;
#define MAX 1001
int n;
ent momo;
ent m[2][MAX];
ent svg[MAX];
ent mess[MAX];
int curr;

void produit(ent *mat, ent *vect, ent *res) {
  for (int i=0; i<n; ++i) {
    res[i] = 0L;
    for (int j=0; j<n; ++j) {
      res[i] += (vect[j]*mat[(i-j+n)%n])%momo;
    }
    res[i] = res[i]%momo;
  }
}

void expo(int n) {
  if (n<=1) return;
  if (n%2==0) {
    expo(n/2);
    produit(m[curr],m[curr],m[(curr+1)%2]);
    curr = (curr+1)%2;
  }
  else {
    expo(n/2);
    produit(m[curr],m[curr],m[(curr+1)%2]);
    curr = (curr+1)%2;
    produit(m[curr],svg,m[(curr+1)%2]);
    curr = (curr+1)%2;
  }
}

int main() {
  int cas,S,X;
  ent a,L,R;
  cin >> cas;
  while (cas-->0) {
    cin >> n >> S >> L >> R >> X;
    momo = 1L;
    for (int i=0; i<X; ++i)
      momo *= 10L;
    L = L%momo;
    R = R%momo;
    curr = 0;
    for (int i=0; i<n; ++i) {
      cin >> a;
      mess[i] = a;
      m[curr][i] = 0L;
      svg[i] = 0L;
    }

    if (S==0) {
      for (int i=0; i<n; ++i) {
	cout << mess[i];
	if (i<n-1) cout << ' ';
      }
      cout << '\n';
      continue;
    }
    
    m[curr][0] = 1L;
    svg[0] = 1L;
    m[curr][1] = L;
    svg[1] = L;
    m[curr][n-1] = R;
    svg[n-1] = R;      
    expo(S);
    produit(m[curr],mess,m[(curr+1)%2]);
    curr = (curr+1)%2;

    for (int i=0; i<n; ++i) {
      cout << m[curr][i];
      if (i<n-1) cout << ' ';
    }
    cout << '\n';
  }    

  return 0;
}

/*
1R0L
L1R0
0L1R
R0L1
*/
