#include <iostream>

using namespace std;

int n,m;
//tableau plus grand pour eviter le debordement
//un nombre negatif represente une mine
int tab[105][105];


void affich(){
  for (int i=1;i<=n;++i){
    for (int j=1;j<=m;++j){
      if (tab[i][j]<0)
	cout << '*';
      else
	cout << tab[i][j];
      }
    cout << '\n';
  }
}

int main(){
  int cas=1;
  bool h=false;
  char a;
  cin >> n >> m;
  while (n!=0 && m!=0){
    if (h)
      cout << '\n';
    h=true;
    for (int i=1;i<=n;++i)
      for (int j=1;j<=m;++j)
	tab[i][j]=0;
    for (int i=1;i<=n;++i){
      for (int j=1;j<=m;++j){
	cin >> a;
	if (a=='*'){
	  tab[i][j]=-10;
	  tab[i+1][j-1]++;
	  tab[i+1][j]++;
	  tab[i+1][j+1]++;
	  tab[i][j-1]++;
	  tab[i][j+1]++;
	  tab[i-1][j+1]++;
	  tab[i-1][j]++;
	  tab[i-1][j-1]++;
	}
      }
    }
    cout << "Field #" << cas++ << ":\n";
    affich();
    cin >> n >> m;
  }
}
