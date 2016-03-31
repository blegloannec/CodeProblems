#include <iostream>
#include <vector>
using namespace std;

#define MAX 10005

vector<int> t[MAX];
int pen[MAX];
int nb0[MAX];
int nb[MAX];
bool mark[MAX];

void parc(int s) {
  //  cout << s << endl;
  int peno = 0;
  int tot = 0;
  for (int i=0; i<(int)t[s].size(); ++i) {
    if (!mark[t[s][i]]) {
      mark[t[s][i]] = true;
      parc(t[s][i]);
      peno += pen[t[s][i]];
      tot += nb[t[s][i]];
    }
  }
  tot += nb0[s]-1;
  peno += abs(tot);
  pen[s] = peno;
  nb[s] = tot;
}

int main() {
  int n,s;
  while (cin >> n) {
    if (n==0) return 0;
    for (int i=0; i<n; ++i) {
      pen[i] = 0;
      nb[i] = 0;
      nb0[i] = 0;
      t[i].clear();
      mark[i] = false;
    }
    for (int i=0; i<n; ++i) {
      cin >> s;
      --s;
      cin >> nb0[s];
      int k,ss;
      cin >> k;
      for (int j=0; j<k; ++j) {
        cin >> ss;
        --ss;
        t[s].push_back(ss);
        t[ss].push_back(s);
      }
    }
    mark[0] = true;
    parc(0);
    cout << pen[0] << '\n';
  } 
  return 0;
}
