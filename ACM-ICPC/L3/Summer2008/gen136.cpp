#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ent;

ent puiss(ent x, ent p) {
  return (ent)floor(pow((double)x,(double)p));
}

int main() {
  vector<ent> t;
  ent res;

  for (int i=0; i<=30; i++) 
    for (int j=0; j<=30; j++)
      for (int k=0; k<=30; k++) {
	res = puiss(2,i)*puiss(3,j)*puiss(5,k);
	if (res>0) t.push_back(res);
      }
  
  sort(t.begin(),t.end());
  cout << t[1499] << endl;

  return 0;
}
