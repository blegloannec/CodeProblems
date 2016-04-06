#include <iostream>
using namespace std;

typedef long long ent;

bool test(ent n) {
  //if (n%10!=0) return false;
  for (int i=9; i>0; --i) {
    n/=100;
    if (n%10!=i) return false;
  }
  return true;
}

const ent N = 1929394959697989990L;

int main() {
  for (ent i=10; i*i<N; i+=10)
    if (test(i*i)) {
	cout << i << endl;
	break;
      }
  return 0;
}
