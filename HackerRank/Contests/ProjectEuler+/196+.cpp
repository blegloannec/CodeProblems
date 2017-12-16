#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

typedef long long ent;
typedef unordered_map<ent,ent> dict;

vector<int> P;

pair<ent,ent> line_int(ent i) {
  --i;
  ent j = i*(i+1)/2+1;
  return make_pair(j,j+i);
}
    
void sieve_list(int N) {
  vector<bool> Pr(N,true);
  for (int i=2; i<N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

// crible pour marquer les nb premiers L <= n <= R
vector<bool> prime_int(ent L, ent R) {
  vector<bool> D(R-L+1,true);
  for (auto ip=P.begin(); ip!=P.end() && (*ip)*(*ip)<=R; ++ip) {
    ent p = *ip;
    for (ent n=max(2LL,(L+p-1)/p)*p; n<=R; n+=p)
      D[n-L] = false;
  }
  return D;
}

void line_count(int i, vector<bool> &P, ent x0, dict &C, dict &C0) {
  auto xy = line_int(i);
  ent x = xy.first, y = xy.second;
  for (ent p=x; p<=y; ++p)
    if (P[p-x0]) {
      vector<ent> V;
      if (p==x)
	V = {p-i+1,p-i+2,p+1,p+i,p+i+1};
      else if (p==y-1)
	V = {p-i,p-i+1,p-1,p+1,p+i-1,p+i,p+i+1};
      else if (p==y)
	V = {p-i,p-1,p+i-1,p+i,p+i+1};
      else
	V = {p-i,p-i+1,p-i+2,p-1,p+1,p+i-1,p+i,p+i+1};
      for (auto iv=V.begin(); iv!=V.end(); ++iv) {
	ent v = *iv;
	if (P[v-x0]) {
	  if (C0.find(p)==C0.end()) C0[p] = v;
	  ++C[p];
	}
      }
    }
}

ent line_sum(int i) {
  if (i<=1) return 0;
  ent x0 = line_int(i-2).first;
  ent y0 = line_int(i+2).second;
  vector<bool> P = prime_int(x0,y0);
  dict C,C0;
  line_count(i-1,P,x0,C,C0);
  line_count(i,P,x0,C,C0);
  line_count(i+1,P,x0,C,C0);
  auto xy = line_int(i);
  ent x = xy.first, y = xy.second, S = 0;
  for (ent p=x; p<=y; ++p)
    if (P[p-x0] && (C[p]>=2 || (C[p]==1 && C[C0[p]]>=2)))
      S += p;
  return S;
}

int main() {
  sieve_list(15000000);
  int a,b;
  cin >> a >> b;
  cout << line_sum(a)+line_sum(b) << endl;
  return 0;
}
