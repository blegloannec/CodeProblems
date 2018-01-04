#include <iostream>
using namespace std;

#define MAX 51

typedef long long ent;

ent mem[MAX][MAX];
int m;

ent light(int n, int k) {
  if (mem[n][k]>=0) return mem[n][k];
  ent res = 0;
  for (int i=1; i<=min(m,n-1); i++) {
    res += light(n-i, k-1);
  }
  if ((n<=m)&&(k==1)) res++;
  mem[n][k] = res;
  return res;
}

int main() {
  int n,k;
  while (cin >> n >> k >> m) {
    mem[1][1] = 1;
    for (int j=2; j<=n; j++) 
      mem[1][j] = 0;
    for (int i=2; i<=n; i++) 
      for (int j=1; j<=n; j++) {
	if (j==1) {
	  if (i>m) mem[i][j] = 0;
	  else mem[i][j] = 1;
	}
	else mem[i][j] = -1;
      }
    cout << light(n,k) << '\n';    
  } 
  
  return 0;
}
