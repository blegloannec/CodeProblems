#include <iostream>
using namespace std;

typedef unsigned short ent;
const ent A = 4;
const ent M = 1<<15;
ent c = 1;
ent memo[A+1][M];

ent f(ent a=A, ent b=1) {
  if (memo[a][b]==M) {
    if (a==0) memo[a][b] = (b==M-1 ? 0 : b+1);
    else if (b==0) memo[a][b] = f(a-1,c);
    else memo[a][b] = f(a-1,f(a,b-1));
  }
  return memo[a][b];
}

int main() {
  for (ent r=1; r<M; ++r) {
    for (int i=0; i<=A; ++i)
      for (int j=0; j<M; ++j) memo[i][j] = M;
    c = r;
    if (f()==6) cout << r << endl;
  }
  return 0;
}
