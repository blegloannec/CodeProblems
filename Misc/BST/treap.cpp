#include <iostream>
#include <cstdlib>
#include <cassert>
#include <vector>
using namespace std;

/* ===== Treap BST ====== */
typedef int val;

struct Node {
  val x;
  Node *p,*l,*r;
  int h;  // heap-style priority

  Node(val x, Node *p=NULL, Node *l=NULL, Node *r=NULL) : x(x),p(p),l(l),r(r) {
    h = rand();
  }
};

struct Treap {
  Node *root;

  Treap() {
    root = NULL;
  }

  ~Treap() {
    clear();
  }
  
  void rotate_left(Node *u);
  void rotate_right(Node *u);
  Node *find(val x) const;
  void upward_percolation(Node *u);
  void downward_percolation(Node *u);
  void insert(val x);
  Node *min(Node *u) const;
  Node *succ(Node *u) const;
  void _erase_in_line(Node *u);
  void erase(Node *u);
  void erase(val x);
  void clear(Node *u);
  void clear();
};

void Treap::rotate_left(Node *u) {
  Node *v = u->r;
  //assert(v!=NULL);
  u->r = v->l; if (u->r!=NULL) u->r->p = u;
  v->l = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

void Treap::rotate_right(Node *u) {
  Node *v = u->l;
  //assert(v!=NULL);
  u->l = v->r; if (u->l!=NULL) u->l->p = u;
  v->r = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

Node *Treap::find(val x) const {
  Node *u = root;
  while (u!=NULL && u->x!=x)
    u = x<=u->x ? u->l : u->r;
  return u;
}

void Treap::upward_percolation(Node *u) {
  while (u->p!=NULL && u->p->h > u->h) {
    if (u->p->l==u) rotate_right(u->p);
    else rotate_left(u->p);
  }
}

void Treap::downward_percolation(Node *u) {
  while ((u->l!=NULL && u->h > u->l->h) || (u->r!=NULL && u->h > u->r->h)) {
    if (u->r==NULL || (u->l!=NULL && u->l->h <= u->r->h)) rotate_right(u);
    else rotate_left(u);
  }
}

void Treap::insert(val x) {
  Node *u0 = NULL, *u = root;
  while (u!=NULL) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  u = new Node(x,u0);
  if (u0==NULL) root = u;
  else if (x<=u0->x) u0->l = u;
  else u0->r = u;
  upward_percolation(u);
}

Node *Treap::min(Node *u=NULL) const {
  if (u==NULL) u = root;
  if (u!=NULL)
    while (u->l!=NULL)
      u = u->l;
  return u;
}

Node *Treap::succ(Node *u) const {
  if (u->r!=NULL) return min(u->r);
  Node *u0 = u->p;
  while (u0!=NULL && u==u0->r) {
    u = u0;
    u0 = u->p;
  }
  return u0;
}

// deletes a node u having at most one child
void Treap::_erase_in_line(Node *u) {
  assert(u->l==NULL || u->r==NULL);
  Node *v = NULL;
  if (u->l!=NULL) v= u->l;
  else if (u->r!=NULL) v = u->r;
  if (u==root) root = v;  // we could as well test u->p==NULL
  else if (u->p->l==u) u->p->l = v;
  else u->p->r = v;
  if (v!=NULL) v->p = u->p;
  delete u;
}

void Treap::erase(Node *u) {
  if (u->l==NULL || u->r==NULL) _erase_in_line(u);
  else {
    Node *v = min(u->r);  // we could as well use succ(u)
    u->x = v->x;
    u->h = v->h;
    _erase_in_line(v);  // v has no left child
    downward_percolation(u);
  }
}

void Treap::erase(val x) {
  Node *u = find(x);
  assert(u!=NULL);
  erase(u);
}

void Treap::clear(Node *u) {
  if (u!=NULL) {
    clear(u->l);
    clear(u->r);
    delete u;
  }
}

void Treap::clear() {
  clear(root);
  root = NULL;
}
/* ===== END Treap ===== */


void traversal(Treap &T) {
  Node *u = T.min();
  while (u!=NULL) {
    cout << u->x << ' ';
    u = T.succ(u);
  }
  cout << endl;
}

void dfs_draw(Treap &T, Node *u, string path) {
  if (u==NULL) cout << path << " [shape=point];" << endl;
  else {
    cout << path << " [label=\"" << u->x << " " << u->h <<"\"];" << endl;
    cout << path << " -> " << path+"0" << ";" << endl;
    cout << path << " -> " << path+"1" << ";" << endl;;
    dfs_draw(T,u->l,path+"0");
    dfs_draw(T,u->r,path+"1");
  }
}

void draw(Treap &T) {
  cout << "digraph G {" << endl;
  dfs_draw(T,T.root,"U");
  cout << "}" << endl;
}

int main() {
  srand(42);
  Treap T;
  int n = 5000000, m = 5000;
  vector<int> C(n),X(n);
  for (int i=0; i<n; ++i) {
    C[i] = rand()%3;
    X[i] = rand()%m;
  }
  for (int i=0; i<n; ++i) {
    int x = X[i];
    if (C[i]>0) T.insert(x);
    else if (T.find(x)!=NULL) T.erase(x);
  }
  //traversal(T);
  return 0;
}
