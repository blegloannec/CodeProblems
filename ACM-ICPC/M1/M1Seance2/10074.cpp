#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

#define MAX 101

typedef pair<int,int> paire;

int t[MAX][MAX];
stack<paire> s;

int main() {
  int M,N,a,curr,airemax;
  while (cin >> M >> N) {
    if (M==0) return 0;
    for (int i=0; i<M; ++i) {
      curr = 0;
      for (int j=0; j<N; ++j) {
        cin >> a;
        if (a==1) {
          t[i][j] = 0;
          curr = 0;
        }
        else {
          ++curr;
          t[i][j] = curr;
        }
      }
    }    
    airemax = 0;
    for (int j=0; j<N; ++j) {
      s.push(paire(0,0));
      for (int i=0; i<M; ++i) {
        while (s.top().first > t[i][j]) {
          airemax = max(airemax, s.top().first * (i - s.top().second));
          s.pop();
        }
        while (s.top().first < t[i][j]) {
          s.push(paire(s.top().first+1,i));
        }
      }
      while (!s.empty()) {
        airemax = max(airemax, s.top().first * (M - s.top().second));
        s.pop();
      }
    }
    cout << airemax << '\n';
  }
  return 0;
}
