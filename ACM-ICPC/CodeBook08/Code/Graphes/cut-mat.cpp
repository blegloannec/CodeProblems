// t le graphe residuel
void DFS(int start) {
  for (int i=0; i<size; ++i)
    if ((t[start][i]>0)&&(pred[i]<0)) {
      pred[i] = start;
      DFS(i);
    }
}

// t0 le graphe initial
void cut_edges(int source) {
  clear_pred(source);
  DFS(source); // dans le graphe t residuel
  for (int i=0; i<size; ++i) 
    if (pred[i]>=0)
      for (int j=0; j<size; ++j)
	if ((t0[i][j]>0)&&(pred[j]<0)) 
	  cout << i << ' ' << j << '\n';
}
