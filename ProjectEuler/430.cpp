#include <iostream>
#include <iomanip>
using namespace std;

/*
  N^2 tirages possibles.
  Le disque 1<=n<=N est flippe par 2*n*(N-n+1)-1 tirages (-1 pour le A=B=n).
  Notons p la proba qu'il soit flippe, la probabilite qu'il soit blanc apres
  M tours W(M) = W(M-1)*(1-p) + (1-W(M-1))*p = W(M-1)*(1-2p) + p
  Soit W'(M) = W(M) - 1/2 verifiant W'(M) = (1-2p)*W'(M-1)
  W(0) = 1 donc W'(0) = 1/2
  et W'(M) = 1/2*(1-2p)^M
  d'ou W(M) = 1/2*(1-2p)^M + 1/2

  On fait ici le calcul sans approximation
  (developpement limite par exemple)

  runs in ~90s with -O3
*/

double expo(double x, int n) {
  if (n==0) return 1.;
  else if (n%2==0) return expo(x*x,n/2);
  else return x*expo(x*x,(n-1)/2);
}

int main() {
  long long N = 10000000000L;
  double Nf = N;
  double N2 = Nf*Nf;
  int M = 4000;
  double E = 0.;
  for (long long n=1; n<=N/2; ++n) {
    double nf = n;
    double p = (2*nf*(Nf-nf+1)-1)/N2;
    double w = 0.5*expo(1-2*p,M)+0.5;
    E += 2*w;
  }
  cout << setiosflags(ios::fixed) << setprecision(3) << E << endl;
  return 0;
}
