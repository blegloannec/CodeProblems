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
#ifdef LISTES
      for (it=t[u].begin(); it!=t[u].end(); ++it) {
	int v = it->dest;
	relacher(u,v,it->weight);
	if (!visited[v]) q.push(vert(v,dist[v]));
#else
      for (int v=0; v<size; ++v) {
	if (t[u][v]>0) {
	  relacher(u,v,w[u][v]); // SIP
	  if (!visited[v]) q.push(vert(v,dist[v]));
	}
#endif
      }
      visited[u] = true;
    }
  }
  return false; // RINN
}
