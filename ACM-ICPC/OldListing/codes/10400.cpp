#include <iostream>
using namespace std;

#define RIEN 0
#define PLUS 1
#define MOINS 2
#define FOIS 3
#define DIV 4

#define MAX 100
#define MMAX 64001
#define C 32000


// Prog. dyn.
// t[i][j] = la derniere operation d'une façon d'obtenir j-32000 en considérant les i premiers nombres
int t[MAX][MMAX];
// tableau des valeurs données
int val[MAX];

inline int f(int i, int j) {
  if (i==0) {
    if (j==val[0]+C) return 1;
    else return 0;
  }
  if (j>64000 || j<0) return 0;
  if (t[i][j]>=0) return t[i][j];
  int res = RIEN;
  if (f(i-1,j-val[i])>0)
    res = PLUS;
  else if (f(i-1,j+val[i])>0)
    res = MOINS;
  else if (f(i-1,(j-C)*val[i]+C)>0)
    res = DIV;
  else if (val[i] !=0 && (j-C) % val[i] == 0 && f(i-1,(j-C)/val[i]+C)>0)
    res = FOIS;
  t[i][j] = res;
  return res;
} 

void affiche(int i, int j) {
  if (i>0) {
    if (t[i][j] == PLUS) {
      affiche(i-1,j-val[i]);
      cout << '+' << val[i];
    }
    else if (t[i][j] == MOINS) {
      affiche(i-1,j+val[i]); 
      cout << '-' << val[i];
    }
    else if (t[i][j] == FOIS) {
      affiche(i-1,(j-C)/val[i]+C);     
      cout << '*' << val[i];
    }
    else {
      affiche(i-1,(j-C)*val[i]+C);  
      cout << '/' << val[i];
    }
  }
}


int main() {
  int cas,n,a;
  cin >> cas;
  while (cas-->0) {
    cin >> n;
    for (int i=0; i<n; ++i)
      for (int j=0; j<MMAX; ++j)
        t[i][j] = -1;
    for (int i=0; i<n; ++i) 
      cin >> val[i];
    cin >> a;
    if (f(n-1,a+C) <= 0) cout << "NO EXPRESSION\n";
    else {
      cout << val[0];
      affiche(n-1,a+C);
      cout << "=" << a << '\n';
    }
  }
  
  return 0;
}
