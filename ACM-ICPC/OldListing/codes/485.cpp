#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

#define TAILLE 8

struct bigint {
  bigint() {init();}
  void init (int n=0) {
    m[0] = n;
    for (int i=1; i<TAILLE; ++i)
      m[i] = 0;
  }

  bigint& operator+(const bigint &op) const {
    bigint *res = new bigint();
    int carry=0;
    for (int i=0; i<TAILLE-1; ++i) {
      res->m[i] = carry+m[i]+op.m[i];
      carry = res->m[i]/1000000000;
      res->m[i] = res->m[i]%1000000000;
    }
    return *res;
  }

  void affiche() {
    int i = TAILLE-1;
    while (m[i] == 0) --i;
    printf("%d",m[i]);
    --i;
    while (i>=0) {
      printf("%09d",m[i]);
      --i;
    }
    //    printf("\n");
  }

  int m[TAILLE];
};


vector<bigint> v[2];

int main() {
  bigint b;
  b.init(1);
  v[0].push_back(b);
  for (int i=0; i<=204; ++i) {
    bigint n1;
    n1.init(1);
    v[(i+1)%2].push_back(n1);
    v[(i+1)%2].push_back(n1);
    for (int j=0; j<(int)v[i%2].size(); ++j) {
      if (j>0) cout << ' ';
      v[i%2][j].affiche();      
    }
    for (int j=0; j<(int)v[i%2].size()-1; ++j) {
      v[(1+i)%2][j+1].init();
      v[(1+i)%2][j+1] = v[i%2][j+1]+ v[i%2][j];
    }
    cout << '\n';
  }
  return 0;
}
