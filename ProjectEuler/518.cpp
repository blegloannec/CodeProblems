#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
typedef pair<int,int> couple;

/*
  a < b < c en progression geometrique
  ssi ac = b^2 et a < b < c
  Donc on peut factoriser les (p+1)^2 et enumerer leurs decompsitions
  en produit de 2 nombres.

  not optimized (rather straightforward), runs in ~50s with -O3
*/

const int N = 100000001;
vector<bool> P(N,true);
vector<int> F(N,1);

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

int main() {
  sieve_smallest_factor();
  ent S = 0;
  for (int b=3; b<N; b+=2)
    if (P[b]) {
      ent B = b+1;
      vector<couple> D;
      decomp(B,D);
      // decomp de B^2
      for (vector<couple>::iterator it=D.begin(); it!=D.end(); ++it)
	it->second *= 2;
      vector<ent> Divs;
      divisors(D,Divs);
      for (vector<ent>::iterator it=Divs.begin(); it!=Divs.end() && *it<B; ++it)
	if (P[*it-1]) {
	  ent C = (B*B)/(*it);
	  if (B<C && C<N && P[C-1]) S += *it+B+C-3;
	}
    }
  cout << S << endl;
  return 0;
}
