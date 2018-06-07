#include <iostream>
#include <vector>
using namespace std;

typedef vector< pair<int,int> > decomp_t;

int fact_val(int n, int p) {
  int cpt = 0, q = p;
  while (q<=n) {
    cpt += n/q;
    q *= p;
  }
  return cpt;
}

decomp_t decomp(int n) {
  decomp_t D;
  int m = 0;
  while (n%2==0) {++m; n /= 2;}
  if (m>0) D.push_back(make_pair(2,m));
  for (int p=3; p*p<=n; p+=2) {
    m = 0;
    while (n%p==0) {++m; n /= p;}
    if (m>0) D.push_back(make_pair(p,m));
  }
  if (n>1) D.push_back(make_pair(n,1));
  return D;
}

int main() {
  int A,B;
  cin >> A >> B;
  decomp_t D = decomp(A);
  int res = 1<<30;
  for (auto it=D.begin(); it!=D.end(); ++it)
    res = min(res,fact_val(B,it->first)/it->second);
  cout << res << endl;
  return 0;
}
