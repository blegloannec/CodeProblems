#include <iostream>
using namespace std;

#define MAX 52

typedef long long ent;

ent mem[MAX];

ent traite(int n) {
  if (mem[n]>=0) return mem[n];
  mem[n] = traite(n-2)+traite(n-1);
  return mem[n];
}


int main() {
  int nb,n;
  cin >> nb;

  mem[0] = 0;
  mem[1] = 2;
  mem[2] = 3;
  for (int i=3; i<MAX; i++)
    mem[i] = -1;

  for (int cas=1; cas<=nb; cas++) {
    cin >> n;
    cout << "Scenario #" << cas << ":\n" << traite(n) << "\n\n";    
  }

  return 0;
}
