#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 1000001

typedef vector<int> liste;
int size;
vector<liste> t; // Table des listes de successeurs


int main() {
  bool debut = true;
  int nb,a,b,res;
  liste::iterator it;

  while (cin >> size >> nb) {
    t.reserve(size);
    res = 0;
    if (debut) debut = false;
    else cout << '\n';
    if ((size<=1)||(nb==0)) {
      cout << "0\n";
      continue;
    }
    cin >> a >> b;
    --a;
    --b;
    t[a].push_back(b);
    t[b].push_back(a);
    for (int i=1; i<nb; ++i) {
      cin >> a >> b;
      --a;
      --b;
      //if (find(t[a].begin(),t[a].end(),b)==t[a].end()) {
      //for (it=t[a].begin(); it!=t[a].end(); ++it) {
	  //cout << *it << endl;
      // t[*it].push_back(b);
      //  t[b].push_back(*it);
      //}
	t[a].push_back(b);
	cout << t[b].size() << endl;
	for (int i=0; i<t[b].size(); ++i) 
	  cout << t[b][i] << ' ';
	cout << endl;
	t[b].push_back(a);
	//}
	//else ++res;
    }
    //cout << res << '\n';
    //for (int i=0; i<size; ++i) t[i].clear();
    t.clear();
  }
}
