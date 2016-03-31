#include <iostream>
using namespace std;

int x,y,z,x2,y2,z2;

int main() {
  int n,a,b,c,d;
  while (cin >> n) {
    if (n==0) return 0;
    for (int i=0; i<n; ++i) {
      cin >> a >> b >> c >> d;
      if (i==0) {
        x = a;
        y = b;
        z = c;
        x2 = a+d;
        y2 = b+d;
        z2 = c+d;
      }
      else {
        x = max(x,a);
        x2 = min(x2,a+d);
        y = max(y,b);
        y2 = min(y2,b+d);
        z = max(z,c);
        z2 = min(z2,c+d);
      }
    }
    if ((x>=x2) || (y>=y2) || (z>=z2))
      cout << "0\n";
    else cout << (x2-x)*(y2-y)*(z2-z) << '\n';
  }

  return 0;
}
