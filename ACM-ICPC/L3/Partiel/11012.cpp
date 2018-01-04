#include <iostream>
using namespace std;

#define MAX 100001

int t[MAX][3];
int n;

int traite() {
  int res = -1;
  int x,y,z;
  for (int i=1; i<=n; i++) {
    x = t[i][0];
    y = t[i][1];
    z = t[i][2];
    for (int j=1; j<=n; j++) {
      res = max(res,abs(t[j][0]-x)+abs(t[j][1]-y)+abs(t[j][2]-z));
    }
  }
  return res;
}


int main() {
  int N;
  cin >> N;
  for (int cas=1; cas<=N; cas++) {
    cin >> n;
    for (int i=1; i<=n; i++)
      cin >> t[i][0] >> t[i][1] >> t[i][2];
    cout << "Case #" << cas << ": " << traite() << '\n';
  }
  
  return 0;
}
