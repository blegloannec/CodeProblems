// Algo en n*log(n)

#include <iostream>
#include <map>
using namespace std;

int main() {
  map<int,int> m;
  pair<map<int,int>::iterator,bool> res;
  map<int,int>::iterator it,it2;
  int n,c;

  m.clear();
  c = 1;
  cin >> n;
  while (true) {
    while (n>=0) {
      res = m.insert(pair<int,int>(n,1));
      if (res.second) {// nouvelle altitude
	it2 = res.first;
	it = it2++;
	if (it2!=m.end()) it->second = it2->second + 1;
      }
      else { // altitude existante
	it = res.first;
	(it->second)++;
      }
      if (it!=m.begin()) {
	it2 = it--;
	if (it->second <= it2->second) m.erase(it);
      }
      cin >> n;
    }

    cout << "Test #" << c << ":\n";
    cout << "  maximum possible interceptions: " << m.begin()->second << '\n';

    cin >> n;
    if (n<0) return 0;
    cout << '\n';
    m.clear();
    ++c;
  }    
  
  return 0;  
}
 
