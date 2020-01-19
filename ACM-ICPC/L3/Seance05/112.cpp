/*attention on demande de gerer les entiers negatifs
 probablement pas optimal surtout au niveau des entrees sorties (le
 plus dur et de tres loin)
*/

#include <iostream>

using namespace std;

#define M 20000
#define N 200000

int i=0,nbpar,ind,maxi;
bool h;
char chaine[M];

void remp(){
  int nbpar=1,ind=1;
  char tmp;
  cin >> tmp;
  chaine[0]='(';
  while (nbpar!=0){
    cin >> tmp;
    if (tmp=='(')
      nbpar++;
    if (tmp==')')
      nbpar--;
    chaine[ind]=tmp;
    ind++;
  }
  maxi=ind;
  ind=0;
}

int recu(){
  bool neg=false;
  char tmp;
  int res=0;
  tmp=chaine[ind];
  if (tmp=='-'){
      neg=true;
      ind++;
      tmp=chaine[ind];
    }
  res=tmp-48;
  ind++;
  tmp=chaine[ind];
  while (tmp!='('){
    res=res*10+tmp-48;
    ind++;
    tmp=chaine[ind];
  }
  if (neg) return -res;
  return res;
}
  

int lecture(){
  int res;
  ind++;
  if (ind>=maxi) return N+3;
  if (chaine[ind]==')' && chaine[ind+1]=='(' && chaine[ind+2]==')'){
    ind=ind+3;
    while (chaine[ind]!='(' && ind<=maxi)
      ind++;
    return N+1;
  }
  if (chaine[ind]==')'){
    ind++;
    while (chaine[ind]!='(' && ind<=maxi)
      ind++;
    return N+2;
  }
  res=recu();
  while (chaine[ind]!='(' && ind <=maxi)
    ind++;
  return res;
}

void aux2(int k){
  int tmp;
  tmp= (lecture());
  if (tmp!=N+3){
    if (k==0 && tmp==N+1){
      h=false;
      cout << "yes\n";
    }
    else if (chaine[ind+1]==')' && chaine[ind+2]=='(' && chaine[ind+3]==')')
      aux2(k-tmp);
    else if (tmp<N){
      if (h)
	aux2(k-tmp);
      if (h)
	aux2(k-tmp);
    }
  }
}

void aux1(){
  ind=0;
  if (cin >> i!=0){
    remp();
    h=true;
    aux2(i);
    if (h) 
      cout << "no\n";
    aux1();
  }
}

int main(){
  aux1();
  return 0;
}
