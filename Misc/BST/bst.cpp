#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

/* ===== BST ====== */
typedef int val;

struct Node {
  val x;
  Node *p,*l,*r;

  Node(val x, Node *p=NULL, Node *l=NULL, Node *r=NULL) : x(x),p(p),l(l),r(r) {}
};

struct BST {
  Node *root;

  BST() {
    root = NULL;
  }

  Node *find(val x) const;
  void insert(val x);
  Node *min(Node *u) const;
  Node *succ(Node *u) const;
  void _erase_in_line(Node *u);
  void erase(Node *u);
  void erase(val x);
  void clear(Node *u);
  void clear();
};

Node *BST::find(val x) const {
  Node *u = root;
  while (u!=NULL && u->x!=x)
    u = x<=u->x ? u->l : u->r;
  return u;
}

void BST::insert(val x) {
  Node *u0 = NULL, *u = root;
  while (u!=NULL) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  if (u0==NULL) root = new Node(x);
  else if (x<=u0->x) u0->l = new Node(x,u0);
  else u0->r = new Node(x,u0);
}

Node *BST::min(Node *u=NULL) const {
  if (u==NULL) u = root;
  if (u!=NULL)
    while (u->l!=NULL)
      u = u->l;
  return u;
}

Node *BST::succ(Node *u) const {
  if (u->r!=NULL) return min(u->r);
  Node *u0 = u->p;
  while (u0!=NULL && u==u0->r) {
    u = u0;
    u0 = u->p;
  }
  return u0;
}

// deletes a node u having at most one child
void BST::_erase_in_line(Node *u) {
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

void BST::erase(Node *u) {
  if (u->l==NULL || u->r==NULL) _erase_in_line(u);
  else {
    Node *v = min(u->r);  // we could as well use succ(u)
    u->x = v->x;
    _erase_in_line(v);  // v has no left child
  }
}

void BST::erase(val x) {
  Node *u = find(x);
  assert(u!=NULL);
  erase(u);
}

void BST::clear(Node *u) {
  if (u!=NULL) {
    clear(u->l);
    clear(u->r);
    delete u;
  }
}

void BST::clear() {
  clear(root);
  root = NULL;
}
/* ===== END BST ===== */


void traversal(BST &T) {
  Node *u = T.min();
  while (u!=NULL) {
    cout << u->x << ' ';
    u = T.succ(u);
  }
  cout << endl;
}

int main() {
  srand(42);
  BST T;
  int n = 5000000, m = 5000;
  for (int i=0; i<n; ++i) {
    int c = rand()%3, x = rand()%m;
    if (c>0) T.insert(x);
    else if (T.find(x)!=NULL) T.erase(x);
  }
  return 0;
}
