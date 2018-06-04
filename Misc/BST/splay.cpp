#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

/* 
   Sleator-Tarjan, Self-Adjusting Binary Search Trees
   Only the "splay-spirit" insertion/deletion are implemented here.
   Alternative "hybrid" implementations consists in using the standard
   BST insertion/deletion and splay afterwards on the inserted node /
   parent of the deleted node (as we do in any other balanced BST
   implementation: standard insertion/deletion followed by a re-balancing
   pass). The amortized analysis of these alternatives is theoretically
   slighty better, yet they do not seem to perform better in practice
   and are not as straightforwardly simple and elegant.
*/


/* ===== Splay BST ====== */
typedef int val;

struct Node {
  val x;
  Node *p,*l,*r;

  Node(val x, Node *p=NULL, Node *l=NULL, Node *r=NULL) : x(x),p(p),l(l),r(r) {
    if (l!=NULL) l->p = this;
    if (r!=NULL) r->p = this;
  }
};

struct Splay {
  Node *root;

  Splay(Node *r=NULL) {
    if (r!=NULL) {
      /*  !!  modifies r->p  !!  */
      root = r;
      root->p = NULL;
    }
    else root = NULL;
  }

  ~Splay() {
    clear();
  }

  void rotate_left(Node *u);
  void rotate_right(Node *u);
  void splay(Node *u);
  Node *access(val x);
  Node *access_max();
  void join(Node *u);
  pair<Node*,Node*> split(val x);
  void insert(val x);
  void erase(val x);
  Node *min(Node *u) const;
  Node *succ(Node *u);
  void clear(Node *u);
  void clear();
};

void Splay::rotate_left(Node *u) {
  Node *v = u->r;
  u->r = v->l; if (u->r!=NULL) u->r->p = u;
  v->l = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

void Splay::rotate_right(Node *u) {
  Node *v = u->l;
  u->l = v->r; if (u->l!=NULL) u->l->p = u;
  v->r = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

void Splay::splay(Node *u) {
  while (u!=root) {
    if (u->p==root) {
      if (u==u->p->l) rotate_right(u->p);
      else rotate_left(u->p);
    }
    else {  // u->p->p exists
      assert(u->p->p!=NULL);
      if (u==u->p->l) {
	if (u->p==u->p->p->l) {
	  rotate_right(u->p->p);
	  rotate_right(u->p);
	}
	else {
	  rotate_right(u->p);
	  rotate_left(u->p);
	}
      }
      else {
	if (u->p==u->p->p->r) {
	  rotate_left(u->p->p);
	  rotate_left(u->p);
	}
	else {
	  rotate_left(u->p);
	  rotate_right(u->p);
	}
      }
    }
  }
}

Node *Splay::access(val x) {
  Node *u = root, *u0 = NULL;
  while (u!=NULL && u->x!=x) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  if (u==NULL) splay(u0);  // ok when u0==NULL as root will be NULL too
  else splay(u);
  return u;
}

Node *Splay::access_max() {
  Node *u = root;
  if (u!=NULL) {
    while (u->r!=NULL) u = u->r;
    splay(u);
  }
  return u;
}

void Splay::join(Node *u) {
  if (root==NULL) root = u;
  else {
    access_max();
    assert(root->r==NULL);
    root->r = u;
    if (root->r!=NULL) root->r->p = root;
  }
}

pair<Node*,Node*> Splay::split(val x) {
  Node *L = NULL, *R = NULL;
  if (root!=NULL) {
    access(x);
    if (root->x<=x) {
      L = root;
      R = root->r;
      L->r = NULL;
      if (R!=NULL) R->p = NULL;
    }
    else {
      L = root->l;
      R = root;
      R->l = NULL;
      if (L!=NULL) L->p = NULL;
    }
    root = NULL;  // neutralize current tree
  }
  return make_pair(L,R);
}

// splay spirit method: insertion using split
void Splay::insert(val x) {
  pair<Node*,Node*> LR = split(x);
  root = new Node(x,NULL,LR.first,LR.second);
}

// splay spirit method: deletion using join
void Splay::erase(val x) {
  Node *u = access(x);
  assert(u!=NULL);
  Node *r = u->r;
  if (r!=NULL) r->p = NULL;
  root = u->l;
  if (root!=NULL) root->p = NULL;
  delete u;
  join(r);
}

Node *Splay::min(Node *u=NULL) const {
  if (u==NULL) u = root;
  if (u!=NULL)
    while (u->l!=NULL)
      u = u->l;
  return u;
}

Node *Splay::succ(Node *u) {
  if (u->r!=NULL) return min(u->r);
  Node *u0 = u->p;
  while (u0!=NULL && u==u0->r) {
    u = u0;
    u0 = u->p;
  }
  return u0;
}

void Splay::clear(Node *u) {
  if (u!=NULL) {
    clear(u->l);
    clear(u->r);
    delete u;
  }
}

void Splay::clear() {
  clear(root);
  root = NULL;
}
/* ===== END Splay ===== */


void traversal(Splay &T) {
  Node *u = T.min();
  while (u!=NULL) {
    cout << u->x << ' ';
    u = T.succ(u);
  }
  cout << endl;
}

void dfs_draw(Splay &T, Node *u, string path) {
  if (u==NULL) cout << path << " [shape=point];" << endl;
  else {
    cout << path << " [label=\"" << u->x << "\"];" << endl;
    cout << path << " -> " << path+"0" << ";" << endl;
    cout << path << " -> " << path+"1" << ";" << endl;;
    dfs_draw(T,u->l,path+"0");
    dfs_draw(T,u->r,path+"1");
  }
}

void draw(Splay &T) {
  cout << "digraph G {" << endl;
  dfs_draw(T,T.root,"U");
  cout << "}" << endl;
}

int main() {
  srand(42);
  Splay T;
  int n = 5000000, m = 5000;
  for (int i=0; i<n; ++i) {
    int c = rand()%3, x = rand()%m;
    if (c>0) T.insert(x);
    else if (T.access(x)!=NULL) T.erase(x);
  }
  //draw(T);
  //traversal(T);
  return 0;
}
