//Bon on n'a pas réussi à faire plus court mais ce doit être possible
#include <iostream>
#define MAX 20001
using namespace std;

typedef long long ent;

ent p(ent a, ent b){
  if(a <= 1 or b <= 1) return 0;
  return p(a-1, b) + ((a-1) * (b*(b-1)/2));
}

int main(void){
  ent a,b;
  int n = 0;
  cin >> a >> b;
  while (a != 0 || b != 0){
    n++;
    cout << "Case " << n << ": " << p(a,b) << endl;
    cin >> a >> b;
  }
  return 0;
}
