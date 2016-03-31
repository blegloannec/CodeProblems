// Ford-Fulkerson pour le problème Sabotage http://acm.uva.es/p/v104/10480.html 

#include <iostream>
#include <deque>
#include <list>
using namespace std;

#define MAX 51
#define SOURCE 1
#define SINK 2
#define INTMAX 50000000

struct edge {
  int e1,e2;
  edge(int x, int y) : e1(x), e2(y) {};
};

int t[MAX][MAX];
int f[MAX][MAX];
int ttmp[MAX][MAX];
int ftmp[MAX][MAX];
int svgt[MAX][MAX];
int prev[MAX];
int n,m;
deque<int> fifo;
list<int> vert;
list<edge> edges;

void clear(int t[MAX][MAX], int f[MAX][MAX]) {
  for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++)
      t[i][j] = f[i][j] = 0;
}

void clear(int f[MAX][MAX]) {
  for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++)
      f[i][j] = 0;
}

void print(int t[MAX][MAX]) {
  for (int i=1; i<=n; i++) {
    for (int j=1; j<=n; j++) cout << t[i][j] << '\t';
    cout << endl;
  }
  cout << endl;
}

void printl() {
  list<int>::iterator it;
  cout << "[ ";
  for (it=vert.begin(); it!=vert.end(); it++) cout << *it << ' ';
  cout << ']' << endl;
}

bool BFS(int t[MAX][MAX]) {
  fifo.clear();
  fifo.push_back(SOURCE);
  vert.clear();
  for (int i=1; i<=n; i++) prev[i]=0; 
  prev[SOURCE] = SOURCE;
  bool test = true;
  while (test && (!fifo.empty())) {
    int c = fifo.front();
    for (int i=1; i<=n; i++) {
      if ((prev[i]==0) && (t[c][i]!=0)) {
	fifo.push_back(i);
	prev[i] = c;
	if (i==SINK) {
	  test = false;
	  break;
	}
      }
    }
    fifo.pop_front();
    //cout << fifo.front() << endl;
  }
  if (test) return false;
  else {
    int c = SINK;
    vert.push_front(c);
    while (c != SOURCE) {
      c = prev[c];
      vert.push_front(c);
    } 
    return true;
  }
}

int ford_fulkerson(int t[MAX][MAX], int f[MAX][MAX]) {
  while (BFS(t)) {
    //print();
    //cout << "checkpoint 2" << endl;
    int cf = INTMAX;
    list<int>::iterator it,it0;
    it = vert.begin();
    it0 = it++;
    //printl();
    while (it!=vert.end()) {
      //cout << *it0 << " -> " << *it << endl;
      cf = min(cf,t[*it0][*it]);
      ++it;
      ++it0;
    }
    //cout << cf << endl;
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
  for (int j=1; j<=n; j++) res += f[1][j];
  return res;
}

void copy(int s[MAX][MAX], int d[MAX][MAX]) {
  for (int i=1; i<=n; i++) 
    for (int j=1; j<=n; j++)
      d[i][j] = s[i][j];
}

int main() {

  while (cin >> n >> m) {
    if ((m==0) && (n==0)) return 0;
    clear(t,f);
    for (int k=0; k<m; k++) {
      int e1,e2,p;
      cin >> e1 >> e2 >> p;
      t[e1][e2] = t[e2][e1] = svgt[e1][e2] = svgt[e2][e1] = p;
    }
    
    int maxflow = ford_fulkerson(t,f);
    edges.clear();
    while(maxflow > 0) {
      int i=1;
      bool test = true;
      while (test && (i<=n)) {
	for (int j=1; j<=n; j++) {
	  if ((f[i][j]>0) && (svgt[i][j]==f[i][j])) {
	    copy(svgt,ttmp);
	    ttmp[i][j] = 0;
	    ttmp[j][i] = 0;
	    copy(ttmp,t);
	    clear(ftmp);
	    if (ford_fulkerson(ttmp,ftmp) == maxflow - f[i][j]) {
	      copy(t,svgt);
	      clear(f);
	      maxflow = ford_fulkerson(t,f);
	      edges.push_front(edge(i,j));
	      test = false;
	      break;
	    }
	  }
	}
	++i;
      }
    }

    list<edge>::iterator it;
    for (it=edges.begin(); it!=edges.end(); it++) 
      cout << it->e1 << ' ' << it->e2 << endl;
    cout << endl;
  } 

  return 0;

}
