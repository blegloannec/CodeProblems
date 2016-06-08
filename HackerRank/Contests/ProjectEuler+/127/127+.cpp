#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ent;
typedef pair<ent,int> couple;

const int C = 100000;
vector<bool> P = vector<bool>(C,true);
vector<couple> Rad = vector<couple>(C);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i<C; ++i) Rad[i] = couple(1L,i);
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

ent comp(int C, double r) {
  ent res = 0;
  for (int c=3; c<C; ++c) {
    double cr = pow(c,r);
    if (2*Rad[c] >= cr) continue;
    int step = 2 -c%2;
    for (int a=1; a<=2; a+=step) {
      ent rad_ac = Rad[a]*Rad[c];
      if (2*rad_ac >= cr) continue;
      int b = c-a;
      if (rad_ac*Rad[b]<cr && gcd(a,b)==1) res += c;
    }
    // a>2
    if (step==1) {if (6*Rad[c] >= cr) continue;}
    else if (15*Rad[c] >= cr) continue;
    for (int a=3; a<=c/2; a+=step) {
      ent rad_ac = Rad[a]*Rad[c];
      if (2*rad_ac >= cr) continue;
      int b = c-a;
      if (rad_ac*Rad[b]<cr && gcd(a,b)==1) res += c;
    }
  }
  return res;
}

int main() {
  int T,L;
  double r;
  sieve();
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> r >> L;
    cout << comp(L,r) << endl;
  }
  return 0;
}

/*
  Si x_i 2 à 2 pee, alors rad(x_1*...*x_n) = rad(x_1)*...*rad(x_n)

  Parmi a,b,c(=a+b) exactement 1 pair
  (car si au moins 2 pairs, pas 2 à 2 pee
  et si 3 impairs, contradiction sur c=a+b)
  donc lorsque c pair, on peut ne parcourir que les a impairs.

  Si a premier avec b, alors a (et b) premier avec a+b

  a>=1 et b>=2, donc rad(c)<c/2 et rad(ac)<c/2
  cela semble une petite optim, mais en pratique ça tue complètement
  faisant passer le temps de 90 à <2s !

  lorsque a>2, on peut être sûr que rad(a)*rad(b)>=6 donc on peut tester
  rad(c)>=c/6
*/
