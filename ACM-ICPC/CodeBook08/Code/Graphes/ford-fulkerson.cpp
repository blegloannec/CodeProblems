#ifdef MATRICES
int f[MAX][MAX]; // tableau du flot
#else
liste f[MAX]; // flot
liste::iterator predit[MAX]; // pointeurs sur les aretes rencontrees
/* Ajouter ce code dans le BFS :
   Juste apres :
   pred[d] = curr;
   Ajouter :
   predit[d] = it; */
void addFlow(liste t[], int src, int dst, int cap) {
  liste::iterator it = t[src].begin();
  while (it!=t[src].end()) {
    if (it->dest == dst) {
      it->weight += cap;
      if (it->weight == 0) t[src].erase(it);
      return;
    }
    ++it;
  }
  t[src].push_back(edge(dst,cap));
}
#endif

int ford_fulkerson(int source, int dest) {
  int v,cf,p,res;
  // Initialisation RINN
#ifdef MATRICES
  for (int i=0; i<size; ++i)
    for (int j=0; j<size; ++j)
      f[i][j] = 0;
#else
  for (int i=0; i<size; ++i) f[i].clear();
#endif
  // tant que l'on trouve un chemin augmentant
  while (BFS(source,dest)) { 
    // Tant que l'on touve un chemin de la source au puits 
    v = pred[dest]; // on suppose source =/= dest
#ifdef MATRICES
    cf = t[v][dest];
#else
    cf = predit[dest]->weight;
#endif
    while (v!=source) {
      p = pred[v];
#ifdef MATRICES
      cf = min(cf,t[p][v]);
#else
      cf = min(cf, predit[v]->weight);
#endif
      v = p;
    }
    v = dest;
    while (v!=source) {
      p = pred[v];
#ifdef MATRICES
      f[p][v] += cf;
      t[p][v] -= cf;
      f[v][p] -= cf;
      t[v][p] += cf;
#else
      addFlow(f,p,v,cf);
      predit[v]->weight -= cf;
      if (predit[v]->weight==0) f[p].erase(predit[v]);
      addFlow(f,v,p,-cf);
      addFlow(t,v,p,cf);
#endif
      v = p;
    }
  }
  // Calcul du maxflow RINN
  res = 0;
#ifdef MATRICES
  for (int j=0; j<size; ++j) res += f[source][j];
#else
  liste::iterator it;
  for (it=f[source].begin(); it!=f[source].end(); ++it) 
    res += it->weight;
#endif
  return res;
}
