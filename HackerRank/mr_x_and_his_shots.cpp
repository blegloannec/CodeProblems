#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> event;
const int SHOT_L = 0;
const int SHOT_R = 3;
const int PLAY_L = 1;
const int PLAY_R = 2;

int main() {
  int N,M;
  cin >> N >> M;
  vector<event> T;
  for (int i=0; i<N; ++i) {
    int A,B;
    cin >> A >> B;
    T.push_back(make_pair(A,SHOT_L));
    T.push_back(make_pair(B,SHOT_R));
  }
  for (int i=0; i<M; ++i) {
    int C,D;
    cin >> C >> D;
    T.push_back(make_pair(C,PLAY_L));
    T.push_back(make_pair(D,PLAY_R));
  }
  sort(T.begin(),T.end());
  long long S = 0;
  int shots = 0, players = 0;
  for (auto it=T.begin(); it!=T.end(); ++it) {
    if (it->second==SHOT_L) {
      ++shots;
      S += players;
    }
    else if (it->second==SHOT_R) --shots;
    else if (it->second==PLAY_L) {
      ++players;
      S += shots;
    }
    else --players;
  }
  cout << S << endl;
  return 0;
}
