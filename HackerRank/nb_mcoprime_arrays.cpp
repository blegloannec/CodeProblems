#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

/*
  on ajoute iterativement les facteurs premiers pi^ai de m
  si l'on connait le nb de m-tableaux de taille n de m
  calculons le nb de m'-tableaux pour m' = m * pi^ai
  pour en fabriquer, on prend un m-tableau dans lequel on
  selectionne un sous-ensemble de cases jamais consecutives
  pour recevoir des p^b avec 1<=b<=a+i
  le nb de telles selections verifie Si(n) = Si(n-1) + ai*Si(n-2)
  (donc on peut calculer ce nb par exponentiation d'une matrice 2x2)
  et il suffit de multiplier le nb courant de m-tableaux par Si(n)
  pour obtenir le nb de m'-tableaux
*/

typedef unsigned long long ent;

const ent P = 1000000007;
const int N = 1000000;
vector<bool> Pr(N,true);
vector<int> LPr;

void sieve() {
  Pr[0] = Pr[1] = false;
  for (int i=2; i<N; ++i)
    if (Pr[i]) {
      LPr.push_back(i);
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

// === Miller-Rabin ===
// multiplication modulo overflow-safe
ent mulmod(ent a, ent b, ent m) {
  a %= m;
  ent ab = 0;
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

// Miller-Rabin deterministe 64 bits
bool witness(ent a, ent n, vector<bool> &b) {
  ent x,d = 1L;
  for (int i=(int)b.size()-1; i>=0; --i) {
    x = d;
    d = mulmod(d,d,n);
    if (d==1 && x!=1 && x!=n-1) return true;
    if (b[i]) d = mulmod(d,a,n);
  }
  return (d!=1);
}

// bases pour Miller-Rabin deterministe 64 bits
// http://miller-rabin.appspot.com/
vector<ent> W {2,325,9375,28178,450775,9780504,1795265022};

bool miller_rabin(ent n) {
  if (n<N) return Pr[n];
  ent m = n-1;
  vector<bool> b;
  while (m>0) {
    b.push_back(((m&1)==1));
    m >>= 1;
  }
  for (vector<ent>::iterator w=W.begin(); w!=W.end(); ++w) {
    if (n == *w) return true;
    if (witness(*w,n,b)) return false;
  }
  return true;
}

struct Matrix2 {
  ent m00,m01,m10,m11;
  Matrix2(ent a=1, ent b=0, ent c=0, ent d=1) {
    m00 = a; m01 = b; m10 = c; m11 = d;
  }
  Matrix2 operator*(const Matrix2 &B) const {
    return Matrix2(((this->m00*B.m00)%P+(this->m01*B.m10)%P)%P,((this->m00*B.m01)%P+(this->m01*B.m11)%P)%P,((this->m10*B.m00)%P+(this->m11*B.m10)%P)%P,((this->m10*B.m01)%P+(this->m11*B.m11)%P)%P);
  }
  Matrix2 pow(ent n) const {
    if (n==0) return Matrix2();
    if ((n&1)==0) return ((*this)*(*this)).pow(n>>1);
    return (*this)*((*this)*(*this)).pow(n>>1);
  }
};

ent coeff(ent a, ent n) {
  Matrix2 M = Matrix2(1,a,1,0).pow(n-1);
  return (((a+1)*M.m00)%P+M.m01)%P;
}

int main() {
  sieve();
  int q;
  cin >> q;
  while (q--) {
    ent n,m;
    cin >> n >> m;
    vector<int> D;
    for (auto ip=LPr.begin(); ip!=LPr.end(); ++ip) {
      ent p = *ip;
      if (m%p==0) {
	int nd = 1;
	m /= p;
	while (m%p==0) {
	  m /= p;
	  ++nd;
	}
	D.push_back(nd);
      }
    }
    if (m>1) {
      // trick: then the remaining m has at most 2 prime factors
      //        m = p or m = p^2 or m = pq
      // and we only need to know in which case we are as we only care
      // about the exponents in the decomposition
      if (miller_rabin(m)) D.push_back(1);
      else {
	ent s = (ent)sqrt(m);
	if (s*s==m) D.push_back(2);
	else {
	  D.push_back(1);
	  D.push_back(1);
	}
      }
    }
    ent res = 1;
    for (auto it=D.begin(); it!=D.end(); ++it)
      res = (res*coeff(*it,n))%P;
    cout << res << endl;
  }
  return 0;
}
