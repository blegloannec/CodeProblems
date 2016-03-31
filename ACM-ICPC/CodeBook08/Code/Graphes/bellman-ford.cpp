#define INTMAX 5000000
int dist[MAX];

void relacher(int u, int v, int w) {
  int d2 = dist[u]+w;
  if (dist[v]>d2) {
    dist[v] = d2;
    pred[v] = u;
  }
}

bool bellman_ford(int start) { 
  // detecte les cycles de poids negatif
  liste::iterator it;
  for (int v=0; v<size; v++) { // initialisation
    dist[v] = INTMAX;
    pred[v] = -1;
  }
  dist[start] = 0;
  for (int j=1; j<size; j++) // relachements
    for (int u=0; u<size; u++) 
#ifdef LISTES
      for (it=t[u].begin(); it!=t[u].end(); it++) 
	relacher(u,it->dest,it->weight);
#else 
      for (int v=0; v<size; ++v) 
	if (t[u][v]>0) relacher(u,v,w[u][v]); // SIP
#endif
  // detection des cycles negatifs, RINN
  for (int u=0; u<size; u++) 
#ifdef LISTES
    for (it=t[u].begin(); it!=t[u].end(); it++) 
      if (dist[it->dest]>dist[u]+(it->weight)) 
#else 
    for (int v=0; v<size; ++v) 
      if ((t[u][v]>0)&&(dist[v]>dist[u]+w[u][v])) // SIP
#endif    
	return false;
  return true;  
}
