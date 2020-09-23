#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;

struct TrieNode {
  array<TrieNode*, 26> child;
  TrieNode() { child.fill(NULL); }
};

int insert(TrieNode *trie, const string &s) {
  int l = 0;
  for (int i=(int)s.size()-1; i>=0; --i) {
    int c = s[i] - 'a';
    if (trie->child[c] == NULL)
      trie->child[c] = new TrieNode();
    else ++l;
    trie = trie->child[c];
  }
  return l == (int)s.size() ? 0 : l;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int N;
  cin >> N;
  vector<string> S(N);
  for (int n=0; n<N; ++n) cin >> S[n];
  sort(S.begin(), S.end(),
       [](const string &s, const string &t){ return s.size()>t.size(); });
  int res = 0;
  TrieNode trie;
  for (const string &s : S)
    res = max(res, insert(&trie, s));
  cout << res << endl;
  return 0;
}
