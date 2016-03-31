#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<bool> pile;
string str;


bool aux(){
  getline(cin, str);
  for (int i=0; i<str.size(); ++i){
    if (str[i]=='(')
      pile.push_back(true);
    else if (str[i]=='[')
      pile.push_back(false);
    else if (str[i]==')'){
      if (pile.size()>0 && pile.back())
	pile.pop_back();
      else return false;
    }
    else if (str[i]==']'){
      if (pile.size()>0 && !pile.back())
	pile.pop_back();
      else
	return false;
    }
  }
  return pile.size()==0;
}

int main(){
  int cas;
  cin >> cas;
  getline(cin, str);
  while(cas-->0){
    pile.clear();
    if (aux())
      cout << "Yes\n";
    else
      cout << "No\n";
  }
}
