#include <iostream>
using namespace std;

#define MAX 500

int tarj[MAX];
int n;

void init() {
  for (int i=0; i<n; ++i) tarj[i] = i;
}

int find(int a) {
  if (tarj[a]==a) return a;
  else {
    tarj[a] = find(tarj[a]);
    return tarj[a];
  }
}

void uni(int a, int b) {
  tarj[find(a)] = tarj[find(b)];
}

int main() {
  int c,m,res,a,b;
  cin >> c;
  while (c-->0) {
    cin >> n >> m;
    res = n;
    init();
    for (int i=0; i<m; ++i) {
      cin >> a >> b;
      if (find(a) != find(b)) {
	--res;
	uni(a,b);
      }
    }
    cout << res << '\n';
  }
  return 0;
}
