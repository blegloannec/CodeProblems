#include <iostream>
using namespace std;

/*
  une configuration solution vue comme une matrice n x n de 0/1
  est une matrice de permutation avec la contrainte supplementaire
  suivante : deux reines ne sont pas sur la meme (anti-)diagonale
*/

// C the colums mask, (A)D the (anti-)diagonal mask
int queens(int n, int i=0, int C=0, int D=0, int AD=0) {
  if (i==n) return 1;
  int res = 0;
  for (int a=0; a<n; ++a) {
    int CA = 1<<a;
    int DA = 1<<(a+i);
    int ADA = 1<<(n-1+a-i);
    if (C&CA || D&DA || AD&ADA) continue;
    res += queens(n,i+1,C|CA,D|DA,AD|ADA);
  }
  return res;
}

int main() {
  int n;
  cin >> n;
  cout << queens(n) << endl;
  return 0;
}
