void BFS(int start) {
  queue<int> q;
  int curr;
  liste::iterator it;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = it->dest;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;
      }
    }
  }
}

bool BFS(int start, int dest) {
  // teste l'accessibilite
  if (start==dest) return true;
  queue<int> q;
  int curr;
  liste::iterator it;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = it->dest;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;
	if (d==dest) return true;
      }
    }
  }
  return false;
}
