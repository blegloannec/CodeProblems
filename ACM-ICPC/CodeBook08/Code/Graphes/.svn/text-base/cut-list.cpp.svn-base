// t le graphe residuel
void DFS(int start) {
  liste::iterator it;
  for (it=t[start].begin(); it!=t[start].end(); ++it) {
    int d = it->dest;
    if (pred[d]<0) {
      pred[d] = start;
      DFS(d);
    }
  }
}

// t0 le graphe initial
void cut_edges(int source) {
  liste::iterator it;
  clear_pred(source);
  DFS(source);
  for (int i=0; i<size; ++i)
    if (pred[i]>=0) 
      for (it=t0[i].begin(); it!=t0[i].end(); ++it)
	if (pred[it->dest]<0) 
	  cout << i << ' ' << it->dest << '\n';
}
