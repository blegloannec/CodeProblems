#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXL 52
#define MAX 26

typedef pair<int,int> couple;

struct lextree {
  char c;
  list<lextree> l;
  lextree(char c) : c(c) {l.clear();};
  lextree() {l.clear();};
};


char buff[MAXL];
lextree t;
bool g[MAX][MAX];
int cpt;
vector<couple> post;
bool present[MAX];
bool visited[MAX];

void insert() {
  int i = 0;
  lextree *p = &t;
  while ((buff[i]>='A')&&(buff[i]<='Z')) {
    if (((p->l).empty())||((p->l).back().c!=buff[i]))
      (p->l).push_back(lextree(buff[i]));
    p = &((p->l).back());
    ++i;
  }
}


int c2i(char c) {
  return (int)c-(int)'A';
}

char i2c(int i) {
  return (char)(i+(int)'A');
}

void init_graph() {
  for (int i=0; i<MAX; i++) {
    present[i] = visited[i] = false;
    for (int j=0; j<MAX; j++) 
      g[i][j] = false;
  }
}

void order_graph(lextree &t) {
  list<lextree>::iterator it;
  int c0,l;
  l = t.l.size();
  if (l>0) {
    it = t.l.begin();
    order_graph(*it);
    c0 = c2i(it->c);
    present[c0] = true;
    if (l>1) {
      for (it=++it; it!=t.l.end(); it++) {
	g[c0][c2i(it->c)] = true;
	c0 = c2i(it->c);
	present[c0] = true;
	order_graph(*it);
      }
    }
  }
}

void explore(int i) {
  visited[i] = true; // Pour eviter les boucles, inutile si l'entree est propre
  for (int j=0; j<MAX; j++) {
    if ((g[i][j])&&(post[j].second<0)&&(!visited[j]))
      explore(j);
  }
  post[i].second = cpt++;
}


void DFS() {
  cpt = 0;
  post.clear();
  for (int i=0; i<MAX; i++)
    post.push_back(couple(i,-1));
  for (int i=0; i<MAX; i++)
    if (present[i]&&(post[i].second<0))
      explore(i);
}

/*
void affiche() {
  for (int i=0; i<MAX; i++) {
    for (int j=0; j<MAX; j++)
      cout << (int)g[i][j];
    cout << endl;
  }
  cout << endl;
}
*/

bool sup(couple a, couple b) {
  return a.second>b.second;
}


int main() {
  vector<couple>::iterator it;

  while (cin >> buff) {
    if (buff[0]=='#') break;
    insert();
  }
  init_graph();
  order_graph(t);
  //affiche();
  DFS();
  sort(post.begin(),post.end(),sup);
  for (it=post.begin(); it!=post.end(); it++)
    if (present[it->first]) 
      cout << i2c(it->first);
  cout << '\n';

  return 0;
}
