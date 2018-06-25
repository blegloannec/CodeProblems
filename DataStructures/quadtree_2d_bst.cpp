#include <cstdlib>
#include <vector>
using namespace std;

// See also HackerRank / PE+ 127


// ===== QUADTREE 2D BST =====
typedef pair<int,int> point;

void shuffle(vector<point> &A) {
  for (int i=(int)A.size()-1; i>0; --i)
    swap(A[i],A[rand()%i]);
}

struct quadnode {
  int x,y,mx,Mx,my,My,cnt,mult;
  quadnode *sw,*se,*ne,*nw;

  quadnode(int x, int y) : x(x), y(y), mx(x), Mx(x), my(y), My(y), cnt(1), mult(1), sw(NULL), se(NULL), ne(NULL), nw(NULL) {}
};

struct QuadTree {
  quadnode *root;

  QuadTree() {}
  
  void init(vector<point> &P) {
    shuffle(P);
    for (auto it=P.begin(); it!=P.end(); ++it)
      insert(it->first,it->second);
  }

  void insert(int x, int y);
  int count(quadnode *t, int x, int y);
  int count(int x, int y) {
    return count(root,x,y);
  }
};

void QuadTree::insert(int x, int y) {
  quadnode *t = root, *t0 = NULL;
  while (t!=NULL) {
    t0 = t;
    ++(t->cnt);
    if (x==t->x && y==t->y) {
      ++(t->mult);
      return;
    }
    t->mx = min(t->mx,x);
    t->my = min(t->my,y);
    t->Mx = max(t->Mx,x);
    t->My = max(t->My,y);
    if (x<=t->x) {
      if (y<=t->y) t = t->sw;
      else t = t->nw;
    }
    else {
      if (y<=t->y) t = t->se;
      else t = t->ne;
    }
  }
  t = new quadnode(x,y);
  if (t0==NULL) root = t;
  else if (x<=t0->x) {
    if (y<=t0->y) t0->sw = t;
    else t0->nw = t;
  }
  else {
    if (y<=t0->y) t0->se = t;
    else t0->ne = t;
  }
}

int QuadTree::count(quadnode *t, int x, int y) {
  if (t==NULL) return 0;
  if (x<t->mx && y<t->my) return 0;
  if (x>=t->Mx && y>=t->My) return t->cnt;
  int res = count(t->sw,x,y);
  if (x>=t->x && y>=t->y) res += t->mult;
  if (x>t->x) res += count(t->se,x,y);
  if (y>t->y) res += count(t->nw,x,y);
  if (x>t->x && y>t->y) res += count(t->ne,x,y);
  return res;
}
// ===== =====


int main() {
  srand(42);
  return 0;
}
