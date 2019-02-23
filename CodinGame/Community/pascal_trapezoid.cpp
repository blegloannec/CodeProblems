#include <iostream>
#include <vector>
using namespace std;

struct Elem {
  int x;
  string s;
  bool is_int;

  Elem(const string &s0, bool infer=false) {
    s = s0;
    is_int = false;
    if (infer)
      try {
	x = stoi(s);
	is_int = true;
      } catch (...) {}
  }

  Elem(int x0) {
    x = x0;
    is_int = true;
    s = to_string(x);
  }

  Elem operator+(const Elem &B) const {
    return (is_int && B.is_int) ? Elem(x+B.x) : Elem(s+B.s);
  }
};

int main() {
  int E,L,N;
  cin >> E >> L >> N;
  vector<Elem> X;
  for (int i=0; i<E; ++i) {
    string s;
    cin >> s;
    X.push_back(Elem(s,true));
  }
  X.resize(N,X.back());
  for (int l=1; l<L; ++l)
    for (int i=min(N-1,E-2+l); i>max(0,N-(L-l)-1); --i)
      X[i] = X[i-1] + X[i];
  cout << X[N-1].s << endl;
  return 0;
}
