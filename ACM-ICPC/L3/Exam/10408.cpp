#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> couple;

vector<couple> fracs;

bool comp(couple a, couple b) {
  return (double)a.first/(double)a.second<(double)b.first/(double)b.second;
}

int pgcd(int a, int b) {
  if (b==0) return a;
  return pgcd(b, a%b);
}

void generate(int k) {
  fracs.clear();
  for (int d=2; d<=k; d++) {
    for (int n=1; n<d; n++) {
      if (pgcd(d,n)==1) fracs.push_back(couple(n,d));
    }
  }
  fracs.push_back(couple(1,1));
  sort(fracs.begin(),fracs.end(),comp);
}

int main() {
  int n,k; 
  
  while (cin >> n >> k) {
    generate(n);
    cout << fracs[k-1].first << '/' << fracs[k-1].second << '\n';
  }

  return 0;
}
