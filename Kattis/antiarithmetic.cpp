/*
  Notons D(i,j) = A[j]-A[i].
  A[i] est le centre d'un triplet arithmetique ssi
  il existe l<i<r tels que D(l,i) = D(i,r) = -D(r,i).
  Comme A est une permutation, si l'on note w(i) = min(A[i],n-1-A[i]),
  alors pour chaque 0 < d <= w(i), il existe exactement deux indices
  a(d) et b(d) portant les valeurs A[a(d)] = A[i]-d et A[b(d)] = A[i]+d.
  On a un triplet arith. de raison d ssi a(d) et b(d) sont de part
  et d'autre de i.
  S'il n'y a pas de tel triplet, alors les a(d) et b(d) pour chaque d
  sont toujours du meme cote de i et
  DL(i) = Sum_{l<i et |D(l,i)|<=w(i)} D(l,i) = 0
  (idem a droite, mais c'est evidemment redondant par complementarite).
  En effet, pour chaque d tel que a(d)<i et b(d)<i,
  les contributions de l = a(d) et l = b(d) a la somme sont opposees.
  
  Une CN pour antiarith. est donc : pour tout i, DL(i) = 0
  On supposera ici (sans preuve complete, valide sur un grand nb d'exemples
  generes aleatoirement) que c'est une CNS.
*/

#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

/* Fenwick Trees */
typedef int ent;
struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}


int n;
vector<int> A;

bool antiarith() {
  Fenwick C(n),S(n);
  for (int i=0; i<n; ++i) {
    ++A[i];  // only to avoid 0 (forbidden in our Fenwick implementation)
    int w = min(A[i]-1,n-A[i]);
    int c = C.prefix_sum(A[i]+w)-C.prefix_sum(A[i]-w-1);
    int s = S.prefix_sum(A[i]+w)-S.prefix_sum(A[i]-w-1);
    if (s!=c*A[i]) return false;
    C.add(A[i],1);
    S.add(A[i],A[i]);
  }
  return true;
}

int main() {
  while (true) {
    scanf("%d",&n);
    if (n==0) break;
    scanf(":");
    A.resize(n);
    for (int i=0; i<n; ++i) scanf("%d",&A[i]);
    if (antiarith()) printf("yes\n");
    else printf("no\n");
  }
  return 0;
}
