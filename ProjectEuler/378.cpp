#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <climits>
using namespace std;

typedef long long ent;
typedef pair<int,int> couple;

/*
  Computing dT(n) is easy from the decompositions of n and n+1;
  (that are coprime, which make it even easier);
  Given j, the number of triples "centered" in j is exactly the
  #{triangle nb before j with greater dT} * #{triangle nb after j with less dT}
  Here we use custom "indexed" Skip Lists to count, which takes a lot of memory...
  Runs in ~100s with -O3
  Should have used Binary Indexed (or Fenwick) Trees.
*/

/* ===== Indexed Skip List ===== */
struct IdxSkipLink;

typedef vector<IdxSkipLink*> idxskiplinks;
typedef vector<int> counters;

struct IdxSkipLink {
  int value;
  idxskiplinks next;
  counters count;

  IdxSkipLink(int d, int v=INT_MIN) {
    value = v;
    if (d>0) count.resize(d,1);
    next.resize(d+1);
  }
};

void isl_find(IdxSkipLink *L, int x, idxskiplinks &pred, counters &pred_idx) {
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

void isl_find_lower(IdxSkipLink *L, int x, idxskiplinks &pred, counters &pred_idx) {
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

int rand_depth(int depth) {
  int n = rand();
  int d = 0;
  while (d<depth && n&1) {
    ++d;
    n >>= 1;
  }
  return d;
}

int isl_insert(IdxSkipLink *L, int x, bool lower=false) {
  int at_depth = rand_depth(L->next.size()-1);
  idxskiplinks pred;
  counters pred_idx;
  if (lower) isl_find_lower(L,x,pred,pred_idx);
  else isl_find(L,x,pred,pred_idx);
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
/* =============== */

const int N = 60000002;
const int dmax = 25;
const ent M = 1000000000000000000;
vector<bool> P(N,true);
vector<int> F(N,1);
vector<int> dT(N,0);
vector<int> nb_greater_before(N,0);
vector<int> nb_less_after(N,0);

void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

void decomp(int n, vector<couple> &D) {
  int p = F[n];
  n /= p;
  int m = 1;
  while (n%p==0) {
    n /= p;
    ++m;
  }
  D.push_back(couple(p,m));
  if (n>1) decomp(n,D);
}

int main() {
  srand(time(NULL));
  // Computing dT
  sieve_smallest_factor();
  int nbdn = 1;
  for (int n=1; n<N-1; ++n) {
    vector<couple> Divsnp1;
    decomp(n+1,Divsnp1);
    int nbdnp1 = 1;
    for (vector<couple>::iterator it=Divsnp1.begin(); it!=Divsnp1.end(); ++it)
      nbdnp1 *= it->first==2?it->second:it->second+1;
    dT[n] = nbdn*nbdnp1;
    nbdn = nbdnp1;
  }
  P.clear();
  F.clear();
  // Inserting in increasing index order
  IdxSkipLink *L = new IdxSkipLink(dmax);
  for (int i=1; i<N-1; ++i)
    nb_greater_before[i] = i-isl_insert(L,dT[i]);
  isl_clear(L);
  // Inserting in decreasing index order
  L = new IdxSkipLink(dmax);
  for (int i=N-2; i>0; --i)
    nb_less_after[i] = isl_insert(L,dT[i],true)-1;
  isl_clear(L);
  // Computing result
  ent res = 0;
  for (int n=1; n<N-1; ++n)
    res = (res + (ent)nb_greater_before[n]*(ent)nb_less_after[n])%M;
  cout << res << endl;
  return 0;
}
