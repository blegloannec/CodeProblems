#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/*
  Aho-Corasick, Efficient String Matching, 1975
*/

const int Alpha = 26;

int num(char c) {
  return (int)c-(int)'a';
}

typedef pair<int,int> match;

struct ACTrie {
  vector<string> W;
  vector< vector<int> > G,O;
  vector<int> F,B;

  int new_state();
  int g(int s, int c) const;
  vector<match> find(const string &S) const;
  vector<int> output(int s);
  
  ACTrie(const vector<string> &words) {
    W = words; // copy
    G.push_back(vector<int>(Alpha,-1));
    O.resize(1);
    F.push_back(-1);
    B.push_back(-1);
    for (int iw=0; iw<(int)W.size(); ++iw) {
      string w = W[iw];
      int s = 0;
      for (int ic=0; ic<(int)w.size(); ++ic) {
	int c = num(w[ic]);
	if (G[s][c]>=0) s = G[s][c];
	else {
	  int s0 = new_state();
	  G[s][c] = s0;
	  s = s0;
	}
      }
      O[s].push_back(iw);
    }
    // failure computation (BFS)
    queue<int> Q;
    Q.push(0);
    while (!Q.empty()) {
      int s = Q.front();
      Q.pop();
      for (int c=0; c<Alpha; ++c) {
	int s0 = G[s][c];
	if (s0>0) {
	  Q.push(s0);
	  if (s==0) F[s0] = 0;
	  else {
	    int f = F[s];
	    while (g(f,c)<0) f = F[f];
	    int f0 = g(f,c);
	    F[s0] = f0;
	    B[s0] = O[f0].empty() ? B[f0] : f0;
	  }
	}
      }
    }
  }
};

int ACTrie::new_state() {
  int s = G.size();
  G.push_back(vector<int>(Alpha,-1));
  O.resize(O.size()+1);
  F.push_back(-1);
  B.push_back(-1);
  return s;
}

int ACTrie::g(int s, int c) const {
  if (G[s][c]>=0) return G[s][c];
  return s==0 ? 0 : -1;
}

vector<match> ACTrie::find(const string &S) const {
  vector<match> M;
  int s = 0;
  for (int i=0; i<(int)S.size(); ++i) {
    int c = num(S[i]);
    while (g(s,c)<0) s = F[s];
    s = g(s,c);
    // renvoie le noeud du trie
    if (!O[s].empty() || B[s]>0) M.push_back(make_pair(i,s));
  }
  return M;
}

vector<int> ACTrie::output(int s) {
  vector<int> R;
  while (s>0) {
    for (vector<int>::iterator it=O[s].begin(); it!=O[s].end(); ++it)
      R.push_back(*it);
    s = B[s];
  }
  return R;
}

int main() {
  vector<string> W = {"he","she","is","hers"};
  ACTrie A(W);
  vector<match> M = A.find("ishers");
  for (vector<match>::iterator it=M.begin(); it!=M.end(); ++it) {
    vector<int> O = A.output(it->second);
    for (vector<int>::iterator jt=O.begin(); jt!=O.end(); ++jt)
      cout << '"' << W[*jt] << "\" found at " << it->first << endl; 
  }
  return 0;
}
