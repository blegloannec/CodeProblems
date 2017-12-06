#include <iostream>
using namespace std;

int beans[26];
int Score[26];
double TotNum;
double TotShares;

void traite(int i, int j, int curr) {
  ++TotNum;
  if (curr == beans[j]) {
    Score[i] +=2;
    TotShares += 2;
  }
  else if (curr-beans[j]==1 || curr-beans[j]==-1) {
    Score[i] +=1;		       
    ++TotShares;
  }
}

int main() {
  int cas,curr;
  char buff[100000];
  cin >> cas;
  cin.ignore();
  cin.ignore();
  while (cas-->0) {
    
    TotNum = 0;
    TotShares = 0;
    for (int i=0; i<26; ++i) {
      beans[i] = 0;
      Score[i] = 0;
    }

    cin.getline(buff,sizeof(buff));
    int c = 0;
    while (buff[c]!=0 && buff[c]!='\n') {
      beans[buff[c]-'a'] += 1;
      ++c;
    }
    cin.getline(buff,sizeof(buff));
    while (buff[0]!=0 && buff[0]!='\n') {
      c = 2;
      int i,j;
      i = buff[0]-'A';
      j = -1;
      curr = 0;
      while (buff[c]!=0 && buff[c]!='\n') {
	if (buff[c]==':' || buff[c]==' ') ++c;
	else if (buff[c]==',') {
	  traite(i,j,curr);
	  ++c;
	  j = -1;
	}
	else if (j<0) {
	  j = buff[c]-'a';
	  curr = 0;
	  ++c;
	}
	else {
	  curr = curr*10 + buff[c]-'0';
	  ++c;
	}
      }
      cin.getline(buff,sizeof(buff));
      traite(i,j,curr);      
    }
    for (int i=0; i<26; ++i) 
      if (Score[i]>0)
	printf("%c %.2f\n",i+'A',(double)Score[i]*2.*TotNum/TotShares);
    if (cas>0) cout << '\n';
  }

  return 0;
}
