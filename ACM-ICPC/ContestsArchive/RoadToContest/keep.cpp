#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 2000001

struct job {
  int dur,fin;
  job(int d, int f) : dur(d), fin(f) {};
};

/* m[i] est le max de taches que l'on peut safisfaire 
   parmi les i premieres */
//int m[MAX];

typedef vector<job> vect;

vect t;

bool ordre(job j1, job j2) {
  if (j1.fin == j2.fin)
    return  j1.dur > j2.dur;
  else return j1.fin < j2.fin;
  
}

int f(int i) {
  if 
}

int main() {
  int cas,n,a,b,res,curr;
  bool debut = true;
  vect::iterator it;
  cin >> cas;
  while (cas-->0) {
    if (debut) debut=false;
    else cout << '\n';
    cin >> n;
    for (int i=0; i<n; ++i) {
      cin >> a >> b;
      t.push_back(job(a,b));
    }
    sort(t.begin(),t.end(),ordre);
    /*
    curr = 0;
    res = 0;
    for (it=t.begin(); it!=t.end(); ++it) {
      if (curr+it->dur < it->fin) {
	++res;
	curr += it->dur;
      }
    }
    */
    
    curr = t[];
    res = 0;
    for (it=t.begin(); it!=t.end(); ++it) {
      if (curr+it->dur < it->fin) {
	++res;
	curr -= it->dur;
      }
    }
    
    //for (int i=0; i<MAX; ++i) 
    //m[i] = -1;
    //m[0] = 0;
    
    cout << res << '\n';
    t.clear();
  }
}
