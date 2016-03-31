#include <iostream>
using namespace std;

int rule[10];
int dish[2][42];

int main() {
  int n,r;
  cin >> n;

  while (n-->0) {
    for (int i=0; i<=9; i++) cin >> rule[i];
    for (int i=0; i<=41; i++) dish[1][i] = 0;
    dish[1][20] = 1;
    cout << "                   .                    \n";
    for (int j=0; j<49; j++) {
      for (int i=1; i<=40; i++) {
	r = dish[j%2][i] = rule[dish[1-j%2][i-1]+dish[1-j%2][i]+dish[1-j%2][i+1]];
	if (r==0) cout << ' ';
	else if (r==1) cout << '.';
	else if (r==2) cout << 'x';
	else cout << 'W';	 
      }
      cout << '\n';
    }
    if (n>0) cout << '\n';
  }
  
  return 0;
}
