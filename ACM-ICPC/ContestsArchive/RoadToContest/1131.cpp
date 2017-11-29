#include <iostream>
#include <vector>
using namespace std;

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
  bool debut = true;
  int P,R;

  while (cin >> P >> R) {
    if (debut) debut = false;
    else cout << endl;
    T.resize(P,-1);
    int res = 0;
    for (int i=0; i<R; ++i) {
      int a,b;
      cin >> a >> b; --a; --b;
      if (find(a)==find(b)) ++res;
      else merge(a,b);
    }
    cout << res << endl;
    
    // cleaning
    T.clear();
  }
}
