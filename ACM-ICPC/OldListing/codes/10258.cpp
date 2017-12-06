#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 101

bool existe[MAX];
bool valid[MAX][10];
int penal[MAX][10];
int scores[MAX];
int times[MAX];

struct team {
  int numb,score,time;
  team(int a, int b, int c) : numb(a), score(b), time(c) {};
};

bool ordre(const team &a, const team &b) {
  return ((a.score>b.score)||((a.score==b.score)&&(a.time<b.time))
    ||((a.score==b.score)&&(a.time==b.time)&&(a.numb<b.numb)));
}

vector<team> t;

void init() {
  for (int i=1; i<MAX; ++i) {
    existe[i] = false;
    scores[i] = 0;
    times[i] = 0;
    for (int j=0; j<10; ++j) {
      valid[i][j] = false;
      penal[i][j] = 0;
    }
  }
  t.clear();
}


int main() {
  int cas,n,p,tps;
  char c;
  char buff[1000];
  bool debut = true;
  buff[0]=0;
  cin >> cas;
  cin.ignore();
  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    init();
    while ((buff[0]==0)||(buff[0]=='\n')) cin.getline(buff,sizeof(buff));
    while (sscanf(buff,"%d %d %d %c",&n,&p,&tps,&c)==4) {
      existe[n] = true;
      if (c=='C') {
	if (!valid[n][p]) {
	  valid[n][p] = true;
          ++scores[n];
	  times[n] += tps+penal[n][p];
	}
      }
      else if (c=='I') {
	penal[n][p] += 20;
      }
      cin.getline(buff,sizeof(buff));
    }
    for (int i=1; i<MAX; ++i) {
      if (existe[i]) {
	t.push_back(team(i,scores[i],times[i]));
      }
    }
    sort(t.begin(),t.end(),ordre);
    for (int i=0; i<(int)t.size(); ++i) {
      cout << t[i].numb << ' ' << t[i].score << ' ' << t[i].time << '\n';
    }
  }
  return 0;
}
