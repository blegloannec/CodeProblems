#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <ctime>
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
    next.resize(d+1);
  }
};

// find the last position to insert x
// used by default for existence test and "stable" insertion
// we trust RVO (Return Value Optimization) here
skiplinks sl_find(SkipLink *L, vtype x) {
  skiplinks pred(L->next.size());
  for (int d=L->next.size()-1; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<=x)
      L = L->next[d];
    pred[d] = L;
  }
  return pred;
}

// find the first position to insert x (simple < instead of <=)
// used for removal
skiplinks sl_find_lower(SkipLink *L, vtype x) {
  skiplinks pred(L->next.size());
  for (int d=L->next.size()-1; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<x)
      L = L->next[d];
    pred[d] = L;
  }
  return pred;
}

bool sl_exists(SkipLink *L, vtype x) {
  skiplinks pred = sl_find(L,x);
  return pred[0]->value==x;
}

int rand_depth(int depth) {
  int n = rand();
  int d = 0;
  while (d<depth && n&1) {
    ++d;
    n >>= 1;
  }
  return d;
}

void sl_insert(SkipLink *L, vtype x) {
  int at_depth = rand_depth(L->next.size()-1);
  skiplinks pred = sl_find(L,x);
  SkipLink *nouv = new SkipLink(at_depth,x);
  for (int d=at_depth; d>=0; --d) {
    nouv->next[d] = pred[d]->next[d];
    pred[d]->next[d] = nouv;
  }
}

// remove x (x itself if it exists)
void sl_remove(SkipLink *L, vtype x) {
  skiplinks pred = sl_find_lower(L,x);
  SkipLink *rem = pred[0]->next[0];
  // checking consistence of the removal
  assert(rem!=NULL && rem->value==x);
  for (int d=rem->next.size()-1; d>=0; --d)
    pred[d]->next[d] = rem->next[d];
  delete rem;
}

void sl_print(SkipLink *L, int dstart=0) {
  for (int d=dstart; d>=0; --d) {
    SkipLink *L0 = L->next[d];
    while (L0!=NULL) {
      cout << L0->value << ' ';
      L0 = L0->next[d];
    }
    cout << endl;
  }
}


/* ===== Indexed Skip List ===== 
   Variant where you can compute the index of elements
   when looking for them without additional cost.
   Each element, say of depth n>0, has a list of n-1 counters.
   For i>0, counter nb i-1 contains the number of elements of depth <i
   between itself (included) and the next element of depth >=i (excluded).
   Said otherwise, counter nb i-1 contains the distance (in the whole list, depth 0)
   to the next element in the list of depth i.
   Counters of level 0 would always be 1, that is why we avoid implementing them.
   Time complexity of operations is the same as with standard Skip Lists, however
   the memory cost is almost doubled.
   This could be "improved" (in memory) in the following way:
    - only one counter for each element, the one for its depth
    - updating counters when inserting becomes trickier when the pred.
      at insertion depth is of a greater depth as we cannot directly derive
      the counter value for the inserted element! This value can however be
      computed the following way: take the next element in the insertion depth list
      and do a fresh search for it (using its value AND pointer to identify it)
      to compute its index, now we know the required distance.
*/
struct IdxSkipLink;

typedef vector<IdxSkipLink*> idxskiplinks;
typedef vector<int> counters;

// the depth of a link is not explicitely kept, it is given by next.size()-1
// IMPORTANT: default value INT_MIN is used for the head, it always has to be
// a "-infinity" for the type/data used (int here, we could use -1 for non-negative
// integers, etc)
struct IdxSkipLink {
  vtype value;
  idxskiplinks next;
  counters count;

  IdxSkipLink(int d, vtype v=INT_MIN) {
    value = v;
    if (d>0) count.resize(d,1);
    next.resize(d+1);
  }
};

// computes the predecessors of x at each depth
// as well as their indices
void isl_find(IdxSkipLink *L, vtype x, idxskiplinks &pred, counters &pred_idx) {
  pred.resize(L->next.size());
  pred_idx.resize(L->next.size());
  int index = 0;
  for (int d=L->next.size()-1; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<=x) {
      index += d==0?1:L->count[d-1];
      L = L->next[d];
    }
    pred[d] = L;
    pred_idx[d] = index;
  }
}

// computes the "strict" predecessors of x at each depth
// as well as their indices
void isl_find_lower(IdxSkipLink *L, vtype x, idxskiplinks &pred, counters &pred_idx) {
  pred.resize(L->next.size());
  pred_idx.resize(L->next.size());
  int index = 0;
  for (int d=L->next.size()-1; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<x) {
      index += d==0?1:L->count[d-1];
      L = L->next[d];
    }
    pred[d] = L;
    pred_idx[d] = index;
  }
}

int isl_insert(IdxSkipLink *L, vtype x) {
  int at_depth = rand_depth(L->next.size()-1);
  idxskiplinks pred;
  counters pred_idx;
  isl_find(L,x,pred,pred_idx);
  IdxSkipLink *nouv = new IdxSkipLink(at_depth,x);
  int nidx = pred_idx[0]+1;
  for (int d=L->next.size()-1; d>=0; --d) {
    if (d>at_depth) ++(pred[d]->count[d-1]);
    else {
      if (d>0) {
	nouv->count[d-1] = pred_idx[d]+pred[d]->count[d-1] - nidx + 1;
	pred[d]->count[d-1] -= nouv->count[d-1] - 1;
      }
      nouv->next[d] = pred[d]->next[d];
      pred[d]->next[d] = nouv;
    }
  }
  return nidx;
}

void isl_clear(IdxSkipLink *L) {
  while (L!=NULL) {
    IdxSkipLink *L0 = L->next[0];
    delete L;
    L = L0;
  }
}

void isl_print(IdxSkipLink *L, int dstart=0) {
  for (int d=dstart; d>=0; --d) {
    IdxSkipLink *L0 = L;
    while (L0!=NULL) {
      if (L0->value>=0) cout << setw(2) << L0->value << ' ';
      if (d>0)
	for (int i=1; i<L0->count[d-1]; ++i)
	  cout << "   ";
      L0 = L0->next[d];
    }
    cout << endl;
  }
}

/* ===== TESTS ===== */
int main() {
  srand(time(NULL));
  int D = 5;
  IdxSkipLink *L = new IdxSkipLink(D);
  for (int i=0; i<20; ++i) {
    int x = rand()%100;
    cout << "inserting " << x << " at " << isl_insert(L,x) << endl;
    isl_print(L,D);
  }
  isl_print(L,D);
  return 0;
}
