#include <iostream>
#include <vector>
using namespace std;

/*
  f(k,n) = sum( i^k, i=1..n )
  S(k,n) = sum( f(k,m), m=1..n )
         = sum( i^k, 1<=i<=m<=n )
         = sum( (n-i+1)i^k, i=1..n )
         = (n+1)f(k,n) - f(k+1,n)
  Il suffit donc de savoir calculer f(k,.) ef f(k+1,.).
  https://en.wikipedia.org/wiki/Faulhaber%27s_formula
  f(k,X) est un polynome de degre k.
  On pourrait utiliser une interpolation de Lagrange (en O(k^2)
  pour k = 10000 pour chaque modulo)...
  On peut aussi calculer explicitement le polynome de Faulhaber en
  calculant les coeff. a partir des nombres de Bernoulli.
  https://en.wikipedia.org/wiki/Bernoulli_number
  Le calcul de ces nombres est neanmoins en O(k^2) pour chaque modulo.
  Cela prend < 4min avec -O3

  Autre methode plus basique mais qui fonctionne bien ici :
  f(k,n) = f(k,n%p) mod p  (car polynome en n)
  a fortiori f(k,p) = 0 mod p
  Or ici on remarque que n%p est toujours tres proche de p
  (vrai pour le n et les p demandes, faux en regle generale)
  donc f(k,n%p) = -sum( i^k, i=n%p+1..p ) mod p
  et cette somme a toujours relativement peu de termes
  donc on peut la calculer directement.
  Cela donne la solution en ~13s avec -O3
  (mais c'est tres contextuel comme methode)
*/

typedef long long ent;
const int k = 10000;

ent expo(ent a, int n, ent p) {
  if (n==0) return 1;
  if (n%2==0) return expo((a*a)%p,n/2,p);
  return (a*expo((a*a)%p,(n-1)/2,p))%p;
}

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

vector<ent> F(k+4,1),Finv(k+4,1),Inv(k+4);
void gen_fact(ent p) {
  for (ent i=1; i<k+4; ++i) {
    F[i] = (F[i-1]*i)%p;
    Finv[i] = inv_mod(F[i],p);
    Inv[i] = inv_mod(i,p);
  }
}

ent binom(int n, int p, ent m) {
  return (F[n]*((Finv[p]*Finv[n-p])%m))%m;
}

vector<ent> B(k+3);
void gen_bernoulli(ent p) {
  B[0] = 1;
  for (int m=1; m<k+3; ++m) {
    B[m] = 0;
    for (int k=0; k<m; ++k)
      B[m] = (B[m] + (binom(m,k,p)*((B[k]*Inv[m-k+1])%p))%p)%p;
    B[m] = (1-B[m]+p)%p;
  }
}

ent f(int m, ent n, ent p) {
  ent s = 0;
  for (int k=0; k<=m; ++k)
    s = (s + ((binom(m+1,k,p)*((B[k]*expo(n,m+1-k,p))%p))%p))%p;
  s = (s*Inv[m+1])%p;
  return s;
}

bool prime(ent n) {
  for (int i=3; i*i<=n; i+=2)
    if (n%i==0) return false;
  return true;
}

// Methode 1
int main0() {
  ent n = 1000000000000LL;
  ent res = 0;
  for (ent p=2000000001; p<=2000002000; p+=2)
    if (prime(p)) {
      ent np = n%p;
      cout << p << endl;
      gen_fact(p);
      gen_bernoulli(p);
      res += ((((((np+1)*f(k,np,p))%p) - f(k+1,np,p))%p) + p)%p;
    }
  cout << res << endl;
  return 0;
}

// Methode 2 (tres contextuelle)
int main() {
  ent n = 1000000000000LL;
  ent res = 0;
  for (ent p=2000000001; p<=2000002000; p+=2)
    if (prime(p)) {
      ent np = n%p;
      ent f0 = 0, f1 = 0;
      for (ent i=np+1; i<p; ++i) {
	ent ik = expo(i,k,p);
	f0 = (f0 + ik)%p;
	f1 = (f1 + ((i*ik)%p))%p;
      }
      f0 = p-f0;
      f1 = p-f1;
      res += ((((((np+1)*f0)%p) - f1)%p) + p)%p;
    }
  cout << res << endl;
  return 0;
}
