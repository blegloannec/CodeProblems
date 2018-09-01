#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;

vector<int> gene2trie,range_start,range_end;
vector< vector<int> > forward_link;

/*
  Aho-Corasick, Efficient String Matching, 1975
  Using that algo alone (in C++) is sufficient to pass
  every testcase except the #13.
  For that one, a trickier offline computation process is needed.
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
      // ajout pb : gene --> trie node
      gene2trie[iw] = s;
    }
    // AJOUT PB
    forward_link.resize(G.size());
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
	  // AJOUT PB : trie node forward link
	  forward_link[B[s0]<0?0:B[s0]].push_back(s0);
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

int timer = 0;
// Forward tree building for ranges
void forward_dfs(int u=0) {
  assert(u>=0);
  assert(u<(int)range_start.size());
  assert(u<(int)range_end.size());
  range_start[u] = ++timer;
  for (vector<int>::iterator it=forward_link[u].begin(); it!=forward_link[u].end(); ++it)
    forward_dfs(*it);
  range_end[u] = timer;
}


/* Fenwick Trees for ranges */
typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, ent v);

  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,-v);
}

/*
// version classique
ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}
*/

// variante range
ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}


/* ===== MAIN ===== */
int main() {
  int n,s;
  long long minH = 1LL<<62;
  long long maxH = 0LL;
  cin >> n;
  gene2trie.resize(n);
  vector<string> G(n);
  for (int i=0; i<n; ++i) cin >> G[i];
  ACTrie A(G);
  range_start.resize(A.G.size());
  range_end.resize(A.G.size());
  forward_dfs();
  Fenwick FT(timer+1);
  vector<int> H(n);
  for (int i=0; i<n; ++i) cin >> H[i];
  cin >> s;

  /*
  for (int i=0; i<s; ++i) {
    int start,end;
    string d;
    cin >> start >> end >> d;
    long long  h = 0LL;
    vector<match> M = A.find(d);
    for (vector<match>::iterator it=M.begin(); it!=M.end(); ++it) {
      vector<int> O = A.output(it->second);
      for (vector<int>::iterator jt=O.begin(); jt!=O.end(); ++jt)
        if (start<=*jt && *jt<=end) h += H[*jt];
    }
    if (h<minH) minH = h;
    if (h>maxH) maxH = h;
  }
  */

  vector<string> strands;
  vector<long long> strandH(s,-1LL);
  vector< pair<int,int> > timeline;
  for (int i=0; i<s; ++i) {
    int start,end;
    string d;
    cin >> start >> end >> d;
    strands.push_back(d);
    if (start>0) timeline.push_back(make_pair(start-1,i));
    else strandH[i] = 0;
    timeline.push_back(make_pair(end,i));
  }
  sort(timeline.begin(),timeline.end());
  int ti = 0;
  for (int t=0; t<n; ++t) {
    FT.range_add(range_start[gene2trie[t]],range_end[gene2trie[t]],H[t]);
    while (ti<(int)timeline.size() && timeline[ti].first==t) {
      int si = timeline[ti].second;
      long long h = 0LL;
      vector<match> M = A.find(strands[si]);
      for (vector<match>::iterator it=M.begin(); it!=M.end(); ++it)
        h += FT[range_start[it->second]];
      if (strandH[si]<0) strandH[si] = h;
      else {
	h -= strandH[si];	
	strandH[si] = h;
	if (h<minH) minH = h;
	if (h>maxH) maxH = h;
      }
      ++ti;
    }
  }

  cout << minH << ' ' << maxH << endl;
  return 0;
}
