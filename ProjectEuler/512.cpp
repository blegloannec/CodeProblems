#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

/* C++ pour consommer moins de mémoire que Python
   et donc éviter d'avoir à cribler par intervalle.
   On a phi(n^i) = phi(n) * n^(i-1)
   donc f(n) = sum(phi(n^i), i=1..n)
             = phi(n) * sum(n^i, i=0..n-1)
             = phi(n) * (n^n-1)/(n-1)
   
   runs in ~ 2 min 30  :-/
*/

ent expmod(ent x, ent n, ent p) {
  if (n==0) return 1;
  if (n%2==0) return expmod((x*x)%p,n/2,p);
  return (x*expmod((x*x)%p,(n-1)/2,p))%p;
}

void sieve_totient(int N, vector<bool> &P, vector<int> &Totient) {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      Totient[i] = i-1;
      for (int k=2*i; k<N; k+=i) {
	P[k] = false;
	int m = 1;
	int l = k/i;
	while (l%i==0) {
	  l /= i;
	  m *= i;
	}
	Totient[k] *= (i-1)*m;
      }
    }
}

int main() {
  int N = 500000001;
  vector<bool> P(N,true);
  vector<int> Totient(N,1);
  sieve_totient(N,P,Totient);
  ent g = 1;
  for (int n=3; n<N; n+=2)
    g += (Totient[n]*(((expmod(n,n,n+1)-1)/(n-1))%(n+1)))%(n+1);
  cout << g << endl;
  return 0;
}
