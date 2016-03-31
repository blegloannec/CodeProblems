#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

#define MAX 201

map<string,int> h;
map<string,int>::iterator it;

int size;
//int pred[MAX];
//int t[MAX][MAX];

/*
void clear_pred(int start) {
  for (int i=0; i<size; ++i) {
    pred[i]=-1;
  }
  pred[start] = start;
}

bool BFS(int start, int dest) {
  if (start==dest) return true;
  queue<int> q;
  int curr;
  clear_pred(start);
  q.push(start);
  while (!(q.empty())) {
    curr = q.front();
    q.pop();
    for (int i = 0; i<size; ++i) 
      if ((t[curr][i]>0) && (pred[i]<0)) {
        q.push(i);
        pred[i] = curr;
        if (i==dest) return true;
      }
  }
  return false;
  }*/

struct edge {
  int ext1,ext2,weight;
  edge(int a, int b, int c) : ext1(a),ext2(b),weight(c) {}
};

int tarj[MAX];

vector<edge> edges;

bool inf(const edge &a, const edge &b) {
  return a.weight > b.weight;
}

int find(int e) {
  int p = tarj[e];
  if (p<0) return e;
  else {
    int root = find(p);
    tarj[e] = root;
    return root;
  }
}

void fusion(int a, int b) {
  tarj[find(b)] = find(a);
}

int kruskal(int start, int dest) {
  sort(edges.begin(),edges.end(),inf);
  vector<edge>::iterator it = edges.begin();
  int res = 0;
  while (find(start)!=find(dest)) {
    if (find(it->ext1)!=find(it->ext2)) {
      res = it->weight;
      fusion(it->ext1,it->ext2);
    } 
    ++it;
  }
  return res;
}

int main() {
  int n,r,w,nb,nba,nbb,cas;
  string a,b;
  cas = 1;
  while (cin >> n >> r) {
    size = n;
    for (int i=0; i<size; ++i) {
      tarj[i] = -1;
      //for (int j=0; j<size; ++j)
      //t[i][j] = f[i][j] = 0;
        
    }
    h.clear();
    edges.clear();    
    nb = 0;
    if (n==0 && r==0) return 0;
    for (int i=0; i<r; ++i) {
      cin >> a >> b >> w;
      it = h.find(a);
      if (it == h.end()) {
        h.insert(pair<string,int>(a,nb));
        nba = nb;
        ++nb;
      }
      else {
        nba = it->second;
      }
      it = h.find(b);
      if (it == h.end()) {
        h.insert(pair<string,int>(b,nb));
        nbb = nb;
        ++nb;  
      }
      else {
        nbb = it->second;
      }
      //t[nba][nbb] = t[nbb][nba] = w;
      edges.push_back(edge(nba,nbb,w));
    }
    cin >> a >> b;
    it = h.find(a);
    nba = it->second;
    it = h.find(b);
    nbb = it->second;
    cout << "Scenario #" << cas << '\n';
    cout << kruskal(nba,nbb) << " tons\n\n";
    ++cas;
  }
  

  return 0;
}
