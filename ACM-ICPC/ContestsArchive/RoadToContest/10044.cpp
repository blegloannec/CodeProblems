/*
  2205 on Archive, 10044 on UVa
  One of the worst input parsing/debugging ever...
  The input actually STRICTLY follows the format of the statement
  (no extra whitespaces within lines, nothing tricky there).
  EXCEPT there are some extra blank lines for some reason
  and, considering the input format, this is the last thing
  one would imagine wrong here.
*/

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

const string erdos = "Erdos, P.";
unordered_map<string, unordered_set<string> > G;
unordered_map<string,int> D;

void bfs() {
  queue<string> Q;
  D[erdos] = 0;
  if (G.find(erdos)!=G.end()) Q.push(erdos);
  while (!Q.empty()) {
    string a = Q.front(); Q.pop();
    for (auto ib=G[a].begin(); ib!=G[a].end(); ++ib)
      if (D.find(*ib)==D.end()) {
	D[*ib] = D[a]+1;
	Q.push(*ib);
      }
  }
}

int main() {
  int S;
  cin >> S;
  for (int s=1; s<=S; ++s) {
    int P,N;
    cin >> P >> N;
    string line;
    for (int p=0; p<P; ++p) {
      vector<string> authors;
      getline(cin,line);
      while (line.empty()) getline(cin,line); // eat empty lines
      int i = 0;
      bool comma = false;
      string curr;
      while (line[i]!=':') {
	if (line[i]==',') {
	  if (comma) {
	    comma = false;
	    authors.push_back(curr);
	    curr.clear();
	  }
	  else {
	    curr += line[i];
	    comma = true;
	  }
	}
	else if (!(curr.empty() && line[i]==' ')) curr += line[i];
	++i;
      }
      authors.push_back(curr);
      for (unsigned int i=0; i<authors.size(); ++i)
	for (unsigned int j=i+1; j<authors.size(); ++j) {
	  G[authors[i]].insert(authors[j]);
	  G[authors[j]].insert(authors[i]);
	}
    }
    bfs();
    cout << "Scenario " << s << endl;
    for (int n=0; n<N; ++n) {
      getline(cin,line);
      if (D.find(line)==D.end()) cout << line << " infinity" << endl;
      else cout << line << ' ' << D[line] << endl;			
    }
    // cleaning
    G.clear();
    D.clear();
  }
  return 0;
}
