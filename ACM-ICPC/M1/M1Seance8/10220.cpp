#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

#define TAILLE 600

int t[1001];

int chiffres(int m){
  int res=0;  
  while (m!=0){
    res+= m%10;
    m/=10;
  }
  return res;
}

struct bigint {
  bigint() {init();}
  // requires n < 1 000 000 000;
  void init(int n=0) {
    m[0] = n;
    for (int i = 1; i < TAILLE; ++i)
      m[i] = 0;
  }

  // requires operandes <= (1 000 000 000^TAILLE - 1) / 2;
  bigint& operator+(const bigint &op) const {
    bigint *res = new bigint();
    int carry=0;
    for (int i = 0; i < TAILLE-1; ++i) {
      res->m[i] = carry+m[i]+op.m[i];
      carry = res->m[i]/1000000000;
      res->m[i] = res->m[i]%1000000000;
    }
    return *res;
  }
  // requires operandes <= 1 000 000 000^(TAILLE/2) - 1;
  bigint& operator*(const bigint &op) const {
    bigint *res = new bigint();
    long long carry=0;
    for (int i = 0; i < TAILLE; ++i)
      for (int j = max(i-TAILLE/2, 0), l = min(TAILLE/2, i+1); j < l; ++j) {
        carry = (long long)(m[j]) * op.m[i-j];
        for (int k = i; carry; ++k) {
          carry += res->m[k];
          res->m[k] = carry%1000000000;
          carry /= 1000000000;
        }
      }
    return *res;
  }
  void affiche() {
    int i = TAILLE-1;
    while (m[i] == 0) --i;
    if (i<0) {
      printf("0\n");
      return;
    }
    printf("%d", m[i]);
    --i;
    while (i >= 0) {
      printf("%09d", m[i]);
      --i;
    }
    printf("\n");
  }
  int m[TAILLE];

  int somme() {
    int i = TAILLE-1;
    while (m[i] == 0) --i;
    if (i<0) return 0;
    int res = chiffres(m[i]);
    --i;
    while (i >= 0) {
      res += chiffres(m[i]);
      --i;
    }
    return res;
  }

};


int main() {
  bigint a,b;
  int s;
  a.init(1);
  t[0] = 1;
  for (int i=1;i<=1000;++i){
    b.init(i);
    a = a*b;
    t[i] = a.somme();
  }
  while (cin >> s)
    cout << t[s] << '\n';
}

