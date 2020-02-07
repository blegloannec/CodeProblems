#include <iostream>
#include <vector>
#include <queue>
using namespace std;


/* ===== BST ====== */
struct Node {
  int x;
  Node *l,*r;

  Node(int x, Node *l=NULL, Node *r=NULL) : x(x),l(l),r(r) {}
};

struct BST {
  Node *root = NULL;

  void insert(int x);

  template <typename F>
  void prefix_traversal(F f);

  template <typename F>
  void _prefix(F f, Node *u);

  template <typename F>
  void infix_traversal(F f);

  template <typename F>
  void _infix(F f, Node *u);

  template <typename F>
  void postfix_traversal(F f);

  template <typename F>
  void _postfix(F f, Node *u);

  template <typename F>
  void bfs_traversal(F f);
};

void BST::insert(int x) {
  Node *u0 = NULL, *u = root;
  while (u!=NULL) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  if (u0==NULL) root = new Node(x);
  else if (x<=u0->x) u0->l = new Node(x);
  else u0->r = new Node(x);
}

template <typename F>
void BST::prefix_traversal(F f) {
  _prefix(f, root);
}

template <typename F>
void BST::_prefix(F f, Node *u) {
  if (u!=NULL) {
    f(u);
    _prefix(f, u->l);
    _prefix(f, u->r);
  }
}

template <typename F>
void BST::infix_traversal(F f) {
  _infix(f, root);
}

template <typename F>
void BST::_infix(F f, Node *u) {
  if (u!=NULL) {
    _infix(f, u->l);
    f(u);
    _infix(f, u->r);
  }
}

template <typename F>
void BST::postfix_traversal(F f) {
  _postfix(f, root);
}

template <typename F>
void BST::_postfix(F f, Node *u) {
  if (u!=NULL) {
    _postfix(f, u->l);
    _postfix(f, u->r);
    f(u);
  }
}

template <typename F>
void BST::bfs_traversal(F f) {
  queue<Node*> Q;
  Q.push(root);
  while (!Q.empty()) {
    Node *u = Q.front();
    Q.pop();
    if (u!=NULL) {
      f(u);
      Q.push(u->l);
      Q.push(u->r);
    }
  }
}
/* ===== END BST ===== */


void print_array(vector<int> &A) {
  for (unsigned int i=0; i<A.size(); ++i)
    cout << A[i] << (i+1==A.size() ? '\n' : ' ');
}

int main() {
  BST T;
  int N;
  cin >> N;  
  for (int i=0; i<N; ++i) {
    int v;
    cin >> v;
    T.insert(v);
  }
  vector<int> Trace;
  auto fill_trace = [&Trace](Node* u) { Trace.push_back(u->x); };
  T.prefix_traversal(fill_trace);
  print_array(Trace);
  Trace.clear();
  T.infix_traversal(fill_trace);
  print_array(Trace);
  Trace.clear();
  T.postfix_traversal(fill_trace);
  print_array(Trace);
  Trace.clear();
  T.bfs_traversal(fill_trace);
  print_array(Trace);
  return 0;
}
