#include <iostream>
#include <vector>
using namespace std;

/* 
   Trie + Backtracking with memoization
   Pretty simple actually (the problem is tagged "very hard")!
*/

typedef long long ll;
typedef vector<bool> morse_string;

/*
  Binary Trie for morse words
  terminal is the number of morse words of the dictionary 
  that end on the current node (we know there are no duplicates
  in the original dictionary, but there might be some once
  translated into morse code)
*/
struct MorseTree {
  MorseTree *l,*r;
  ll terminal;
  
  MorseTree() {
    l = NULL;
    r = NULL;
    terminal = 0;
  }

  void insert(const morse_string &s, unsigned int i);
};
  
void MorseTree::insert(const morse_string &s, unsigned int i=0) {
  if (i==s.size()) ++terminal;
  else if (s[i]) {
    if (r==NULL) r = new MorseTree();
    r->insert(s,i+1);
  }
  else {
    if (l==NULL) l = new MorseTree();
    l->insert(s,i+1);
  }
}

morse_string L; // morse string to cut
MorseTree *LT = new MorseTree(); // Trie root
vector<ll> memo;

// Backtracking + Memoization (only when on root node, i.e. actual cuts)
ll word_split(MorseTree *lt, unsigned int i=0) {
  if (i==L.size()) return lt->terminal;
  if (lt==LT && memo[i]>=0)
    return memo[i];
  ll res = 0;
  // terminal node, possible cut here
  if (lt->terminal>0) res += lt->terminal * word_split(LT,i);
  // we try to continue, not cutting here
  MorseTree *child = (L[i] ? lt->r : lt->l);
  if (child!=NULL) res += word_split(child,i+1);
  if (lt==LT) memo[i] = res;
  return res;
}

// Morse code
vector<morse_string> M = {{0,1},{1,0,0,0},{1,0,1,0},{1,0,0},{0},{0,0,1,0},{1,1,0},{0,0,0,0},{0,0},{0,1,1,1},{1,0,1},{0,1,0,0},{1,1},{1,0},{1,1,1},{0,1,1,0},{1,1,0,1},{0,1,0},{0,0,0},{1},{0,0,1},{0,0,0,1},{0,1,1},{1,0,0,1},{1,0,1,1},{1,1,0,0}};

// Translate an english word into morse code
morse_string word2morse(const string &W) {
  morse_string res;
  for (unsigned int i=0; i<W.size(); ++i) {
    int c = (int)W[i] - (int)'A';
    for (morse_string::iterator it=M[c].begin(); it!=M[c].end(); ++it)
      res.push_back(*it);
  }
  return res;
}

int main() {
  string L0;
  cin >> L0;
  for (unsigned int i=0; i<L0.size(); ++i)
    L.push_back(L0[i]=='-');
  int N;
  cin >> N;
  for (int i=0; i<N; ++i) {
    string W;
    cin >> W;
    LT->insert(word2morse(W));
  }
  memo.resize(L.size(),-1);
  cout << word_split(LT) << endl;
  return 0;
}
