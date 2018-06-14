#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
using namespace std;

typedef long long ent;

struct Bloom {
  int m,k;
  vector<bool> H;
  vector<ent> P,A,B;

  bool prime(int p) {
    if (p<=2 || p%2==0) return false;
    for (int i=3; i*i<=p; i+=2)
      if (p%i==0) return false;
    return true;
  }
  
  Bloom(int m0, int k0) {
    m = m0;
    k = k0;
    H.resize(m,false);
    P.resize(k);
    A.resize(k);
    B.resize(k);
    for (int i=0; i<k; ++i) {
      P[i] = m+rand();
      while (!prime(P[i])) P[i] = m+rand();
      A[i] = (rand()%(P[i]-1))+1;
      B[i] = rand()%P[i];
    }
  }

  int hash(int i, ent x) {
    return ((A[i]*x+B[i])%P[i])%m;
  }
  
  bool add(ent x) {
    bool collision = true;
    for (int i=0; i<k; ++i) {
      int h = hash(i,x);
      if (!H[h]) {
	collision = false;
	H[h] = true;
      }
    }
    return !collision;
  }

  bool check(ent x) {
    for (int i=0; i<k; ++i)
      if (!H[hash(i,x)]) return false;
    return true;
  }
};

const int N = 100000000;
vector<bool> P(N,true);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

int main() {
  srand(time(NULL));
  sieve();
  Bloom B(10*N,5);
  int total = 0, coll = 0;
  for (int i=3; i<N; i+=2)
    if (P[i]) {
      ++total;
      if (!B.add(i)) ++coll;
    }
  cout << total <<  ' ' << coll << endl;
  return 0;
}
