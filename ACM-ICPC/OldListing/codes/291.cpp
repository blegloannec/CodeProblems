#include <iostream>
using namespace std;

#define N 9
#define MIN 1111111
#define MAX 5555555

int num[5][5] = {{-1, 0, 1,-1, 2},
		 { 0,-1, 3,-1, 4},
		 { 1, 3,-1, 5, 6},
		 {-1,-1, 5,-1, 7},
		 { 2, 4, 6, 7,-1}};

int t[N];
bool used[8];

int f(int j) {
  return num[t[j]-1][t[j+1]-1];
}

bool valide(int i) {
  int j,a;
  t[0] = 1;
  t[N-1] = 2;
  for (j=N-2; j>0; j--) {
    t[j] = i%10;
    if ((t[j]<=0)||(t[j]>5)) return false;
    i = i/10;
  }
  for (j=0; j<8; j++) used[j] = false;
  for (j=0; j<N-1; j++) {
    a = f(j);
    if (a<0) return false;
    if (used[a]) return false;
    used[a] = true;
  }
  return true;
}

int main() {
  int i;
  for (i=MIN; i<MAX; i++)
    if (valide(i)) cout << '1' << i << "2\n";
  return 0;
}
