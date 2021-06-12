#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, cnt = 0;
  cin >> n;
  vector<int> SQRT(10*n,-1);
  for (int r=0; r*r<=(int)SQRT.size(); ++r) SQRT[r*r] = r;
  for (int a=0; a*a<=n; ++a)
    for (int b=0; a*a+b*b<=n; ++b)
      for (int c=0; a*a+b*b+c*c<=n; ++c) {
	int d2 = n - (a*a+b*b+c*c);
	if (SQRT[d2]>=0 && SQRT[b+3*c+5*SQRT[d2]]>=0) ++cnt;
      }
  cout << cnt << endl;
}
