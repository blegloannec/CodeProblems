#include <iostream>
using namespace std;

#define MAX 10001
#define NB 22

typedef long long ent;

ent mem[MAX][NB];
 
ent traite(int n, int j) {
  if (n<0) return 0;
  if (mem[n][j]>=0) return mem[n][j];
  mem[n][j] = (traite(n, j-1) + traite(n-j*j*j, j));
  return mem[n][j];
}


int main() {
  int n;
  for (int i=1; i<NB; i++)
    mem[0][i] = 1;
  for (int i=1; i<MAX; i++)
    mem[i][0] = 0;
  
  for (int i=1; i<MAX; i++) 
    for (int j=1; j<NB; j++)
      mem[i][j] = -1;

  while (cin >> n) {
    cout << traite(n, NB-1) << '\n';
  }

  return 0;
}
