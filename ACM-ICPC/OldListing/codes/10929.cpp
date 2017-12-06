#include <iostream>

using namespace std;

#define N 1010;

string str;

void aux(){
  int length=str.length();
  int res=0;
  int j=length-1;
  for (j;j>0;j=j-2){
    // int tmp =(str[j]-48)+10*(str[j-1]-48);
    //cout << tmp << "\n";
    res= res+(str[j]-48)+10*(str[j-1]-48);
      }
  if (j==0)
    res= res+(str[0]-48);
  //cout << "res: " << res << "\n";
  if (res % 11==0)
    cout << str << " is a multiple of 11.\n";
  else
    cout << str << " is not a multiple of 11.\n";
}


int main(){
  cin >> str;
  while (str!="0"){
    aux();
    str.clear();
    cin >> str;
  }
  return 0;
}
