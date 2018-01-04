#include <iostream>
using namespace std;

#define MAX 101

int s[MAX];
bool t[20001];
int N;

bool verif() {
  int S;
  if (s[1]<1) return false;
  for (int i=1; i<N; i++)
    if (s[i]>=s[i+1]) return false;
  for (int i=1; i<=N; i++)
    for (int j=i; j<=N; j++){
      S = s[i]+s[j]; 
      if (t[S]) return false;
      t[S] = true;
    }
  return true;
}


int main() {
  int v,cas;
  cas = 1;
  while (cin >> N) {
    for (int i=1; i<=N; i++) {
      cin >> v;
      s[i] = v;
    }
    for (int i=0; i<=20000; i++) t[i]=false;
    if (verif()) cout << "Case #" << cas++ << ": It is a B2-Sequence.\n\n";
    else  cout << "Case #" << cas++ << ": It is not a B2-Sequence.\n\n";	
  } 

  return 0;
}
