#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

/* Fenwick Trees */
typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, ent v);

  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,-v);
}

/*
// version classique
ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}
*/

// variante range
ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}


int main() {
  return 0;
}
