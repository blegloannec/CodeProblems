// Kruskall (avec Tarjan) pour Is There A Second Way Left ?

#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

#define INTMAX 50000000

struct edge {
  int ext1;
  int ext2;
  int weight;
  edge(int e1, int e2, int w) : ext1(e1),ext2(e2),weight(w) {};
};

bool inf(edge a, edge b) {
  return (a.weight < b.weight);
}

void affiche(vector<edge> *t) {
  vector<edge>::iterator it;
  cout << "[ ";
  for (it = t->begin(); it != t->end(); it++) {
    cout << '(' << it->ext1 << ',' << it->ext2 << ',' << it->weight << ") ";
  }
  cout << "]" << endl;
}

int find(int e, vector<int> *t) {
  int p = (*t)[e];
  if (p==0) return e;
  else {
    int root = find(p,t);
    (*t)[e] = root;    
    return root;
  }
}

void fusion(int a, int b, vector<int> *t) {
  int roota = find(a,t);
  int rootb = find(b,t);
  (*t)[rootb] = roota;
}

int main(void) {
  int nbt,cas;
  cin >> nbt;
  cas = 0;
  
  while (++cas <= nbt) {
    vector<edge> t;
    t.clear();
    int N, M;
    cin >> N >> M;
    
    while (M-- > 0) {
      int a,b,c;
      cin >> a >> b >> c;
      t.push_back(edge(a,b,c));
    }

    // Ici le code
    //    affiche(&t);
    sort(t.begin(),t.end(),inf);
    //    affiche(&t);

    vector<int> tarj;
    vector<edge>::iterator it;
    list<vector<edge>::iterator> used_edges;
    used_edges.clear();
    tarj.assign(N+1,0);
   
    it = t.begin();
    int c = N-1;
    int res = 0;
    while ((c>0)&&(it!=t.end())) {
      edge e = *it;
      if (find(e.ext1,&tarj) != find(e.ext2,&tarj)) {
	used_edges.push_front(it);
	res += e.weight;
	--c;
	fusion(e.ext1,e.ext2,&tarj);
      }
      ++it;
    }
    
    if (c>0) {
      cout << "Case #" << cas << " : No way\n";
      continue;
    }

    res = INTMAX;
    
    while (!(used_edges.empty())) {
      it = t.begin();     
      tarj.assign(N+1,0);
      int c = N-1;
      int pres = 0;
      while ((c>0)&&(it!=t.end())) {
	if (it != used_edges.front()) {
	  edge e = *it;
	  if (find(e.ext1,&tarj) != find(e.ext2,&tarj)) {
	    pres += e.weight;
	    --c;
	    fusion(e.ext1,e.ext2,&tarj);
	  }
	}
	++it;
      }
      if (c==0) res = min(res,pres);
      used_edges.pop_front();
    }

    if (res==INTMAX) cout << "Case #" << cas << " : No second way\n";
    else cout << "Case #" << cas << " : " << res << '\n';
    
  }

  return 0;
}
