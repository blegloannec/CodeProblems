#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

/* ===== AVL BST ====== */
typedef int val;

struct Node {
  val x;
  Node *p,*l,*r;
  int h;

  Node(val x, Node *p=NULL, Node *l=NULL, Node *r=NULL) : x(x),p(p),l(l),r(r) {
    h = 1+max((l==NULL?0:l->h),(r==NULL?0:r->h));
  }
};

struct AVL {
  Node *root;

  AVL() {
    root = NULL;
  }

  int height(Node *u) const;
  void refresh_height(Node *u);
  int bf(Node *u) const;
  void rotate_left(Node *u);
  void rotate_right(Node *u);
  bool balance_node(Node *u);
  void upward_balance(Node *u);
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

int AVL::height(Node *u) const {
  return u==NULL ? 0 : u->h;
}

void AVL::refresh_height(Node *u) {
  //assert(u!=NULL);
  u->h = 1+max(height(u->l),height(u->r));
}

// balance factor
int AVL::bf(Node *u) const {
  return height(u->r)-height(u->l);
}

void AVL::rotate_left(Node *u) {
  Node *v = u->r;
  //assert(v!=NULL);
  u->r = v->l; if (u->r!=NULL) u->r->p = u;
  v->l = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
  refresh_height(u);
  refresh_height(v);
}

void AVL::rotate_right(Node *u) {
  Node *v = u->l;
  //assert(v!=NULL);
  u->l = v->r; if (u->l!=NULL) u->l->p = u;
  v->r = u; v->p = u->p; u->p = v;
  if (root==u) root = v;  // we could as well test v->p==NULL
  else if (v->p->l==u) v->p->l = v;
  else v->p->r = v;
  refresh_height(u);
  refresh_height(v);
}

bool AVL::balance_node(Node *u) {
  bool mod = false;
  if (bf(u)>1) {
    //assert(bf(u)==2);
    /* in a post-insertion situation, bf(u->r) cannot be 0
       yet this can happen post-deletion and is solved by
       a single rotation as in the case bf(u->r) = 1 */
    if (bf(u->r)>=0) rotate_left(u);
    else {
      rotate_right(u->r);
      rotate_left(u);
    }
    mod = true;
  }
  else if (bf(u)<-1) {
    //assert(bf(u)==-2);
    if (bf(u->l)<=0) rotate_right(u);
    else {
      rotate_left(u->l);
      rotate_right(u);
    }
    mod = true;
  }
  return mod;
}

void AVL::upward_balance(Node *u) {
  /* in a post-insertion situation, there cannot be more than one
     node to re-balance by a single or double rotation
     yet in a post-deletion, several balancings might be necessary */
  while (u!=NULL) {
    balance_node(u);
    refresh_height(u);
    //assert(abs(bf(u))<2);
    u = u->p;
  }
}

Node *AVL::find(val x) const {
  Node *u = root;
  while (u!=NULL && u->x!=x)
    u = x<=u->x ? u->l : u->r;
  return u;
}

void AVL::insert(val x) {
  Node *u0 = NULL, *u = root;
  while (u!=NULL) {
    u0 = u;
    u = x<=u->x ? u->l : u->r;
  }
  if (u0==NULL) root = new Node(x);
  else if (x<=u0->x) u0->l = new Node(x,u0);
  else u0->r = new Node(x,u0);
  upward_balance(u0);
}

Node *AVL::min(Node *u=NULL) const {
  if (u==NULL) u = root;
  if (u!=NULL)
    while (u->l!=NULL)
      u = u->l;
  return u;
}

Node *AVL::succ(Node *u) const {
  if (u->r!=NULL) return min(u->r);
  Node *u0 = u->p;
  while (u0!=NULL && u==u0->r) {
    u = u0;
    u0 = u->p;
  }
  return u0;
}

// deletes a node u having at most one child
void AVL::_erase_in_line(Node *u) {
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

void AVL::erase(Node *u) {
  if (u->l==NULL || u->r==NULL) {
    Node *u0 = u->p;
    _erase_in_line(u);
    upward_balance(u0);
  }
  else {
    Node *v = min(u->r);  // we could as well use succ(u)
    u->x = v->x;
    Node *v0 = v->p;
    _erase_in_line(v);  // v has no left child
    upward_balance(v0);
  }
}

void AVL::erase(val x) {
  Node *u = find(x);
  assert(u!=NULL);
  erase(u);
}

void AVL::clear(Node *u) {
  if (u!=NULL) {
    clear(u->l);
    clear(u->r);
    delete u;
  }
}

void AVL::clear() {
  clear(root);
  root = NULL;
}
/* ===== END AVL ===== */


void traversal(AVL &T) {
  Node *u = T.min();
  while (u!=NULL) {
    cout << u->x << ' ';
    u = T.succ(u);
  }
  cout << endl;
}

void dfs_draw(AVL &T, Node *u, string path) {
  if (u==NULL) cout << path << " [shape=point];" << endl;
  else {
    cout << path << " [label=\"" << u->x << " " << u->h << " " << T.bf(u) <<"\"];" << endl;
    cout << path << " -> " << path+"0" << ";" << endl;
    cout << path << " -> " << path+"1" << ";" << endl;;
    dfs_draw(T,u->l,path+"0");
    dfs_draw(T,u->r,path+"1");
  }
}

void draw(AVL &T) {
  cout << "digraph G {" << endl;
  dfs_draw(T,T.root,"U");
  cout << "}" << endl;
}

int main() {
  srand(42);
  AVL T;
  int n = 5000000, m = 5000;
  for (int i=0; i<n; ++i) {
    int c = rand()%3, x = rand()%m;
    if (c>0) T.insert(x);
    else if (T.find(x)!=NULL) T.erase(x);
  }
  return 0;
}
