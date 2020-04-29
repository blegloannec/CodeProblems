#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int S = 0;
vector< unordered_map<string,int> > Idx(4);
vector<int> T;

int suffix(string &s) {
  int l = min(3, (int)s.size());
  s = s.substr(s.size()-l, l);
  if (Idx[l].find(s)==Idx[l].end()) Idx[l][s] = S++;
  return Idx[l][s];
}

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) T[y0] = x0;
}

int main() {
  int N;
  cin >> N;
  vector< pair<int,int> > Is, Not;
  for (int i=0; i<N; ++i) {
    string left, op, right;
    cin >> left >> op >> right;
    int l = suffix(left), r = suffix(right);
    if (op.size()==2) Is.push_back(make_pair(l,r));
    else Not.push_back(make_pair(l,r));
  }
  T.resize(S, -1);
  for (int l=2; l<=3; ++l) {
    for (const auto &si : Idx[l]) {
      string s = si.first;
      for (int ls=1; ls<l; ++ls) {
	string suff = s.substr(l-ls,ls);
	auto it = Idx[ls].find(suff);
	if (it!=Idx[ls].end()) merge(si.second, it->second);
      }
    }
  }
  for (const auto &is : Is) merge(is.first, is.second);
  bool valid = true;
  for (const auto &no : Not)
    if (find(no.first)==find(no.second)) {
      valid = false;
      break;
    }
  cout << (valid ? "yes" : "wait what?") << endl;
  return 0;
}
