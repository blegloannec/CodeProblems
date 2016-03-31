#include <iostream>
#include <queue>
#include <vector>
using namespace std;

#define N 40000


#define MAX 40000
struct edge {
  int dest,weight;
  edge(int d, int w) : dest(d), weight(w) {};
};
typedef vector<edge> liste;
int size;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}

struct vert {
  int num,dist;
  vert(int n, int d) : num(n),dist(d) {};
};

struct comp {
  bool operator()(vert &v1, vert &v2) {
    return (v1.dist > v2.dist);
  };
};

int dist[MAX];
bool visited[MAX];

void relacher(int u, int v, int w) {
  int d2 = dist[u]+w;
  if ((dist[v]<0)||(dist[v]>d2)) {
    dist[v] = d2;
    pred[v] = u;
  }
}

bool dijkstra(int start, int dest) { // teste si l'on atteint dest
  int u;
  liste::iterator it; // RINN
  priority_queue<vert,vector<vert>,comp> q;
  // initialisation
  for (int i=0; i<size; i++) {
    dist[i] = -1;
    pred[i] = -1;
    visited[i] = false;
  }
  dist[start] = 0;
  q.push(vert(start,0));
  while (!q.empty()) { // BFS
    u = q.top().num;
    if (u==dest) return true; // RINN
    q.pop();
    if (!visited[u]) {
      for (it=t[u].begin(); it!=t[u].end(); ++it) {
	int v = it->dest;
	relacher(u,v,it->weight);
	if (!visited[v]) q.push(vert(v,dist[v]));
	}
	visited[u] = true;
      }
    }
    return false; // RINN
}

int width, height;
int tab[N];
char ordre[26];
int xdep, ydep, xfin, yfin;
int distance_trucmuche[N];
vector<int> piege;

void parcours(int dep){
//   cout << "plop\n";
//   cout << "dep: " << dep/width << ", " << dep%width << '\n';
  for (int i=0;i<width*height;i++) {
    distance_trucmuche[i]=-1;
    visited[i] = false;
  }
  distance_trucmuche[dep]=0;
  queue<int> file;
  int curr;
  if (tab[dep]==1) return;
  file.push(dep);
  while(!file.empty()){
    curr=file.front();
    file.pop();
    if (visited[curr]) continue;
    visited[curr] = true;
//     cout << "curr: " << curr/width << ", " << curr%width << '\n';
    if (tab[curr]>1 && curr != dep){
      if (tab[curr]>tab[dep] || dep==(ydep*width+xdep)){
	t[dep].push_back(edge(curr, distance_trucmuche[curr]));
// 	cout << "on ajoute " << dep/width << ", " << dep%width << " -> " << curr/width << ", " << curr%width << " avec la distance " << distance_trucmuche[curr] << '\n';
      }
      continue;
    }

    if (tab[curr+1]!=1 && distance_trucmuche[curr+1]<0){
      distance_trucmuche[curr+1]=distance_trucmuche[curr]+1;
      file.push(curr+1);
    }
    if (tab[curr-1]!=1 && distance_trucmuche[curr-1]<0){
      distance_trucmuche[curr-1]=distance_trucmuche[curr]+1;
      file.push(curr-1);
    }
    if (tab[curr+width]!=1 && distance_trucmuche[curr+width]<0){
      distance_trucmuche[curr+width]=distance_trucmuche[curr]+1;
      file.push(curr+width);
    }
    if (tab[curr-width]!=1 && distance_trucmuche[curr-width]<0){
      distance_trucmuche[curr-width]=distance_trucmuche[curr]+1;
      file.push(curr-width);
    }
  }
  curr=(yfin*width+xfin);
  if (distance_trucmuche[curr]>=0){
    t[dep].push_back(edge(curr, distance_trucmuche[curr]));  
// 	cout << "on ajoute " << dep/width << ", " << dep%width << " -> " << curr/width << ", " << curr%width << " avec la distance " << distance_trucmuche[curr] << '\n';
  }
}

  int main(){
    char tmp;
    while (cin >> tmp){
      ordre[tmp-'A']=0;
      for (int i=1;i<26;i++){
	cin >> tmp;
	ordre[tmp-'A']=i;
      }
    
      cin >> width >> height;
      width+=2; height+=2;
      size = width*height;
      for (int i=1;i<height-1;i++){
	for (int j=1;j<width-1;j++){
	  cin >> tmp;
	  if (tmp=='x')
	    tab[i*width+j]=1;
	  else if (tmp=='o')
	    tab[i*width+j]=0;
	  else{
	    tab[i*width+j]=ordre[tmp-'A']+2;
	    piege.push_back(i*width+j);
// 	    cout << "push_back piege " << i << ", " << j << '\n';
	  }
	}
      }
      for (int i=0;i<width;i++){
	tab[i]=1;
	tab[i+(height-1)*width]=1;
      }
      for (int i=1;i<height;i++){
	tab[i*width]=1;
	tab[i*width+width-1]=1;
      }
      
      cin >> xdep >> ydep >> xfin >> yfin;
      xdep++; ydep++; xfin++; yfin++;
      piege.push_back(ydep*width+xdep);
      for (int i=0; i<(int)piege.size(); i++)
	parcours(piege[i]);
      dijkstra(ydep*width+xdep, yfin*width+xfin);
      cout << dist[yfin*width+xfin] << '\n';
      piege.clear();
    }
  }
