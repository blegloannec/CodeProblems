#include <iostream>
#include <map>
using namespace std;

#define NMAX 100
typedef long long ent;
typedef tuple<int,int,ent,ent> key;

int N,M;
ent a[NMAX], b[NMAX];
int A[NMAX], B[NMAX];
map<key,ent> memo;

ent PLSSC_mod(int i, int j, ent va, ent vb) {
  if (i<0 || j<0) return 0;
  key K(i,j,va,vb);
  auto it = memo.find(K);
  if (it!=memo.end()) return it->second;
  ent res;
  if (A[i]==B[j]) {
    if (va<vb)
      res =  PLSSC_mod(i-1,j,a[i-1],vb-va)+va;
    else if (va>vb)
      res =  PLSSC_mod(i,j-1,va-vb,b[j-1])+vb;
    else
      res =  PLSSC_mod(i-1,j-1,a[i-1],b[j-1])+va;
  }
  else 
    res =  max(PLSSC_mod(i-1,j,a[i-1],vb),PLSSC_mod(i,j-1,va,b[j-1]));
  memo[K] = res;
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int c=1; c<=T; ++c) {
    cin >> N >> M;
    for (int i=0; i<N; ++i)
      cin >> a[i] >> A[i];
    for (int i=0; i<M; ++i)
      cin >> b[i] >> B[i];
    memo.clear();
    cout << "Case #" << c << ": " << PLSSC_mod(N-1,M-1,a[N-1],b[M-1]) << endl;
  }
  return 0;
}
