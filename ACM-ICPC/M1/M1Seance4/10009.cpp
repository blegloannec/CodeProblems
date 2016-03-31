#include <iostream>
#include <vector>
#include <queue>
#include <list>

using namespace std;

#define MAX 26

typedef vector<int> liste;
int size;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
int etage[MAX];

int l2n[MAX];
char n2l[MAX];

void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
  etage[start] = 0;
}

void BFS(int start) {
  queue<int> q;
  int curr;
  liste::iterator it;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = *it;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;
        etage[d] = etage[curr]+1;
      }
    }
  }
}

int main() {
  string a,b;
  int cas,m,n;
  for (int i=0; i<26; ++i) {
    n2l[i] = -1;
    l2n[i] = -1;
  }

  cin >> cas;
  while (cas-->0) {
    cin >> m >> n;
    size = 0;
    for (int i=0; i<m; ++i) {
      cin >> a >> b;
      if (l2n[(int)a[0]-'A'] < 0) {
        l2n[(int)a[0]-'A'] = size;
        n2l[size] = a[0];
        ++size;
      }
      if (l2n[(int)b[0]-'A'] < 0) {
        l2n[(int)b[0]-'A'] = size;
        n2l[size] = b[0];
        ++size;
      }
      int c = l2n[a[0]-'A'];
      int d = l2n[b[0]-'A'];
      t[c].push_back(d);
      t[d].push_back(c);
    }
    BFS(l2n['R'-'A']);

    list<char> r1,r2;
    list<char>::iterator it;
    
    for (int i=0; i<n; ++i) {
      cin >> a >> b;

      int c,d;
      c = l2n[a[0]-'A'];
      d = l2n[b[0]-'A'];
      while (etage[c] > etage[d]) {
        r1.push_back(n2l[c]);
        c = pred[c];
      }
      while (etage[d] > etage[c]) {
        r2.push_front(n2l[d]);
        d = pred[d];
      }
      while (c != d) {
        r1.push_back(n2l[c]);
        c = pred[c];
        r2.push_front(n2l[d]);
        d = pred[d];
      }
      r1.push_back(n2l[c]);
      for (it=r1.begin(); it!=r1.end(); ++it)
        cout << *it;
      for (it=r2.begin(); it!=r2.end(); ++it)
        cout << *it;
      cout << '\n';
      r1.clear();
      r2.clear();
    }
    
    if (cas>0) cout << '\n';
    
    for (int i=0; i<26; ++i) {
      t[i].clear();
      n2l[i] = -1;
      l2n[i] = -1;
    }
  }

  return 0;
}
