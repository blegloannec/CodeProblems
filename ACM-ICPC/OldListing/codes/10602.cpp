#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define MAX 101

string Stk[MAX];
string Mot_de_ref;

int plus_long_prefixe(const string &a, const string &b){
  int lga = (int) a.size();
  int lgb = (int) b.size();
  bool diff = false;
  int res = 0;
  while(!diff && res < min(lga, lgb)){
    if(a[res] == b[res])
      res++;
    else
      diff = true;
  }
  return res;
}

bool mon_superieur(const string &a, const string &b){
  int resa = plus_long_prefixe(a, Mot_de_ref);
  int resb = plus_long_prefixe(b, Mot_de_ref);
  if(resa != resb) return resa > resb;
  int lga = (int) a.size();
  int lgb = (int) b.size();
  bool diff = false;
  int res = resa;
  while(!diff && res < min(lga, lgb)){
    if(a[res] == b[res])
      res++;
    else{
      diff = true; //ne sert à rien.
      return (a[res] > b[res]);
    }
  }
  return lga > lgb; //Doit être stricte sinon seg faulte
}

int main(void){
  int n,a;
  cin >> n;
  for(int i = 0; i < n; ++i){
    cin >> a;
    cin.ignore();
    getline(cin, Mot_de_ref);
    for(int j = 0; j < a-1; ++j){
      getline(cin, Stk[j]);    
    }
    if(a > 2) sort(Stk, Stk + a - 1, mon_superieur);
    int res = (int) Mot_de_ref.size();
    
    for(int j = 0; j < a-1; j++){
      res += 
	(int) Stk[j].size();
      if(j == 0)
	res -= plus_long_prefixe(Stk[0], Mot_de_ref);
      if(j > 0)
	res -= plus_long_prefixe(Stk[j], Stk[j-1]);
    }
    cout << res << endl;
    cout << Mot_de_ref << endl;
    for(int j = 0; j < a-1; j++){
      cout << Stk[j] << endl;
    }
  }
  return 0;
}
