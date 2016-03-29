#include <iostream>
using namespace std;

typedef long long ent;

const int C = 120000;
bool P[C];
ent Rad[C];

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

int main() {
  sieve();
  int res = 0;
  for (int c=3; c<C; ++c) {
    if (2*Rad[c] >= c) continue;
    int step = c%2==0 ? 2 : 1;
    for (int a=1; a<=c/2; a+=step) {
      ent rad_ac = Rad[a]*Rad[c];
      if (2*rad_ac >= c) continue;
      int b = c-a;
      if (rad_ac*Rad[b]<c && gcd(a,b)==1) res += c;
    }
  }
  cout << res << endl;
  return 0;
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
