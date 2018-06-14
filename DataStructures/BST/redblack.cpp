#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

/* ===== RedBlack BST ====== */
/* !! Use T.NIL instead of NULL !! */
typedef int val;

struct Node {
  val x;
  bool red;
  Node *p,*l,*r;

  Node(val x, bool red, Node *p, Node *l, Node *r) : x(x),red(red),p(p),l(l),r(r) {}
};

struct RedBlack {
  Node *root;
  Node *NIL;  // convenient sentinel for NIL->red and erase_fixup(NIL)
  
  RedBlack() {
    NIL = new Node(0,false,NULL,NULL,NULL);
    root = NIL;
  }
  
  ~RedBlack() {
    clear();
    delete NIL;
  }
  
  void rotate_left(Node *u);
  void rotate_right(Node *u);
  void insert_fixup(Node *u);
  Node *find(val x) const;
  void insert(val x);
  Node *min(Node *u) const;
  Node *succ(Node *u) const;
  Node *_erase_in_line(Node *u);
  void erase_fixup(Node *u);
  void erase(Node *u);
  void erase(val x);
  void clear(Node *u);
  void clear();
};

void RedBlack::rotate_left(Node *u) {
  Node *v = u->r;
  u->r = v->l; if (u->r!=NIL) u->r->p = u;
  v->l = u; v->p = u->p; u->p = v;
  if (root==u) root = v;
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

void RedBlack::rotate_right(Node *u) {
  Node *v = u->l;
  u->l = v->r; if (u->l!=NIL) u->l->p = u;
  v->r = u; v->p = u->p; u->p = v;
  if (root==u) root = v;
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
}

void RedBlack::insert_fixup(Node *u) {
  while (u->p->red) {
    if (u->p==u->p->p->l) {  // u is on the left side of its grandparent
      Node *v = u->p->p->r;  // u's uncle
      if (v->red) {
	u->p->red = false;
	v->red = false;
	u = u->p->p;
	u->red = true;
      }
      else {
	if (u==u->p->r) {
	  u = u->p;
	  rotate_left(u);
	}
	u->p->red = false;
	u->p->p->red = true;
	rotate_right(u->p->p);
      }
    }
    else {  // symmetric
      Node *v = u->p->p->l;
      if (v->red) {
	u->p->red = false;
	v->red = false;
	u = u->p->p;
	u->red = true;
      }
      else {
	if (u==u->p->l) {
	  u = u->p;
	  rotate_right(u);
	}
	u->p->red = false;
	u->p->p->red = true;
	rotate_left(u->p->p);
      }
    }
  }
  root->red = false;
}

Node *RedBlack::find(val x) const {
  Node *u = root;
  while (u!=NIL && u->x!=x)
    u = x<=u->x ? u->l : u->r;
  return u;
}

void RedBlack::insert(val x) {
  Node *u0 = NIL, *u = root;
  while (u!=NIL) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  u = new Node(x,true,u0,NIL,NIL);
  if (u0==NIL) root = u;
  else if (x<=u0->x) u0->l = u;
  else u0->r = u;
  insert_fixup(u);
}

Node *RedBlack::min(Node *u=NULL) const {
  if (u==NULL) u = root;
  if (u!=NIL)
    while (u->l!=NIL)
      u = u->l;
  return u;
}

Node *RedBlack::succ(Node *u) const {
  if (u->r!=NIL) return min(u->r);
  Node *u0 = u->p;
  while (u0!=NIL && u==u0->r) {
    u = u0;
    u0 = u->p;
  }
  return u0;
}

// deletes a node u having at most one child
Node *RedBlack::_erase_in_line(Node *u) {
  assert(u->l==NIL || u->r==NIL);
  Node *v = NIL;
  if (u->l!=NIL) v= u->l;
  else if (u->r!=NIL) v = u->r;
  if (u==root) root = v;
  else if (u->p->l==u) u->p->l = v;
  else u->p->r = v;
  /* NB: we do the next line unconditionally, even when v = NIL,
     so that v->p points to the right parent when calling erase_fixup(v) */
  v->p = u->p;
  delete u;
  return v;
}

void RedBlack::erase_fixup(Node *u) {
  while (u!=root && !u->red) {
    if (u==u->p->l) {
      Node *v = u->p->r;
      if (v->red) {
	v->red = false;
	u->p->red = true;
	rotate_left(u->p);
	v = u->p->r;
      }
      if (!v->l->red && !v->r->red) {
	v->red = true;
	u = u->p;
      }
      else {
	if (!v->r->red) {
	  v->l->red = false;
	  v->red = true;
	  rotate_right(v);
	  v = u->p->r;
	}
	v->red = u->p->red;
	u->p->red = false;
	v->r->red = false;
	rotate_left(u->p);
	u = root;
      }
    }
    else {
      Node *v = u->p->l;
      if (v->red) {
	v->red = false;
	u->p->red = true;
	rotate_right(u->p);
	v = u->p->l;
      }
      if (!v->l->red && !v->r->red) {
	v->red = true;
	u = u->p;
      }
      else {
	if (!v->l->red) {
	  v->r->red = false;
	  v->red = true;
	  rotate_left(v);
	  v = u->p->l;
	}
	v->red = u->p->red;
	u->p->red = false;
	v->l->red = false;
	rotate_right(u->p);
	u = root;
      }
    }
  }
  u->red = false;
}

void RedBlack::erase(Node *u) {
  Node *w;
  bool black_erased;
  if (u->l==NIL || u->r==NIL) {
    black_erased = !u->red;
    w = _erase_in_line(u);
  }
  else {
    Node *v = min(u->r);  // we could as well use succ(u)
    u->x = v->x;
    black_erased = !v->red;
    w = _erase_in_line(v);  // v has no left child
  }
  if (black_erased) erase_fixup(w);
}

void RedBlack::erase(val x) {
  Node *u = find(x);
  assert(u!=NIL);
  erase(u);
}

void RedBlack::clear(Node *u) {
  if (u!=NIL) {
    clear(u->l);
    clear(u->r);
    delete u;
  }
}

void RedBlack::clear() {
  clear(root);
  root = NIL;
}
/* ===== END RedBlack ===== */


void traversal(RedBlack &T) {
  Node *u = T.min();
  while (u!=T.NIL) {
    cout << u->x << ' ';
    u = T.succ(u);
  }
  cout << endl;
}

void dfs_draw(RedBlack &T, Node *u, string path) {
  if (u==T.NIL) cout << path << " [shape=point];" << endl;
  else {
    string col = u->red ? "red" : "black";
    cout << path << " [label=\"" << u->x << "\",color=" << col<< "];" << endl;
    cout << path << " -> " << path+"0" << ";" << endl;
    cout << path << " -> " << path+"1" << ";" << endl;;
    dfs_draw(T,u->l,path+"0");
    dfs_draw(T,u->r,path+"1");
  }
}

void draw(RedBlack &T) {
  cout << "digraph G {" << endl;
  dfs_draw(T,T.root,"U");
  cout << "}" << endl;
}

int main() {
  srand(42);
  RedBlack T;
  int n = 5000000, m = 5000;
  for (int i=0; i<n; ++i) {
    int c = rand()%3, x = rand()%m;
    if (c>0) T.insert(x);
    else if (T.find(x)!=T.NIL) T.erase(x);
  }
  //traversal(T);
  //draw(T);
  return 0;
}
