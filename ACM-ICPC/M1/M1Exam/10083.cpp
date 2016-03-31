#include <iostream>
using namespace std;

bool overflow=false;

#define TAILLE 100
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
    for (int i=TAILLE-1; i>=12; --i)
      if (m[i]!=0) overflow=true;
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
    for (int i=TAILLE-1; i>=12; --i)
      if (m[i]!=0) overflow=true;
    return *res;
  }
  void affiche() {
    int i = TAILLE-1;
    while (m[i] == 0) --i;
    if (i<0) {
      printf("0\n");
      return;
    }
    if (i>=11) {
      if (m[11]>0 || i>11) {
        cout << "is not an integer with less than 100 digits.\n";
        return;
      }
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

bigint exp(bigint i, int p) {
  bigint tmp;
  tmp.init(1);
  if (p==0) return tmp;
  if (p==1) return i;
  if (p%2==0) {
    tmp = exp(i,p/2);
    return tmp*tmp;
  }
  else {
    tmp = exp(i,p/2);
    return i*tmp*tmp;
  }

}

int main() {
  int t,a,b,q;
  while (cin >> t >> a >> b) {
    if (b == 0 || t==1) {
      cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) is not an integer with less than 100 digits.\n";
    }
    else if (a==0) {
      cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) 0\n";
      
    }
    else if (a==b) {
      cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) 1\n";
    }
    else {
      q = a%b;    
    if (q!=0 || a<b) {
      cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) is not an integer with less than 100 digits.\n";
    }
    else {
      bigint bt;
      bt.init(t);
      bigint base = exp(bt,b);
      bigint res;
      res.init(1);
      bigint un;
      un.init(1);
      for (int i=1; i<=a/b-1; ++i) {
        res = res*base;
        if (overflow) {
          cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) is not an integer with less than 100 digits.\n";
          break;
        }
        res = res  + un; 
        if (overflow) {
          cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) is not an integer with less than 100 digits.\n";
          break;
        }
      }
      if (!overflow) {
        cout << '(' << t << '^' << a << "-1)/(" << t << '^' << b << "-1) ";
        res.affiche();
      }
      //      cout << "\n";
    }
    }
    overflow=false;
  }
  return 0;
}
