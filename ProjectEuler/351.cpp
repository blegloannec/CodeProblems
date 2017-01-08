#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

/*
  Similaire au pb 72 (compter les fractions)
  Au sein d'une des 6 branches, on a sur la n-ieme "ligne"
  n+1 points correspondant a des directions qu'on peut associer
  aux fractions 0/n, 1/n, 2/n, ..., n/n.
  Un point est cache si sa fraction etait deja presente avec un
  denominateur plus faible, ie. s'il n'est pas premier avec n.
  On deduit le resultat de la somme des indicatrices d'Euler.
  
  runs in < 5s with -O3
*/

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
  int N = 100000000;
  vector<bool> P(N+1,true);
  vector<int> Totient(N+1,1);
  sieve_totient(N+1,P,Totient);
  ent g = 3;
  for (int n=2; n<=N; ++n)
    g += Totient[n];
  cout << 6*(((ent)N+1)*((ent)N+2)/2-g) - 6*(N-1) << endl;
  return 0;
}
