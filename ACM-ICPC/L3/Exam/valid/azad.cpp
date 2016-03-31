#include <iostream>
#include <cmath>
using namespace std;

#define MAX 52

typedef long long ent;

ent mem[MAX];

ent traite(ent n) {
  double s = sqrt(n);
  ent res = 0;
  if (n%2 == 0) res += 2 + n/2;
  for (int i=3; i<=s; i+=2) 
    if (n%i == 0) res += i + n/i;
  return res;
}


int main() {
  int n;
  ent nb,s,s2;
  
  while (cin >> n) {
    if (n==0) return 0;
    //if (n==1) {
    //cout << "Given number is NOT prime! NO perfect number is available.\n";
    // continue;
    //}
    nb = (ent)pow((double)2,(double)n)-1;
    s2 = (ent)pow((double)2,(double)n);
    s = traite(nb);
    if (s+1+nb==s2) cout << "Perfect: " << nb*s2/2 << "!\n";
    else if (traite(n)==0) cout << "Given number is prime. But, NO perfect number is available.\n";
    else cout << "Given number is NOT prime! NO perfect number is available.\n";
  }

  return 0;
}
