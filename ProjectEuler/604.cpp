#include <iostream>
#include <vector>
using namespace std;

/*
  par exemple pour N = 11, on peut prendre les pentes
  successives 1/3, 1/2, 1/1, 3/2, 2/1, 3/1
  ce qui donne 7 points de l'optimum partant de (0,0)
  pour F(n), il s'agit de trouver une plus grande sequence
  strictement croissante de fractions irreductibles telles que
  la somme des numerateurs (deplacement vertical) et la somme
  des denominateurs (deplacement horizontal) soient <= N
  pour l'exemple 1+1+1+3+2+3 = 11 et 3+2+1+2+1+1 = 10
  la sequence partant de (0,0) aboutit en (10,11) <= (11,11)
  generateur des diviseurs (a partir des decomp)
*/

typedef long long ll;
typedef pair<int,int> couple;

const ll n = 1000000000000000000LL; // input

const int N = 2500000;
vector<bool> P(N,true);
vector<int> F(N);

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
  vector<couple> D;
  decomp(n,D);
  Divs.push_back(1);
  for (vector<couple>::iterator it=D.begin(); it!=D.end(); ++it) {
    int l = Divs.size();
    int f = it->first;
    for (int a=1; a<=it->second; ++a) {
      for (int i=0; i<l; ++i)
	Divs.push_back(Divs[i]*f);
      f *= it->first;
    }
  }
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  sieve_smallest_factor();
  vector<int> C(N,0);
  // C[i] = nb de couples (a,b) tq i = a+b et gcd(a,b) = 1
  C[2] = 1;
  for (int i=3; i<N; ++i) {
    // si i = a+b avec gcd(a,b) = d > 1, alors d | i
    // a = da', b = db', i/d = a'+b' avec gcd(a',b') = 1
    // il y a donc C[i/d] tels couples
    // ainsi C[i] = i-1 - sum( C[i/d] pour 1 < d | i )
    C[i] = i-1;
    vector<int> D;
    divisors(i,D);
    for (vector<int>::iterator id=D.begin(); id!=D.end(); ++id)
      if (0<*id && *id<i) C[i] -= C[*id];
  }
  ll s = 1, ab = 3, f = 1;
  while (s<=n) {
    if (s+(C[ab]*ab)/2<=n) {
      // on traite d'un coup toutes les fractions a/b tq a+b = ab
      f += C[ab];
      s += (C[ab]*ab)/2;
    }
    else {
      // on les parcourt 1 a une jusqu'a arriver a s = n
      for (int a=1; a<=ab/2; ++a) {
	int b = ab-a;
	if (a==b) continue;
	if (gcd(a,b)==1) {
	  ++f;
	  s += a;
	  if (s>n) break;
	  ++f;
	  s += b;
	}
	if (s>n) break;
      }
    }
    ++ab;
  }
  cout << f-1 << endl;
  return 0;
}
