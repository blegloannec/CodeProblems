#include <iostream>
#include <vector>
using namespace std;

struct rocket {
  int a,v;
  rocket(int alt, int val) : a(alt),v(val) {};
};

vector<rocket> t;

int main() {
  int n,m,l,c,vmax;
  t.clear();
  c = 1;
  cin >> n;
  while (true) {
    while (n>=0) {
      t.push_back(rocket(n,1));
      cin >> n;
    }
    l = t.size();
    vmax = 1;
    for (int i=l-2; i>=0; i--) {
      m = 1;
      for (int j=i+1; j<l; j++) 
	if (t[j].a <= t[i].a) 
	  m = max(m,t[j].v+1);
      t[i].v = m;
      vmax = max(vmax,m);
    }
    
    cout << "Test #" << c << ":\n";
    cout << "  maximum possible interceptions: " << vmax << '\n';
    
    cin >> n;
    if (n<0) return 0;
    cout << '\n';
    t.clear();
    ++c;
  }    
  
  return 0;  
}
