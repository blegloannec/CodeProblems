#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  T[find(y)] = find(x);
}

int main() {
  int t;
  string c;
  cin >> t;
  cin >> c;
  while (t--) {
    n = stoi(c);
    int s = 0, u = 0;
    T.resize(n);
    fill(T.begin(),T.end(),-1);
    while ((cin >> c) && (c=="c" || c=="q")) {
      int i,j;
      cin >> i >> j; --i; --j;
      if (c=="c") {
	if (find(i)!=find(j)) merge(i,j);
      }
      else {
	if (find(i)==find(j)) ++s;
	else ++u;
      }
    }
    cout << s << ',' << u << endl;
    if (t) cout << endl;
  }
  return 0;
}
