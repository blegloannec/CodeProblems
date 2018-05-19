/*
  Notons C(x) = nb d'occurences de la valeur x dans A.
  Le nb de triplets (i,j,k) avec A_k = x est "presque"
  C(x) * sum_{a+b=x} C(a)*C(b).
  "Presque" car i, j et k doivent etre distincts donc les termes
  C(0)*C(x) et C(x)*C(0) de la somme sont incorrects
  ainsi, si x est pair, que le terme C(x/2)*C(x/2).
  Mais il n'est pas trop difficile de corriger le resultat apres coup
  en prenant en compte ces cas particuliers.
  On se ramene donc a calculer une convolution CC(x) = sum_{a+b=x} C(a)*C(b)
  efficacement par FFT.
  Comme -50000<=x<=50000, on decalera les indices de C de D = 50000 et
  on regardera les indices decales CC(_+2D) pour les sommes.
  Le resultat pouvant etre grand, on calculera la FFT/NTT modulo 2 grands
  nombres premiers valides pour cette tache (MOD et MOD2 dans le code)
  et l'on recombinera par theoreme chinois pour le resultat final.
*/

#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

const int N = 1<<18;
const int D = 50000;
vector<ll> C(N,0),C0,C2;

const ll MOD = 1004535809;
// phi(MOD) = MOD-1 = 2^21 * 479
const ll MOD2 = 740294657;
// phi(MOD) = MOD-1 = 2^21 * 353

ll power(ll a, ll b, ll MOD) {
  if (b==0) return 1;
  if ((b&1)==0) return power((a*a)%MOD,b>>1,MOD);
  return (a*power((a*a)%MOD,b>>1,MOD))%MOD;
}

// 3 is a primitive root mod MOD and MOD2
// 3^479 is of order 2^21 for MOD
const ll root = power(3,479,MOD);
const ll root_1 = power(root,MOD-2,MOD);  // inverse mod
const int root_pw = 1<<21;  // order
// 3^353 is of order 2^21 for MOD2
const ll root2 = power(3,353,MOD2);
const ll root_12 = power(root2,MOD2-2,MOD2);  // inverse mod
// these parameters allow us to compute the NTT mod MOD or MOD2
// of any sequence of size 2^k for k<=21

// modular FFT from e-maxx.ru/algo/fft_multiply
// https://www.hackerrank.com/contests/101hack46/challenges/counting-road-networks/editorial
void fft(ll MOD, ll root, ll root_1, int root_pw, vector<ll> &a, bool invert=false) {
  int n = a.size();
  // bit reverse ordering
  for (int i=1, j=0; i<n; ++i) {
    int bit = n >> 1;
    for (; j >= bit; bit>>=1) j -= bit;
    j += bit;
    if (i<j) swap(a[i],a[j]);
  }
  // efficient in-place iterative fft
  for (int len=2; len<=n; len<<=1) {
    ll wlen = invert ? root_1 : root;
    for (int i=len; i<root_pw; i<<=1)
      wlen = (wlen*wlen)%MOD;
    for (int i=0; i<n; i+=len) {
      ll w = 1;
      for (int j=0; j<len/2; ++j) {
	int u = a[i+j],  v = (a[i+j+len/2]*w)%MOD;
	a[i+j] = u+v < MOD ? u+v : u+v-MOD;
	a[i+j+len/2] = u-v >= 0 ? u-v : u-v+MOD;
	w = (w*wlen)%MOD;
      }
    }
  }
  if (invert) {
    int nrev = power(n,MOD-2,MOD);  // inverse mod
    for (int i=0; i<n; ++i)
      a[i] = (a[i]*nrev)%MOD;
  }
}

const ll pq = MOD*MOD2;
const ll u = -170385281;  // bezout for MOD and MOD2
const ll v = 231202690;
const ll up = (((u*MOD)%pq)+pq)%pq;
const ll vq = (v*MOD2)%pq;

// integer overflow safe multiplication (slow)
ll mulmod(ll a, ll b, ll m=pq) {
  ll ab = 0;
  while (b) {
    if (b&1) {
      ab += a;
      if (ab>=m) ab -= m;
    }
    a = (a<<1)%m;
    b >>= 1;
  }
  return ab;
}

ll rev_chinois(ll a, ll b) {
  return (mulmod(b,up)+mulmod(a,vq))%pq;
}

int main() {
  int n;
  scanf("%d",&n);
  for (int i=0; i<n; ++i) {
    int a;
    scanf("%d",&a);
    ++C[a+D];
  }
  C0 = C;
  // FFT
  C[D] = 0;  // on vire completement les 0
  C2 = C;
  fft(MOD,root,root_1,root_pw,C);
  for (int i=0; i<N; ++i) C[i] = (C[i]*C[i])%MOD;
  fft(MOD,root,root_1,root_pw,C,true);
  fft(MOD2,root2,root_12,root_pw,C2);
  for (int i=0; i<N; ++i) C2[i] = (C2[i]*C2[i])%MOD2;
  fft(MOD2,root2,root_12,root_pw,C2,true);
  // Resultats
  ll res = 0, res2 = 0;
  for (int i=-D; i<=D; ++i) {
    if (C0[i+D]==0) continue;
    res = (res + C0[i+D]*C[i+2*D])%MOD;
    res2 = (res2 + C0[i+D]*C2[i+2*D])%MOD2;
    // correction pour x pair non 0 des x/2 + x/2 = x
    if (i!=0 && i%2==0) {
      res = (res - C0[i+D]*C0[i/2+D])%MOD;
      res2 = (res2 - C0[i+D]*C0[i/2+D])%MOD2;
    }
  }
  // Cas particulier des 0
  if (C0[D]>0) {
    // cas des 0 + x = x + 0 = x
    for (int i=-D; i<=D; ++i) {
      if (i==0) continue;
      res = (res + 2*C0[D]*C0[i+D]*(C0[i+D]-1))%MOD;
      res2 = (res2 + 2*C0[D]*C0[i+D]*(C0[i+D]-1))%MOD2;
    }
    // cas du 0 + 0 = 0
    if (C0[D]>=3) {
      res = (res + C0[D]*(C0[D]-1)*(C0[D]-2))%MOD;
      res2 = (res2 + C0[D]*(C0[D]-1)*(C0[D]-2))%MOD2;
    }
  }
  /* 
     On recombine par theoreme chinois 
     NB : on aurait pu le faire sur chaque valeur juste apres les 2 FFT
     afin de ne pas avoir les corrections en double, mais cela requiert
     une multiplication overflow-safe lente, donc il est preferable
     de le faire le moins possible de fois.
  */
  res = rev_chinois(res,res2);
  printf("%lld\n",res);
  return 0;
}
