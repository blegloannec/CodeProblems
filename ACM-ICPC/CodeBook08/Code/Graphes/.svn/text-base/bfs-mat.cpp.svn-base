void BFS(int start) {
  queue<int> q;
  int curr;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (int i=0; i<size; ++i)
      if ((t[curr][i]>0)&&(pred[i]<0)) {
	q.push(i);
	pred[i] = curr;
      }
  }
}


bool BFS(int start, int dest) {
  // teste l'accessibilite
  if (start==dest) return true;
  queue<int> q;
  int curr;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (int i=0; i<size; ++i)
      if ((t[curr][i]>0)&&(pred[i]<0)) {
	q.push(i);
	pred[i] = curr;
	if (i==dest) return true;
      }
  }
  return false;
}
