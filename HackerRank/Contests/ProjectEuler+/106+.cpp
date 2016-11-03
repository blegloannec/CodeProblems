#include <iostream>
#include <vector>
using namespace std;

/* Utilisation de C++ +/- indispensable ici, sauf erreur un code identique
   ne passe pas en Python (a <2s pres), alors qu'en C++ il ne prend qu'un
   quart environ du temps imparti...

   Comme la condition 2 est deja verifiee,
   il suffit de tester les sous-ensembles de meme cardinal.
   Si de plus on veut tester A = {X_a1 < ... < X_an} et B = {X_b1 < ... < X_bn}
   mais que pour tout i, ai < bi, alors X_ai < X_bi, alors S(A) < S(B),
   donc ce n'est pas la peine de tester A et B.
   Autrement dit on doit tester seulement les sous-ensembles pour lesquels les
   ensembles d'indices "se croisent" : il existe i,j tels que ai<bi et aj>bj.

   Paires d'ensembles de n elements a tester :
     - choisir 2n elements (tries, a repartir en 2 sous-ensembles de n)
     - construisons A et B de taille n "se croisant"
       on met arbitrairement le premier element (le plus petit) dans A
       1. Si l'on compte +1 lorsqu'on met dans A et -1 lorsqu'on
          met dans B, le compteur commence a 0, puis 1 au premier element,
          doit terminer a 0 (repartition equitable n/n) et il y a croisement
          ssil existe un instant auquel le compteur est strictement negatif.
       2. Avec cette vision des choses, en ecrivant "(" les A et ")" les B
          on cherche en fait exactement les mots de taille 2n avec n "(" et n ")"
          qui sont mal parentheses ! Les mots bien parentheses sont comptes par
	  les nbs de Catalan : https://en.wikipedia.org/wiki/Catalan_number
       3. De facon equivalente, en considerant un carre nxn, il s'agit des
          chemins du coin inferieur gauche au superieur droit qui franchissent
          strictement la diagonale. Ie. le complementaire des "Dyck paths" :
          http://mathworld.wolfram.com/DyckPath.html
       4. C'est aussi le complementaire des non-crossing partitions :
          https://en.wikipedia.org/wiki/Noncrossing_partition
       5. etc
       Bilan : le nb que l'on recherche est
       binom(2n-1,n) - Cn = binom(2n-1,n) - binom(2n,n)/(n+1)
                          = binom(2n-1,n+1)
*/

typedef long long ent;
const ent P = 1000000007;
vector<ent> F,InvF;

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

ent binom(ent n, ent p) {
  return (((F[n]*InvF[p])%P)*InvF[n-p])%P;
}

ent count(ent n) {
  ent s = 0;
  for (ent k=2; k<=n/2; ++k)
    s = (s + (binom(n,2*k)*binom(2*k-1,k+1))%P)%P;
  return s;
}

int main() {
  /* pre-calcul des factorielles modulo et de leurs
     inverses momdulaires */
  F.push_back(1);
  InvF.push_back(1);
  for (ent i=1; i<=1000000; ++i) {
    F.push_back((F[i-1]*i)%P);
    InvF.push_back(inv_mod(F[i],P));
  }
  ent T,N;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    cout << count(N) << endl;
  }
  return 0;
}
