#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <vector>
#include <climits>
#include <cassert>
using namespace std;

/* ===== Skip List ===== */
struct SkipLink;

typedef int vtype;
typedef vector<SkipLink*> skiplinks;

// the depth of a link is not explicitely kept, it is given by next.size()-1
// IMPORTANT: default value INT_MIN is used for the head, it always has to be
// a "-infinity" for the type/data used (int here, we could use -1 for non-negative
// integers, etc)
struct SkipLink {
  vtype value;
  skiplinks next;

  SkipLink(int d, vtype v=INT_MIN) {
    value = v;
    next.resize(d+1,NULL);
  }

  int depth() {
    return (int)next.size()-1;
  }
};

struct SkipList {
  int depth;
  SkipLink *head;

  SkipList(int d) {
    depth = d;
    head = new SkipLink(depth);
  }

  ~SkipList() {
    clear();
    delete head;
  }
  
  skiplinks find(vtype x);
  skiplinks find_lower(vtype x);
  bool exists(vtype x);
  int rand_depth();
  SkipLink *insert(vtype x);
  void remove(vtype x);
  void print(int max_depth);
  void clear();
};

// find the last position to insert x
// used by default for existence test and "stable" insertion
// we trust RVO (Return Value Optimization) here
skiplinks SkipList::find(vtype x) {
  SkipLink *L = head;
  skiplinks pred(depth+1);
  for (int d=depth; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<=x)
      L = L->next[d];
    pred[d] = L;
  }
  return pred;
}

// find the first position to insert x (simple < instead of <=)
// used for removal
skiplinks SkipList::find_lower(vtype x) {
  SkipLink *L = head;
  skiplinks pred(depth+1);
  for (int d=depth; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<x)
      L = L->next[d];
    pred[d] = L;
  }
  return pred;
}

bool SkipList::exists(vtype x) {
  skiplinks pred = find(x);
  return pred[0]->value==x;
}

int SkipList::rand_depth() {
  int n = rand();
  int d = 0;
  while (d<depth && n&1) {
    ++d;
    n >>= 1;
  }
  return d;
}

SkipLink *SkipList::insert(vtype x) {
  int at_depth = rand_depth();
  skiplinks pred = find(x);
  SkipLink *nouv = new SkipLink(at_depth,x);
  for (int d=at_depth; d>=0; --d) {
    nouv->next[d] = pred[d]->next[d];
    pred[d]->next[d] = nouv;
  }
  return nouv;
}

// remove x (x itself if it exists)
void SkipList::remove(vtype x) {
  skiplinks pred = find_lower(x);
  SkipLink *rem = pred[0]->next[0];
  // checking consistence of the removal
  assert(rem!=NULL && rem->value==x);
  for (int d=rem->depth(); d>=0; --d)
    pred[d]->next[d] = rem->next[d];
  delete rem;
}

void SkipList::print(int max_depth=0) {
  for (int d=max_depth; d>=0; --d) {
    SkipLink *L0 = head->next[d];
    while (L0!=NULL) {
      cout << L0->value << ' ';
      L0 = L0->next[d];
    }
    cout << endl;
  }
}

void SkipList::clear() {
  SkipLink *L = head->next[0];
  while (L!=NULL) {
    SkipLink *L0 = L;
    L = L->next[0];
    delete L0;
  }
  for (int i=0; i<=depth; ++i) head->next[i] = NULL;
}


/* ===== TESTS ===== */
/*
int main() {
  srand(time(NULL));
  int D = 5;
  SkipList L(D);
  for (int i=0; i<20; ++i) {
    int x = rand()%100;
    L.insert(x);
    //cout << "inserting " << x << " at " << L.insert(x) << endl;
    L.print(D);
  }
  L.print(D);
  return 0;
}*/

int main() {
  srand(42);
  int n = 5000000, m = 5000;
  SkipList L((int)log2(n)+1);
  vector<int> C(n),X(n);
  for (int i=0; i<n; ++i) {
    C[i] = rand()%3;
    X[i] = rand()%m;
  }
  for (int i=0; i<n; ++i) {
    int x = X[i];
    if (C[i]>0) L.insert(x);
    else if (L.exists(x)) L.remove(x);
  }
  //L.print();
  return 0;
}
