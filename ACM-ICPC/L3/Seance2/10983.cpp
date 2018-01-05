// Ford-Fulkerson pour le problème Buy one...
// ATTENTION, code pas efficace du tout...

#include <iostream>
#include <deque>
#include <list>
using namespace std;

#define MAX 32*13
#define INTMAX 500000

int t[MAX][MAX];
int svgt[MAX][MAX];
int cost[MAX][MAX];
int f[MAX][MAX];
int pred[MAX];
int n,n0,d,SINK,SOURCE;
deque<int> fifo;
list<int> vert;

int go(int e, int u) {
  return n0*e+u;
}

void clear(int a[MAX][MAX]) {
  for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++) 
      a[i][j] = 0;
}

bool BFS(int t[MAX][MAX]) {
  fifo.clear();
  fifo.push_back(SOURCE);
  vert.clear();
  for (int i=1; i<=n; i++) pred[i]=0; 
  pred[SOURCE] = SOURCE;
  bool test = true;
  while (test && (!fifo.empty())) {
    int c = fifo.front();
    for (int i=1; i<=n; i++) {
      if ((pred[i]==0) && (t[c][i]!=0)) {
	fifo.push_back(i);
	pred[i] = c;
	if (i==SINK) {
	  test = false;
	  break;
	}
      }
    }
    fifo.pop_front();
  }
  if (test) return false;
  else {
    int c = SINK;
    vert.push_front(c);
    while (c != SOURCE) {
      c = pred[c];
      vert.push_front(c);
    } 
    return true;
  }
}

// Version  qui calcule le maxflow
int ford_fulkerson(int t[MAX][MAX], int f[MAX][MAX]) {
  clear(f);
  while (BFS(t)) {
    int cf = INTMAX;
    list<int>::iterator it,it0;
    it = vert.begin();
    it0 = it++;
    while (it!=vert.end()) {
      cf = min(cf,t[*it0][*it]);
      ++it;
      ++it0;
    }
    it = vert.begin();
    it0 = it++;
    while (it!=vert.end()) {
      f[*it0][*it] += cf;
      t[*it0][*it] -= cf;
      f[*it][*it0] -= cf;
      t[*it][*it0] += cf;
      ++it;
      ++it0;
    }
  }
  int res = 0;
  for (int j=1; j<=n; j++) res += f[SOURCE][j];
  return res;
}

int get_cost() {
  int c = 0;
  for (int e=0; e<d; e++)
    for (int u=1; u<n0; u++)
      for (int v=1; v<n0; v++)
	if (f[go(e,u)][go(e+1,v)]>0) 
	  c = max(c,cost[go(e,u)][go(e+1,v)]);
  return c;
}

void copy(int a[MAX][MAX], int b[MAX][MAX]) {
  for (int i=0; i<=n; i++)
    for (int j=0; j<=n; j++)
      b[i][j] = a[i][j];
}


void copy_filter(int a[MAX][MAX], int b[MAX][MAX], int filter) {
  for (int i=0; i<=n; i++)
    for (int j=0; j<=n; j++)
      if (cost[i][j]<filter) b[i][j] = a[i][j];
      else b[i][j] = 0;
}

/*
void affich(int a[MAX][MAX]) {
  for (int i=1; i<=n; i++) {
    for (int j=1; j<=n; j++)
      cout << a[i][j] << '\t';
    cout << endl;
  }
}
*/

/*/ Version qui ne calcule pas le maxflow
void ford_fulkerson(int t[MAX][MAX], int f[MAX][MAX]) {
  while (BFS(t)) {
    int cf = INTMAX;
    list<int>::iterator it,it0;
    it = vert.begin();
    it0 = it++;
    while (it!=vert.end()) {
       cf = min(cf,t[*it0][*it]);
      ++it;
      ++it0;
    }
    it = vert.begin();
    it0 = it++;
    while (it!=vert.end()) {
      f[*it0][*it] += cf;
      t[*it0][*it] -= cf;
      f[*it][*it0] -= cf;
      t[*it][*it0] += cf;
      ++it;
      ++it0;
    }
  }
}
*/

int main() {
  int N,m,total,c,res;
  cin >> N;

  for (int cas=1; cas<=N; cas++) {
    cin >> n0 >> d >> m;
    ++n0;
    n = go(d,n0);
    SINK = n-1;
    SOURCE = go(0,n0);
    
    for (int i=0; i<=n; i++)
      for (int j=0; j<=n; j++) {
	t[i][j] = 0;
	cost[i][j] = 0;
      }

    for (int e=0; e<d; e++) 
      for (int i=1; i<n0; i++)
	t[go(e,i)][go(e+1,i)] = INTMAX;
    
    
    while (m-->0) {
      int u,v,c,p,e;
      cin >> u >> v >> c >> p >> e;
      t[go(e,u)][go(e+1,v)] = c;
      cost[go(e,u)][go(e+1,v)] = p;
    }
    
    total = 0;
    for (int i=1; i<n0; i++) {
      int nb;
      cin >> nb;
      t[SOURCE][go(0,i)] = nb;
      total += nb;
    }
 
    copy(t,svgt);
    c = -1;
    res = ford_fulkerson(t,f);
    
    while (res == total) {
      c = get_cost();
      copy_filter(svgt,t,c); 
      res = ford_fulkerson(t,f);
    }

    if (c<0) cout << "Case #" << cas << ": Impossible" << endl;
    else cout << "Case #" << cas << ": " << c << endl;
  }

  return 0;

}
