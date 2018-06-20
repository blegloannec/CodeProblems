#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

class BSTStructure {
public:
  virtual bool exists(int x) = 0;
  virtual void insert(int x) = 0;
  virtual void erase(int x) = 0;
  virtual void clear() = 0;
};

double testcase(int n, int m, int seed, BSTStructure *S) {
  srand(seed);
  vector<int> C(n),X(n);
  for (int i=0; i<n; ++i) {
    C[i] = rand()%3;
    X[i] = rand()%m;
  }
  clock_t t = clock();
  for (int i=0; i<n; ++i) {
    if (C[i]>0) S->insert(X[i]);
    else if (S->exists(X[i])) S->erase(X[i]);
  }
  t = clock()-t;
  double s = (double)t/CLOCKS_PER_SEC;
  return s;
}

void bench(BSTStructure *S) {
  cout.precision(2);
  cout << fixed;
  cout << testcase(500000,5000,42,S) << 's';
  cout << '\t' << testcase(5000000,5000,42,S) << 's';
  cout << '\t' << testcase(5000000,500000,54,S) << 's';
  cout << '\t' << testcase(10000000,5000000,55,S) << 's' << endl;
  S->clear();
}
