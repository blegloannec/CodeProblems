#include <iostream>
using namespace std;

#define MAX 101
#define CAP 200
#define INFTY 1000000000

int kmax;
int C[MAX];
int S[MAX];
int mem[MAX][CAP+1];

bool init() {
  for (int e=0; e<=CAP; e++) {
    if (e==CAP/2-S[1]) mem[1][e] = 0;
    else mem[1][e] = INFTY;
  }
  for (int k=2; k<=kmax; k++) 
    for (int e=0; e<=CAP; e++) 
      mem[k][e] = -1;
  return (CAP/2-S[1]>=0);
}


/* Cout minimal pour arriver a la kieme station
   avec la quantite E
*/
int cost(int k, int E) {
  if (mem[k][E]>=0) return mem[k][E];
  int d = S[k]-S[k-1];
  int res = INFTY;
  if (E+d<=CAP) {
    for (int e=0; e<=E+d; e++)
      res = min(res,cost(k-1,e)+(E-e+d)*C[k-1]);
  }
  mem[k][E] = res;
  return res;
}

int main() {
  int nb,dist,d,p,res;
  char buff[100];
  cin >> nb;
  
  while (cin >> dist) {
    cin.getline(buff,sizeof(buff));
    cin.getline(buff,sizeof(buff));
    kmax = 1;
    while (sscanf(buff,"%d %d",&d,&p) == 2) {
      C[kmax] = p;
      S[kmax] = d;
      ++kmax;
      cin.getline(buff,sizeof(buff));
    }
    S[kmax] = dist;
    if (kmax==1) {
      if (dist==0) cout << p << '\n';
      else cout << "Impossible\n";
    }
    else {
      if (init()) {
	res = cost(kmax,CAP/2);
	if (res>=INFTY) cout << "Impossible\n";
	else cout << res << '\n';
      }
      else cout << "Impossible\n";
    }
  }
  

  return 0;
}
