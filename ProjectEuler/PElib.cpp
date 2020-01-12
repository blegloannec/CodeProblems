typedef long long ent;
typedef pair<int,int> couple;

ent expmod(ent x, ent n, ent m) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

ent gcd(ent a, ent b) {
  return b==0?a:gcd(b,a%b);
}

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

vector<bool> P(N,true);
void sieve() {
  P[0] = P[1] = false;
  for (long long i=2; i*i<N; ++i)
    if (P[i])
      for (long long k=i*i; k<N; k+=i)
	P[k] = false;
}

vector<bool> P(N,true);
vector<int> F;
void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (long long i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (long long k=i*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

vector<int> factors(int n) {
  vector<int> D;
  while (n>1) {
    int p = F[n];
    D.push_back(p);
    do {n /= p;} while (n%p==0);
  }
  return D;
}

vector<couple> decomp(int n) {
  vector<couple> D;
  while (n>1) {
    int p = F[n], m = 0;
    while (n%p==0) {++m; n /= p;}
    D.push_back(make_pair(p,m));
  }
  return D;
}

void divisors(vector<couple> &D, vector<ent> &Divs) {
  Divs.push_back(1);
  for (vector<couple>::iterator it=D.begin(); it!=D.end(); ++it) {
    int l = Divs.size();
    ent f = it->first;
    for (int a=1; a<=it->second; ++a) {
      for (int i=0; i<l; ++i)
	Divs.push_back(Divs[i]*f);
      f *= it->first;
    }
  }
  sort(Divs.begin(),Divs.end());
}


typedef double scal;
typedef vector< vector<scal> > matrice;

struct Matrice {
  int m,n;
  matrice M;
  
  Matrice(matrice &M0) {
    M = M0; // attention, pas de copie profonde
    m = M.size();
    n = M[0].size();
  }

  Matrice(int m, int n, scal x=0) : m(m), n(n) {
    M.resize(m);
    for (int i=0; i<m; ++i) M[i].resize(n,x);
  }

  static Matrice id(int n) {
    Matrice M(n,n);
    for (int i=0; i<n; ++i) M[i][i] = 1;
    return M;
  }

  vector<scal> &operator[](int i) {
    return M[i];
  }
  
  const vector<scal> &operator[](int i) const {
    return M[i];
  }
  
  Matrice operator*(const Matrice &A) const {
    //assert(n==A.m);
    Matrice C(m,A.n);
    for (int i=0; i<m; ++i)
      for (int k=0; k<n; ++k)
	for (int j=0; j<A.n; ++j)
	  C[i][j] += M[i][k] * A[k][j];  // % MOD here if needed
    return C;
  }
  
  Matrice copy() const {
    Matrice C(m,n);
    for (int i=0; i<n; ++i) C[i] = M[i]; // copy
    return C;
  }
  
  Matrice pow(long long b) const {
    //assert(m==n);
    Matrice result = id(n);
    Matrice A = copy();
    while (b) {
      if (b&1) result = result*A;
      A = A*A;
      b >>= 1;
    }
    return result;
  }
};


// === Miller-Rabin ===
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
  if (n<=3) return n>=2;
  ent m = n-1;
  vector<bool> b;
  while (m>0) {
    b.push_back(((m&1)==1));
    m >>= 1;
  }
  for (vector<ent>::iterator w=W.begin(); w!=W.end(); ++w)
    if ((*w)%n!=0 && witness(*w,n,b)) return false;
  return true;
}


// === Pollard's Rho ===
ent randint(ent a, ent b) {
  return (ent)rand()%(b-a+1) + a;
}

ent pr_f(ent x, ent c, ent n) {
  return (mulmod(x,x,n)+c)%n;
}

ent pollard_rho(ent n) {
  ent c = randint(1,n-1);
  ent x = randint(0,n-1);
  ent y = x;
  x = pr_f(x,c,n);
  y = pr_f(pr_f(y,c,n),c,n);
  while (x!=y) {
    ent p = gcd(n,abs(x-y));
    if (1<p && p<n) return p;
    x = pr_f(x,c,n);
    y = pr_f(pr_f(y,c,n),c,n);
  }
  return -1;
}

void factorisation(ent n, factors &D) {
  while (n>1) {
    if (miller_rabin(n)) {
      ++D[n];
      n = 1;
    }
    else {
      ent f = pollard_rho(n);
      if (f>0) {
	factorisation(f,D);
	n /= f;
      }
    }
  }
}

// Retire les facteurs 2 avant (sinon ca boucle)
factors full_factorisation(ent n) {
  factors D;
  while ((n&1)==0) {
    ++D[2];
    n >>= 1;
  }
  factorisation(n,D);
  return D;
}


// === Matrix 2x2 ===
struct Matrix2 {
  ent m00, m01, m10, m11;
  
  Matrix2(ent a=1, ent b=0, ent c=0, ent d=1) :
    m00(a), m01(b), m10(c), m11(d) {}
  
  Matrix2 operator*(const Matrix2 &B) const {
    return Matrix2(((m00*B.m00)%P+(m01*B.m10)%P)%P,
		   ((m00*B.m01)%P+(m01*B.m11)%P)%P,
		   ((m10*B.m00)%P+(m11*B.m10)%P)%P,
		   ((m10*B.m01)%P+(m11*B.m11)%P)%P);
  }
  
  Matrix2 pow(ent n) const {
    if (n==0) return Matrix2();
    if ((n&1)==0) return ((*this)*(*this)).pow(n>>1);
    return (*this)*((*this)*(*this)).pow(n>>1);
  }
};
