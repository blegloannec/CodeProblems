#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
typedef pair<int,int> couple;

/*
  Le developpement de 1/n est ultimement periodique.
  Il est strictement periodique (pour 1/n) si n premier avec 10.
  Sinon la periode est la meme que pour n' obtenu en retirant les
  facteurs 2 et 5, on peut donc toujours supposer n premier avec 10.
  La periode L(n) est l'ordre de 10 dans le groupe multiplicatif de Z/nZ.
  C'est en particulier un diviseur de phi(n) (ou plus finement de la
  fonction lambda de Carmichael).
  Si n = prod( pi^ai ) decomposition primale, alors
  L(n) = ppcm( L(pi^ai) )
  En revanche, L(pi^ai) est presque toujours L(pi).pi^(ai-1) mais
  il y a des exceptions, et L(pi) n'est pas forcement pi-1 (ce n'est
  le cas que pour les premiers qui engendrent les nb cycliques, cf pb 358).

  runs in < 1 min with -O3
*/

const int N = 100000001;
vector<bool> P(N,true);
vector<int> F(N,1);
vector<int> L(N,1);

ent expmod(ent x, ent n, ent m) {
  if (n==0) return 1;
  if (n%2==0) return expmod((x*x)%m,n/2,m);
  return (x*expmod((x*x)%m,(n-1)/2,m))%m;
}

ent gcd(ent a, ent b) {
  return b==0?a:gcd(b,a%b);
}

ent lcm(ent a, ent b) {
  return a*b/gcd(a,b);
}

void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

void decomp(int n, vector<couple> &D) {
  int p = F[n];
  n /= p;
  int m = 1;
  while (n%p==0) {
    n /= p;
    ++m;
  }
  D.push_back(couple(p,m));
  if (n>1) decomp(n,D);
}

void divisors(int n, vector<int> &Divs) {
  Divs.push_back(1);
  vector<couple> D;
  decomp(n,D);
  for (vector<couple>::iterator it=D.begin(); it!=D.end(); ++it) {
    int l = Divs.size();
    int f = it->first;
    for (int a=1; a<=it->second; ++a) {
      for (int i=0; i<l; ++i)
	Divs.push_back(Divs[i]*f);
      f *= it->first;
    }
  }
  sort(Divs.begin(),Divs.end());
}

int lambda(int n) {
  int p = F[n];
  int f = p;
  int m = n/p;
  while (m%p==0) {
    m /= p;
    f *= p;
  }
  if (m==1) { // puissance d'un nb premier
    if (p==2 || p==5) L[n] = 1; // cas particulier
    else {
      vector<int> D;
      int phi = (p-1)*(n/p);
      divisors(phi,D);
      for (vector<int>::iterator it=D.begin(); it!=D.end(); ++it)
	if (expmod(10,*it,n)==1) {
	  L[n] = *it;
	  break;
	}
    }
  }
  else L[n] = lcm(L[f],L[m]);
  return L[n];
}

int main() {
  sieve_smallest_factor();
  ent S = 0;
  for (int n=3; n<N; ++n) {
    int m = n;
    while (F[m]==2 || F[m]==5) m /= F[m]; // cas particulier
    if (m>1) S += lambda(n);
  }
  cout << S << endl;
  return 0;
}
