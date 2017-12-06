// Dijstra pour listes d'adjacence et Here we Go(relians)

#include <iostream>
#include <list>
#include <queue>
using namespace std;

#define SOURCE 1
#define MAX 21*21+1
//#define INTMAX 50000000

struct edge {
  int e,w;
  edge(int ee, int ww) : e(ee),w(ww) {};
};
  
struct vert {
  int v,d;
  vert(int vv, int dd) : v(vv),d(dd) {};
};

struct comp {
  bool operator()(vert v1, vert v2) {
    return (v1.d > v2.d);
  };
};

int n,c,l,DEST;
list<edge> adj[MAX];
int d[MAX];
int pi[MAX];
bool visited[MAX];
priority_queue<vert,vector<vert>,comp> q;

int go(int i, int j) {
  return i*(c+1)+j+1;
}

void clearg() {
  for (int i=1; i<=n; i++) adj[i].clear();
}

void init() {
  for (int i=1; i<=n; i++) {
    d[i] = -1;
    pi[i] = 0;
    visited[i] = false;
  }
  d[SOURCE] = 0;
  while (!q.empty()) q.pop();
  q.push(vert(SOURCE,0));
}

void relacher(int u, int v, int w) {
  int d2 = d[u]+w;
  if ((d[v]<0)||(d[v]>d2)) {
    d[v] = d2;
    pi[v] = u;
  }
}

bool dijkstra() {
  int u;
  list<edge>::iterator it;
  init();
  while (!q.empty()) {
    u = q.top().v;
    if (u==DEST) return true;
    q.pop();
    if (!visited[u]) {
      for (it=adj[u].begin(); it!=adj[u].end(); it++) {
	int v = it->e;
	relacher(u,v,it->w);
	if (!visited[v]) {
	  q.push(vert(v,d[v]));
	}
      }
      visited[u] = true;
    }
  }
  return false;
}

/*
void affich() {
  for (int i=1; i<=n; i++) {
    for (list<edge>::iterator it=adj[i].begin(); it!=adj[i].end(); it++) 
      cout << '(' << i << ' ' << it->e << ' ' << it->w << ") ";
    cout << endl;
  }
}
*/

int main() {
  int w;
  char *sens = (char*) malloc(2*sizeof(char));
  
  while (cin >> l >> c) {
    if ((c==0)&&(l==0)) return 0;
    n = go(l,c);
    DEST = n;
    clearg();
    
    for (int i=0; i<2*l+1; i++) {
      if (i%2==0) {
	for (int j=0; j<c; j++) {
	  cin >> w >> sens;
	  if (w>0) {
	    w = 2520/w;
	    if (!strcmp(sens,">")) 
	      adj[go(i/2,j)].push_back(edge(go(i/2,j+1),w));
	    else if(!strcmp(sens,"<")) 
	      adj[go(i/2,j+1)].push_back(edge(go(i/2,j),w));
	    else {
	      adj[go(i/2,j)].push_back(edge(go(i/2,j+1),w));
	      adj[go(i/2,j+1)].push_back(edge(go(i/2,j),w));
	    }
	  }
	}
      }
      else {
	for (int j=0; j<=c; j++) {
	  cin >> w >> sens;
	  if (w>0) {
	    w = 2520/w;
	    if (!strcmp(sens,"v")) 
	      adj[go(i/2,j)].push_back(edge(go(i/2+1,j),w));
	    else if(!strcmp(sens,"^")) 
	      adj[go(i/2+1,j)].push_back(edge(go(i/2,j),w));
	    else {
	      adj[go(i/2,j)].push_back(edge(go(i/2+1,j),w));
	      adj[go(i/2+1,j)].push_back(edge(go(i/2,j),w));
	    }
	  }
	}
      }
    }

    //affich();    
    if (!dijkstra()) cout << "Holiday\n";
    else cout << d[DEST] << " blips\n";
    
  }
  
  return 0;
}
