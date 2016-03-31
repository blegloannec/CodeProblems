#include <iostream>
#include <math.h>

using namespace std;

int n;
/*
void verif(int deb, int l){
  int tmp=0;
  for (int j=deb;j<=deb+l;j++)
    tmp= tmp+j;
  if (n!=tmp){
    cout << deb << " " << l << "\n";
    cout << n << "!=" << tmp << "\n";
  }}
*/

void aux(){
  bool h=false;
  int l=sqrt(2*n)+2,tmp=0,tmp1;
  //cout << "l: " << l << "\n";
   while (l>0 && !h){
     l--;
     tmp=(2*n-l*(l+1))/(2*(l+1));
     h=(tmp>=0 && n== (l+1)*tmp+(l*(l+1)/2));
   
   }
   // cout << "n= " << (l+1)*tmp+(l*(l+1)/2) << "\n";
   //cout << "l= " << l << " tmp= " << tmp << "\n";
   if (tmp==0 && l>0)
     tmp1=tmp+1;
   else 
     tmp1=tmp;
   //verif(tmp,l);
    cout << n << " = " << tmp1 << " + ... + " << tmp+l << "\n";
}

int main(){
  //for (int i=0;i<=1000000000;i++){
  // n=i;
  // aux();
  //}
  
  
  cin >> n;
  while (n>-1){
    aux();
    cin >> n;
  }
  
  return 0;
}
