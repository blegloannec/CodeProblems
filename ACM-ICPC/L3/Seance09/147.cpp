/* Morale de ce probleme : 
    - jamais de float, toujours des double
    - utiliser (int)round() pour caster un flottant en entier avec precision
*/
#include <iostream>
#include <cmath>
using namespace std;

#define MAX 30001

typedef long long ent;

int money[12] = {0,5,10,20,50,100,200,500,1000,2000,5000,10000};

ent mem[MAX][12];


// Nb de facons de former la somme S avec
// les p premieres pieces
ent nb(int S, int p) {
  ent res;
  if (S<0) return 0;
  if (mem[S][p]>=0) return mem[S][p];
  res = nb(S-money[p],p) + nb(S,p-1);
  mem[S][p] = res;
  return res;
}

int main() {
  double in;
  int n;

  mem[0][0] = 1;
  for (int i=1; i<MAX; i++) {
    mem[i][0] = 0;
    for (int j=1; j<12; j++) {
      mem[0][j] = 1;
      mem[i][j] = -1;
    }
  }

  while (cin >> in) {
    if (in==0) return 0;
    n = (int)round(100*in);
    printf("%6.2f%17Ld\n",in,nb(n,11));
  }
  
  return 0;
}
