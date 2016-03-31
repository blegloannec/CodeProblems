#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define MAX_BRANCH 26
#define BEG_CHAR 'A'

struct lextree {
  bool term; // noeud terminal RINN
  vector<lextree*> l;
  lextree(): term(false) {
    l.resize(MAX_BRANCH, NULL);
  };
  ~lextree() {
    for (int i = 0; i < MAX_BRANCH; ++i)
      delete l[i];
  };
  void insert(const string s) {
    lextree *curr=this;
    int i=0;
    char c;
    while (s[i]) {
      c = s[i]-BEG_CHAR;
      if (curr->l[c] == NULL)
        curr->l[c] = new lextree();
      curr = curr->l[c];
      ++i;
    }
    curr->term = true;
  };
  bool accept(const string s) {
    lextree *curr=this;
    int i=0;
    char c;
    while (s[i]) {
      c = s[i]-BEG_CHAR;
      if (curr->l[c] == NULL)
        return false;
      curr = curr->l[c];
      ++i;
    }
    return curr->term;
  };
};
