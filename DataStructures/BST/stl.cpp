#include <iostream>
#include <cstdlib>
#include <set>
#include "benchmark.hpp"
using namespace std;

void traversal(multiset<int> &T) {
  for (auto it=T.begin(); it!=T.end(); ++it) {
    cout << *it << " ";
  }
  cout << endl;
}

/*
int main() {
  srand(42);
  multiset<int> T;
  int n = 5000000, m = 5000;
  for (int i=0; i<n; ++i) {
    int c = rand()%3, x = rand()%m;
    if (c>0) T.insert(x);
    else {
      auto it = T.find(x);
      if (it!=T.end()) T.erase(it);
    }
  }
  traversal(T);
  return 0;
}
*/

class BST_STL : public BSTStructure {
public:
  multiset<int> T;
  virtual bool exists(int x) {return T.find(x)!=T.end();}
  virtual void insert(int x) {T.insert(x);}
  virtual void erase(int x) {T.erase(T.find(x));}
  virtual void clear() {T.clear();}
};

int main() {
  BST_STL S;
  bench(&S);
  return 0;
}
