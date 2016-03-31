#include <iostream>

using namespace std;

#define MAX 105
#define INF -1000000
#define TINF -1000

int n;
//matbase[i][j]: cout pour aller de i a j;
int matbase[MAX][MAX];
int vec[MAX];
int vectmp[MAX];
int matres[MAX][MAX];
int mattmp[MAX][MAX];

void init(){
  int e, nbdoor, tmp;

  for (int i=0;i<n;++i)
    vec[i]= INF;

  vec[0]= 100;

  for (int i=0;i<n;++i)
    for (int j=0;j<n;++j)
      matbase[i][j]= INF;

  for (int i=0;i<n;++i){
    cin >> e >> nbdoor;
    for (int j=0;j<nbdoor;++j){
      cin >> tmp;
      tmp--;
      matres[i][tmp] = matbase[i][tmp]= e;
    }
  }
  for (int i=0;i<n;++i)
    matbase[i][i]=0;
}

void computvec(){
  for (int i=0;i<n;++i){
    vectmp[i]= vec[0] + matbase[0][i];
    for (int k=1;k<n;++k){
      vectmp[i]= max(vectmp[i], vec[k]+ matbase[k][i]);
    }
  }
  for (int i=0;i<n;++i)
    if (vectmp[i]>0)
      vec[i]= max(vec[i],vectmp[i]);
}

void computmat(){
  for (int i=0;i<n;++i)
    for (int j=0;j<n;++j){
      mattmp[i][j]= matres[i][0]+matbase[0][j]; 
      for (int k=1;k<n;++k){
        mattmp[i][j]= max(mattmp[i][j], matres[i][k]+ matbase[k][j]);
      }
    }
  for (int i=0;i<n;++i)
    for (int j=0;j<n;++j){
      if (mattmp[i][j]>TINF)
        matres[i][j]= max(matres[i][j], mattmp[i][j]);
    }
}


int main(){
  cin >> n;
  while (n!=-1){
    init();

    for (int i=0;i<n;++i){
      computmat();
      computvec();
    }

    for (int i=0; i<n;++i)
      cout << vec[i] << " ";

    if (vec[n-1]< TINF)
      cout << "hopeless\n";
    else{
      bool possible=false;
      for (int i=0;i<n;++i){
        if (vec[i]>0 && matres[i][i]>0 && matres[i][n-1]>TINF)
          possible=true;
      }
      if (possible || vec[n-1]>0)
        cout << vec[n-1] << "winnable\n";
      else
        cout << "hopeless\n";
    }

    cin >> n;
  }
}
