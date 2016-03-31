// Accessibilité orientée toutes paires
#include <iostream>
#include <map>

using namespace std;

#define MAX 500

string inv_tbl[MAX];
map<string,int> tbl;
map<string,int>::iterator it,it2;

char t[MAX][MAX]; // tableau du graphe
int size; // taille du tableau : size x size
void clear2() {
  for (int i=0; i<size; ++i) 
    for (int j=0; j<size; ++j)
      t[i][j] = 0;
}

int dist[MAX][MAX]; // distances, cf initialisation
#define INTMAX 1000000000

void FloydWarshall() {
  // initialisation
  for (int i=0; i<size; ++i)
    for (int j=0; j<size; ++j) // WARNING. cas i=j
      if (t[i][j]>0) {
	dist[i][j] = t[i][j];
      }
      else {
	dist[i][j] = INTMAX;
      }
  // prog. dyn.
  for (int k=0; k<size; ++k)
    // dist_k[i][j] = plus courte distance de i a j en utilisant les k premiers sommets
    for (int i=0; i<size; ++i)
      for (int j=0; j<size; ++j) {
	int d = dist[i][k]+dist[k][j];
	if (dist[i][j]>d) {
	  dist[i][j] = d;
	}
      }
}

string s;

int get_s() {
  it = tbl.find(s);
  if (it == tbl.end()) {
    tbl.insert(pair<string,int>(s,size));
    inv_tbl[size] = s;
    ++size;
    return (size-1);
  }
  else return it->second;
}

int main() {
  int NC, NE, NM, pred_num, tmp, tmp2, cas;
  cas = 1;
  while (cin >> NC) {
    if (NC == 0) return 0;
    size = 0;
    tbl.clear();
    size = MAX;
    clear2();
    size = 0;
    for (int i=0; i<NC; ++i) {
      cin >> NE;
      for (int j=0; j<NE; ++j) {
	cin >> s;
	tmp = get_s();
	if (j==0) pred_num = tmp;
	else {
	  t[pred_num][tmp] = 1;
	  pred_num = tmp;
	}
      }
    }
    cin >> NM;
    for (int i=0; i<NM; ++i) {
      cin >> s;
      tmp = get_s();
      cin >> s;
      tmp2 = get_s();
      t[tmp][tmp2] = 1;
    }
    FloydWarshall();
    string sa,sb,sc,sd;
    int res = 0;
    for (int i=0; i<size; ++i)
      for (int j=i+1; j<size; ++j)
	if (dist[i][j]>MAX && dist[j][i]>MAX) {
	  if (res == 0) {
	    sa = inv_tbl[i];
	    sb = inv_tbl[j];
	  }
	  if (res == 1) {
	    sc = inv_tbl[i];
	    sd = inv_tbl[j];
	  }
	  ++res;
	}
    if (res==0)
      cout << "Case " << cas << ", no concurrent events.\n";
    else 
      cout << "Case " << cas << ", " << res << " concurrent events:\n";
    if (res==1)
      cout << "(" << sa << "," << sb << ") \n";
    else if (res>1)
      cout << "(" << sa << ',' << sb << ") (" << sc << ',' << sd << ") \n";
    ++cas;
  }
  return 0;
}
