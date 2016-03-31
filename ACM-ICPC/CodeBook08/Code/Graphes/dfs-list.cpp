// INITIALISER  clear_pred(start);
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

// INITIALISER clear_pred(start);
bool DFS(int start, int dest) {
  // teste l'accessibilite de dest depuis start
  if (start==dest) return true; 
  liste::iterator it;
  for (it=t[start].begin(); it!=t[start].end(); ++it) {
    int d = it->dest;
    if (pred[d]<0) {
      pred[d] = start;
      if (DFS(d,dest)) return true; 
    }
  }
  return false; 
}
