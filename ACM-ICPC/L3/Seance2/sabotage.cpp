// Ford-Fulkerson pour le problème Sabotage http://acm.uva.es/p/v104/10480.html 

#include <iostream>
#include <deque>
#include <list>
using namespace std;

#define MAX 51
#define SOURCE 1
#define SINK 2
#define INTMAX 50000000

int t[MAX][MAX];
int svgt[MAX][MAX];
int f[MAX][MAX];
int prev[MAX];
int n,m;
deque<int> fifo;
list<int> vert;

void clear(int a[MAX][MAX], int b[MAX][MAX], int c[MAX][MAX]) {
  for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++) 
      a[i][j] = b[i][j] = c[i][j] = 0;
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

/*// Version  qui calcule le maxflow
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
  for (int j=1; j<=n; j++) res += f[1][j];
  return res;
}
*/

// Version qui ne calcule pas le maxflow
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


int main() {

  while (cin >> n >> m) {
    if ((m==0) && (n==0)) return 0;
    clear(t,f,svgt);
    for (int k=0; k<m; k++) {
      int e1,e2,p;
      cin >> e1 >> e2 >> p;
      t[e1][e2] = t[e2][e1] = svgt[e1][e2] = svgt[e2][e1] = p;
    }
    
    ford_fulkerson(t,f);
    
    /* Une partition de la coupe est constituée par l'ensemble des sommets
       accessibles à partir de la source dans le graphe résiduel.
     */
    for (int i=1; i<=n; i++) 
      if (prev[i]>0) 
	for (int j=1; j<=n; j++) 
	  if ((prev[j]==0)&&(svgt[i][j]>0)) 
	    cout << i << ' ' << j << endl;
       

    cout << endl;
  } 

  return 0;

}
