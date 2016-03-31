#include <iostream>
#include <vector>
using namespace std;

#define INF 1000000000

int n,m,k;
int prix[6];
int combos[8][7];
int t[10][10][10][10][10][10];


int f(vector<int> in) {
  //cout << in.size() << endl;;
  for (int i=0; i<6; ++i)
    if (in[i]<0) 
      return INF;
  if (t[in[0]][in[1]][in[2]][in[3]][in[4]][in[5]] > -1){
    return t[in[0]][in[1]][in[2]][in[3]][in[4]][in[5]];
  }
  int res = INF;
  for(int i = 0; i < m; ++i){
    vector<int> tmp;
    for (int j=0; j<6; ++j) {
      tmp.push_back(in[j]-combos[i][j]);
    }
    res = min(res,f(tmp)+combos[i][6]);
  }
  int r = 0;
  for (int i=0; i<6; ++i) {
    r += prix[i]*in[i];
  }
  res = min(res,r);
  t[in[0]][in[1]][in[2]][in[3]][in[4]][in[5]] = res;
  return res;
  
}


int main() {
  while (cin >> n) {
  for(int i1 = 0; i1 < 10; ++i1)
    for(int i2 = 0; i2 < 10; ++i2)
      for(int i3 = 0; i3 < 10; ++i3)
        for(int i4 = 0; i4 < 10; ++i4)
          for(int i5 = 0; i5 < 10; ++i5)
            for(int i6 = 0; i6 < 10; ++i6)
              t[i1][i2][i3][i4][i5][i6] = -1;
  for(int i = 0; i < 6; ++i)
    prix[i] = 0;
  for (int i=0; i<n; ++i) 
    cin >> prix[i];
  cin >> m;
  for (int i=0; i<m; ++i){ 
    for (int j=0; j<6; ++j)
      combos[i][j] = 0;
    for (int j=0; j<n; ++j)
      cin >> combos[i][j];
    cin >> combos[i][6];
  }
  cin >> k;
  vector<int> com;
  for (int i=0; i<k; ++i) {
    for (int j=0; j<n; ++j) {
      int g;
      cin >> g;
      com.push_back(g);
    }
    for (int j=n; j<6; ++j) 
      com.push_back(0);
    cout << f(com) << '\n';
    com.clear();
  }
  }
  return 0;
}
