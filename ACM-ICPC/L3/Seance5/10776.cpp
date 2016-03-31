#include <iostream>
#include<vector>
#include<string>

using namespace std;


int n;
vector<char> chaine;

void aux(int ind, int i, string tmp){
  string paf;
  
  //cout << "ind="<< (ind) << " i=" << (i) << " chaine=" << tmp << "\n";
  
  if (i==0)
    cout << tmp << "\n";
  else{ 
    for (int j=ind; j<=(n-i);j++){
      paf=tmp;
      if (chaine[j]==chaine[j+1]){
	aux(j+1,i-1,paf.append(1,chaine[j]));
	int k=j;
	while (chaine[k]==chaine[j+1])
	  j++;
      }
      else
	aux(j+1,i-1,paf.append(1,chaine[j]));
    }}}

int main(){
 
  int nb;
  string tmp;
 
  
  while (cin >> tmp!=0){
    chaine.clear();
    
    for (int i=0;i<tmp.length();i++)
      chaine.push_back(tmp[i]);
    sort(chaine.begin(), chaine.end() );
    n=chaine.size();
    cin >> nb; 
    aux(0, nb, "");
  }
  return 0;
}

