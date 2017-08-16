#include <iostream>
#include <vector>
using namespace std;

/*
  C++ is required to pass the p = 100% last testcase.
  In Python, one had to pre-compute the answer and hard-code it
  (which is possible as for p = 100%, the value of NUMBER does not matter).
*/

typedef long long ll;
typedef pair<int,int> couple;

const ll N = 1000000;
int NUMBER,p;
vector<int> T(N,-1),S(N,1);

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void uni(int x, int y) {
  int x0 = find(x), y0 = find(y);
  T[y0] = x0;
  S[x0] += S[y0];
}

// generateur de paires
struct Gen {
  int n,curr;
  vector<int> s;

  Gen() {
    n = 0;
    curr = 0;
    for (ll k=1; k<56; ++k)
      s.push_back((100003-200003*k+300007*k*k*k)%N);
    s.push_back((s[s.size()-24]+s[s.size()-55])%N);
  }

  couple next() {
    if (n<56) {
      couple res(s[n],s[(n+1)%56]);
      n += 2;
      return res;
    }
    s[curr] = (s[(curr-24+56)%56]+s[(curr-55+56)%56])%N;
    curr = (curr+1)%56;
    s[curr] = (s[(curr-24+56)%56]+s[(curr-55+56)%56])%N;
    couple res(s[(curr-1+56)%56],s[curr]);
    curr = (curr+1)%56;
    return res;
  }
};

int connect() {
  Gen gen;
  int cpt = 0;
  while (true) {
    couple c = gen.next();
    int x = c.first, y = c.second;
    if (x!=y) {
      ++cpt;
      if (find(x)!=find(y)) {
	uni(x,y);
	if (100*S[find(NUMBER)]>=p*N)
	  return cpt;
      }
    }
  }
}

int main() {
  cin >> NUMBER >> p;
  cout << connect() << endl;
  return 0;
}
