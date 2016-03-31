#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

#define TAILLE 60

struct bigint {
  bigint() {init();}
  // requires n < 1 000 000 000;
  void init(int n=0) {
    m[0] = n;
    for (int i = 1; i < TAILLE; ++i)
      m[i] = 0;
  }
  void init(string s) {
    int starti;
    for (int i = 0; i < TAILLE; ++i) m[i] = 0;
    int start = ((int)s.size()-1)/9;
    for (int k=start; k>=0; --k) {
      if (k==start) starti = ((int)s.size()-1)%9;
      else starti = 8;
      for (int i=starti; i>=0; --i) 
	m[k] = 10*m[k] + (int)s[(int)s.size()-1-(k*9+i)]-(int)'0';
    }
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
};


int main() {
  bigint a,b,c;
  string s1,s2;
  while (cin >> s1 >> s2) {
    a.init(s1);
    //a.affiche();
    b.init(s2);
    //b.affiche();
    c = a*b;
    c.affiche();
  }
  return 0;
}
