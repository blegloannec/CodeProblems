#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;

struct D {
  int c;
  double e;
  D(int c, double e) : c(c), e(e) {};
};

bool Dcmp(D a, D b) {
  return (a.c<b.c || (a.c==b.c && a.e<b.e));
}

const int C = 100000;
bool P[C];
ent Rad[C];

vector<D> V;

void sieve() {
  P[0] = P[1] = false;
  for (int i=0; i<C; ++i) {
    P[i] = true;
    Rad[i] = 1L;
  }
  for (int i=2; i<C; ++i)
    if (P[i]) {
      Rad[i] = i;
      for (int j=2*i; j<C; j+=i) {
	Rad[j] *= i;
	P[j] = false;
      }
    }
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int comp(int C, double r) {
  int res = 0;
  for (int c=3; c<C; ++c) {
    double cr = pow(c,r);
    if (2*Rad[c] >= cr) continue;
    int step = c%2==0 ? 2 : 1;
    for (int a=1; a<=2; a+=step) {
      ent rad_ac = Rad[a]*Rad[c];
      if (2*rad_ac >= cr) continue;
      int b = c-a;
      double rad = rad_ac*Rad[b];
      if (rad<cr && gcd(a,b)==1)
	V.push_back(D(c,log2(rad)/log2(c)));
    }
    if (6*Rad[c] >= cr) continue;
    for (int a=3; a<=c/2; a+=step) {
      ent rad_ac = Rad[a]*Rad[c];
      if (2*rad_ac >= cr) continue;
      int b = c-a;
      double rad = rad_ac*Rad[b];
      if (rad<cr && gcd(a,b)==1)
	V.push_back(D(c,log2(rad)/log2(c)));
    }
  }
  return res;
}

int main2() {
  int T,L;
  double r;
  sieve();
  scanf("%d\n",&T);
  for (int t=0; t<T; ++t) {
    scanf("%lf %d\n",&r,&L);
    printf("%d\n",comp(L,r));
  }
  return 0;
}

int main() {
  sieve();
  comp(C,1.15);
  sort(V.begin(),V.end(),Dcmp);
  for (vector<D>::iterator i=V.begin(); i!=V.end(); ++i)
    printf("D(%i,%lf),",i->c,i->e);
  fprintf(stderr,"%d\n",(int)V.size());
}

/*
  Si x_i 2 à 2 pee, alors rad(x_1*...*x_n) =  

  Parmi a,b,c(=a+b) exactement 1 pair
  car si au moins 2 pairs, pas 2 à 2 pee
  et si 3 impairs, contradiction sur c=a+b

  Si a premier avec b, alors a (et b) premier avec a+b

  a>=1 et b>=2, donc rad(c)<c/2 et rad(ac)<c/2
  cela semble une petite optim, mais en pratique ça tue complètement
  faisant passer le temps de 90 à <2s !

  Solution : 18407904
*/
