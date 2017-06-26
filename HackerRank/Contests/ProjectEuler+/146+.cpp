#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

const int N = 1000000;
vector<bool> Pr(N,true);
void sieve() {
  Pr[0] = Pr[1] = false;
  for (int i=2; i*i<N; ++i)
    if (Pr[i])
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
}

// multiplication modulo overflow-safe
// (pour a<m, sinon ajouter "a %= m;" au debut)
ent mulmod(ent a, ent b, ent m) {
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
  
vector<int> P;
vector<bool> A(41);
ent amin,amax;

bool test(ent n) {
  ent n2 = n*n;
  for (ent a=amin; a<=amax; ++a)
    if (miller_rabin(n2+a)!=A[a]) return false;
  return true;
}

int main() {
  sieve();
  int i = 2;
  // 1000 nb premiers pour le pre-calcul
  while (P.size()<1000) {
    if (Pr[i]) P.push_back(i);
    ++i;
  }
  int T,L;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> L;
    vector<int> B(6);
    fill(A.begin(),A.end(),false);
    for (int i=0; i<6; ++i) {
      cin >> B[i];
      A[B[i]] = true;
      if (i==0) amin = B[i];
      else if (i==5) amax = B[i];
    }
    // pre-calcul pour aller tres vite
    // PP[i][r] est mis a faux si le i-eme nb premier p_i divise
    // au moins l'un des r^2 + a_k
    // un nb n est directement elimine si l'un des PP[i][n%p_i] est faux
    // sinon on lance le test complet (lent) utilisant Miller-Rabin
    vector< vector<bool> > PP(P.size());
    for (unsigned int i=0; i<P.size(); ++i) {
      PP[i].resize(P[i],true);
      for (int r=0; r<P[i]; ++r)
	for (int j=0; j<6; ++j)
	  if ((r*r+B[j])%P[i]==0) {
	    PP[i][r] = false;
	    break;
	  }
    }
    ent S = 0;
    for (ent n=1; n<L; ++n) {
      bool pp = true;
      for (unsigned int i=0; i<P.size(); ++i)
	if (n*n>P[i] && !PP[i][n%P[i]]) {
	  pp = false;
	  break;
	}
      if (pp && test(n)) S += n;
    }
    cout << S << endl;
  }
  return 0;
}
