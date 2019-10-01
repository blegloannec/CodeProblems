// adapted from UVa 10044
#include <bits/stdc++.h>
using namespace std;

const string erdos = "PAUL_ERDOS";
unordered_map<string, unordered_set<string> > G;
unordered_map<string,int> D;

void bfs() {
  queue<string> Q;
  D[erdos] = 0;
  if (G.find(erdos)!=G.end()) Q.push(erdos);
  while (!Q.empty()) {
    string a = Q.front(); Q.pop();
    for (string b : G[a])
      if (D.find(b)==D.end()) {
	D[b] = D[a]+1;
	Q.push(b);
      }
  }
}

int main() {
  vector<string> first_authors;
  string line;
  while (getline(cin,line)) {
    istringstream sline(line);
    vector<string> authors((istream_iterator<string>(sline)),istream_iterator<string>());
    first_authors.push_back(authors[0]);
    for (unsigned int i=1; i<authors.size(); ++i) {
      G[authors[0]].insert(authors[i]);
      G[authors[i]].insert(authors[0]);
    }
  }
  bfs();
  for (string line : first_authors) {
    if (D.find(line)==D.end()) cout << line << " no-connection" << endl;
    else cout << line << ' ' << D[line] << endl;			
  }
  return 0;
}
