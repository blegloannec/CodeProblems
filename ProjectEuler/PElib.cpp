typedef long long ent;
typedef pair<int,int> couple;

ent expmod(ent x, ent n, ent m) {
  if (n==0) return 1;
  if (n%2==0) return expmod((x*x)%m,n/2,m);
  return (x*expmod((x*x)%m,(n-1)/2,m))%m;
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
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

vector<bool> P(N,true);
vector<int> F;
void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

void factors(int n, vector<int> &D) {
  int p = F[n];
  D.push_back(p);
  do {n /= p;} while (n%p==0);
  if (n>1) factors(n,D);
}

void decomp(int n, vector<couple> &D) {
  int p = F[n];
  n /= p;
  int m = 1;
  while (n%p==0) {
    n /= p;
    ++m;
  }
  D.push_back(couple(p,m));
  if (n>1) decomp(n,D);
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

  static Matrice zero(int m, int n) {
    matrice M0(m);
    for (int i=0; i<m; ++i) M0[i].resize(n,0);
    return Matrice(M0);
  }

  static Matrice id(int n) {
    Matrice M = zero(n,n);
    for (int i=0; i<n; ++i) M.M[i][i] = 1;
    return M;
  }
  
  Matrice operator*(const Matrice &A) const {
    //assert(n==A.m);
    Matrice C = zero(m,A.n);
    for (int i=0; i<m; ++i)
      for (int k=0; k<n; ++k)
	for (int j=0; j<A.n; ++j)
	  C.M[i][j] += M[i][k] * A.M[k][j];
    return C;
  }
  
  Matrice copy() const {
    matrice M0(n);
    for (int i=0; i<n; ++i) M0[i] = M[i]; // copy
    return Matrice(M0);
  }
  
  Matrice pow(int b) const {
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
