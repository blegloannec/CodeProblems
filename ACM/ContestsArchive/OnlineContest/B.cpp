#include <iostream>
#include <queue>
using namespace std;

#define MAX 1005
#define INF 1000000000

typedef pair<int,int> paire;

int t[MAX][MAX];
int tj[MAX][MAX];
int FR[MAX];
int FC[MAX];
int R,C;
int nb_fire;
int JR,JC;

void BFS_fire(int f) {
  int i,j;
  queue<paire> q;
  q.push(paire(FR[f],FC[f]));
  while (!q.empty()) {
    i = q.front().first;
    j = q.front().second;
    q.pop();
    if (i>0 && t[i][j]+1<t[i-1][j]) {
      t[i-1][j] = t[i][j]+1;
      q.push(paire(i-1,j));
    }
    if (i<R-1 && t[i][j]+1<t[i+1][j]) {
      t[i+1][j] = t[i][j]+1;
      q.push(paire(i+1,j));
    }
    if (j>0 && t[i][j]+1<t[i][j-1]) {
      t[i][j-1] = t[i][j]+1;
      q.push(paire(i,j-1));
    }
    if (j<C-1 && t[i][j]+1<t[i][j+1]) {
      t[i][j+1] = t[i][j]+1;
      q.push(paire(i,j+1));
    }    
  }
}

int BFS() {
  int i,j;
  queue<paire> q;
  tj[JR][JC] = 0;
  q.push(paire(JR,JC));
  while (!q.empty()) {
    i = q.front().first;
    j = q.front().second;
    if (i==0 || i==R-1 || j==0 || j==C-1)
      return tj[i][j];
    q.pop();
    if (i>0 && tj[i-1][j]<0 && tj[i][j]+1<t[i-1][j]) {
      tj[i-1][j] = tj[i][j]+1;
      q.push(paire(i-1,j));
    }
    if (i<R-1 && tj[i+1][j]<0 && tj[i][j]+1<t[i+1][j]) {
      tj[i+1][j] = tj[i][j]+1;
      q.push(paire(i+1,j));
    }
    if (j>0 && tj[i][j-1]<0 && tj[i][j]+1<t[i][j-1]) {
      tj[i][j-1] = tj[i][j]+1;
      q.push(paire(i,j-1));
    }
    if (j<C-1 && tj[i][j+1]<0 && tj[i][j]+1<t[i][j+1]) {
      tj[i][j+1] = tj[i][j]+1;
      q.push(paire(i,j+1));
    }    
  }
  return -1;
}

int main() {
  int cas;
  cin >> cas;
  while (cas-->0) {
    cin >> R >> C;
    char c;
    nb_fire = 0;
    for (int i=0; i<R; ++i)
      for (int j=0; j<C; ++j) {
	tj[i][j] = -1;
	cin >> c;
	if (c=='#') 
	  t[i][j] = -2;
	else if (c=='F') {
	  t[i][j] = 0;
	  FR[nb_fire] = i;
	  FC[nb_fire] = j;
	  ++nb_fire;
	}
	else if (c=='J') {
	  t[i][j] = INF;
	  JR = i;
	  JC = j;
	} 
	else t[i][j] = INF;
      }
    for (int k=0; k<nb_fire; ++k) 
      BFS_fire(k);
    int res = BFS();
    if (res<0) 
      cout << "IMPOSSIBLE\n";
    else 
      cout << res+1 << endl;
  }

  return 0;
}
