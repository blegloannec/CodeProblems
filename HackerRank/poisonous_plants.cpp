/*
  O(n) approach using linked lists
  Each non-increasing chain of the input is stocked as a linked list
  4->3 | 7->5 | 6->4->2
  At each step, the first element of each chain, except the first,
  is eliminated and chains that "connect" (non-increasingly) are merged
  4->3 | 5 | 4->2  leading to  4->3 | 5->4->2
  Then (step 2): 4->3 | 4->2
  Then (step 3): 4->3->2
  We stop when there is a single chain left.
  Merging is done in O(1) with linked lists, hence the complexity of a step is
  the number of chains at that step, i.e. the number of eliminated elements
  at that step. Thus, as an element is eliminated at most once, the total
  complexity is O(n).

  The editorial uses a nice stack-based O(n) approach.
*/
#include <iostream>
#include <vector>
using namespace std;

struct Link {
  int x;
  Link *L,*R;

  Link(int x) : x(x) {
    L = R = NULL;
  }
};

struct List {
  Link *Front,*Back;

  List() : Front(NULL), Back(NULL) {}

  bool empty() const {
    return Front==NULL;
  }
  
  void pop_front() {
    if (Front!=NULL) {
      Link *F = Front;
      Front = Front->R;
      if (Front!=NULL) Front->L = NULL;
      delete F;
    }
  }
  
  void push_back(Link *B) {
    if (empty()) {
      Front = Back = B;
      B->L = B->R = NULL;
    }
    else {
      Back->R = B;
      B->L = Back;
      B->R = NULL;
      Back = B;
    }
  }
};

void merge(List &A, List &B) {
  A.Back->R = B.Front;
  B.Front->L = A.Back;
  A.Back = B.Back;
}

int main() {
  int n;
  cin >> n;
  vector<int> P(n),Q;
  for (int i=0; i<n; ++i) cin >> P[i];
  vector<List> S;
  for (int i=0; i<n; ++i) {
    if (i==0 || P[i-1]<P[i]) S.push_back(List());
    S.back().push_back(new Link(P[i]));
  }
  int cpt = 0;
  while (S.size()>1) {
    vector<List> T;
    T.push_back(S[0]);
    for (int i=1; i<(int)S.size(); ++i) {
      S[i].pop_front();
      if (!S[i].empty()) {
	if (!T.empty() && T.back().Back->x>=S[i].Front->x) merge(T.back(),S[i]);
	else T.push_back(S[i]);
      }
    }
    S = T;
    ++cpt;
  }
  cout << cpt << endl;
  return 0;
}
