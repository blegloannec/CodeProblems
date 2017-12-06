#include <iostream>
#include <string>

using namespace std;

string exam(string n)
{
  if (n=="1" || n=="4" || n=="78")
    return "+\n";
  if (n.substr(n.length()-2,2)=="35")
    return "-\n";
  if (n.substr(0,3)=="190")
    return "?\n";
  if (n[0]=='9' && n[n.length()-1]=='4')
    return "*\n";
  return "";
}

int main(){
  int cas;
  string n;
  cin >> cas;
  while (cas-->0){
    cin >> n;
    cout << exam(n);
  }
}
