#include <iostream>
#include <vector>
#include <queue>
#define MAX 10001
using namespace std;

int stk[MAX];
int croit[MAX];
int decroit[MAX];
int M[MAX];

void calc_croit(int n){
  int L = 1;
  M[1] = 0;
  croit[0] = 1;

  for(int i = 1; i < n; ++i){
    //on cherche max(l) tq l <= L et stk[M[l]] < stk[i]
    int dichop = L;
    int dichom = 0;
    int mil;
    while(dichop != dichom){
      mil = (dichop + dichom) / 2;
      if(stk[M[mil+1]] < stk[i]){
	dichom = mil+1;
      }
      else dichop = mil;
    }
    //cout << "dichop " << dichop << endl;
    if(dichop == L || stk[i] < stk[M[dichop+1]]){
      M[dichop+1] = i;
      L = max(L, dichop + 1);
    }
    croit[i] = L;
  }
}

void calc_decroit(int n){
  int L = 1;
  M[1] = 0;
  decroit[n-1] = 1;

  for(int i = 1; i < n; ++i){
    //on cherche max(l) tq l <= L et stk[M[l]] < stk[i]
    int dichop = L;
    int dichom = 0;
    int mil;
    while(dichop != dichom){
      mil = (dichop + dichom) / 2;
      if(stk[n-1 - M[mil+1]] < stk[n-1-i]){
	dichom = mil+1;
      }
      else dichop = mil;
    }   
    if(dichop == L || stk[n-1-i] < stk[n-1-M[dichop+1]]){
      M[dichop+1] = i;
      L = max(L, dichop + 1);
    }
    decroit[n-1-i] = L;
  }
}

int main(void){
  int n;
  while(cin >> n){
    for(int i = 0; i < n; ++i){
      cin >> stk[i];
    }
    calc_croit(n);    
    calc_decroit(n);
    int m2 = 0;
    for(int i = 0; i < n; ++i){
      m2 = max(m2, 2*(min(croit[i], decroit[i])) - 1);
    }
    cout << m2 << endl;
  }
}
