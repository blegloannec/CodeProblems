// INITIALISER clear_pred(start);
void DFS(int start) {
  for (int i=0; i<size; ++i)
    if ((t[start][i]>0)&&(pred[i]<0)) {
      pred[i] = start;
      DFS(i);
    }
}

// INITIALISER clear_pred(start);
bool DFS(int start, int dest) {
  // teste si dest est accessible depuis start
  if (start==dest) return true;
  for (int i=0; i<size; ++i)
    if ((t[start][i]>0)&&(pred[i]<0)) {
      pred[i] = start;
      if (DFS(i,dest)) return true;
    }
  return false;
}
