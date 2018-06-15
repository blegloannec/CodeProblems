#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <vector>
#include <climits>
#include <cassert>
using namespace std;


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

typedef int vtype;
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
    next.resize(d+1,NULL);
  }

  int depth() {
    return (int)next.size()-1;
  }
};

struct IdxSkipList {
  int depth;
  IdxSkipLink *head;

  IdxSkipList(int d) {
    depth = d;
    head = new IdxSkipLink(depth);
  }

  ~IdxSkipList() {
    clear();
    delete head;
  }
  
  void find(vtype x, idxskiplinks &pred, counters &pred_idx);
  void find_lower(vtype x, idxskiplinks &pred, counters &pred_idx);
  int rand_depth();
  int insert(vtype x);
  void print(int max_depth);
  void clear();
};

// computes the predecessors of x at each depth
// as well as their indices
void IdxSkipList::find(vtype x, idxskiplinks &pred, counters &pred_idx) {
  IdxSkipLink *L = head;
  pred.resize(depth+1);
  pred_idx.resize(depth+1);
  int index = 0;
  for (int d=depth; d>=0; --d) {
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
void IdxSkipList::find_lower(vtype x, idxskiplinks &pred, counters &pred_idx) {
  IdxSkipLink *L = head;
  pred.resize(depth+1);
  pred_idx.resize(depth+1);
  int index = 0;
  for (int d=depth; d>=0; --d) {
    while (L->next[d]!=NULL && L->next[d]->value<x) {
      index += d==0?1:L->count[d-1];
      L = L->next[d];
    }
    pred[d] = L;
    pred_idx[d] = index;
  }
}

int IdxSkipList::rand_depth() {
  int n = rand();
  int d = 0;
  while (d<depth && n&1) {
    ++d;
    n >>= 1;
  }
  return d;
}

int IdxSkipList::insert(vtype x) {
  int at_depth = rand_depth();
  idxskiplinks pred;
  counters pred_idx;
  find(x,pred,pred_idx);
  IdxSkipLink *nouv = new IdxSkipLink(at_depth,x);
  int nidx = pred_idx[0]+1;
  for (int d=depth; d>=0; --d) {
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

void IdxSkipList::print(int max_depth=0) {
  IdxSkipLink *L = head;
  for (int d=max_depth; d>=0; --d) {
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

void IdxSkipList::clear() {
  IdxSkipLink *L = head->next[0];
  while (L!=NULL) {
    IdxSkipLink *L0 = L->next[0];
    delete L;
    L = L0;
  }
  for (int i=0; i<=depth; ++i) head->next[i] = NULL;
}


/* ===== TESTS ===== */
int main() {
  srand(time(NULL));
  int D = 5;
  IdxSkipList L(D);
  for (int i=0; i<20; ++i) {
    int x = rand()%100;
    cout << "inserting " << x << " at " << L.insert(x) << endl;
    L.print(D);
  }
  L.print(D);
  return 0;
}
