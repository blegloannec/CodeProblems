#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int inf = 1<<30;
int A,B,C;

int reduce2(vector<int> &X) {
  sort(X.begin(),X.end());
  if (X[0]==0) {
    int res = X[1];
    X[1] = 0;
    X[2] -= res;
    return res;
  }
  else if (X[1]==X[2]) {
    int a = X[0]/2;
    int b = X[0]-a;
    X[0] = 0;
    X[1] -= a;
    X[2] -= b;
    return a+b+reduce2(X);
  }
  else {
    int m = min(X[0],X[2]-X[1]);
    X[0] -= m;
    X[2] -= m;
    return m+reduce2(X);
  }
}

int dist(vector<int> X) {
  if (X[0]<0) return inf;
  int D = 0;
  if (B<=2*A) {
    int m = reduce2(X);
    D += m*B;
  }
  D += (X[0]+X[1]+X[2])*A;
  return D;
}

int dicho(vector<int> X0, int e) {
  int l = 0, r = X0[0]/2;
  while (l<r) {
    int m1 = (l+r)/2;
    int m2 = m1+1;
    vector<int> X1 = X0;
    vector<int> X2 = X0;
    for (int i=0; i<3; ++i) {
      X1[i] -= 2*m1+e;
      X2[i] -= 2*m2+e;
    }
    int d1 = (2*m1+e)*C + dist(X1);
    int d2 = (2*m2+e)*C + dist(X2);
    if (d1<=d2) r = m1;
    else l = m2;
  }
  for (int i=0; i<3; ++i) X0[i] -= 2*l+e;
  return (2*l+e)*C + dist(X0);
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    vector<int> X(3);
    cin >> X[0] >> X[1] >> X[2] >> A >> B >> C;
    sort(X.begin(),X.end());
    cout << min(dicho(X,0),dicho(X,1)) << endl;
  }
  return 0;
}
