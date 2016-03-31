#include <iostream>
#define MAX 51
using namespace std;

bool matrice[MAX][MAX];
bool mat_calc[MAX][MAX];
bool tmp[MAX][MAX];

//multiplie mat_calc par matrice
void one_mult(int n){
  bool sum;
  for(int i = 0; i < n; ++i){
    for(int k = 0; k < n; ++k){
      sum = false;
      for(int j = 0; j < n; ++j){
	sum = sum || (mat_calc[i][j] && matrice[j][k]);	  
      }    
      tmp[i][k] = sum;
    }
  }
  /*
  if(n == 3){
    cout << mat_calc[0][0] << mat_calc[0][1] << mat_calc[0][2] << " " << matrice[0][0] << matrice[0][1] << matrice[0][2] << " " << tmp[0][0] << tmp[0][1] << tmp[0][2] << endl;
    cout << mat_calc[1][0] << mat_calc[1][1] << mat_calc[1][2] << "*" << matrice[1][0] << matrice[1][1] << matrice[1][2] << "=" << tmp[1][0] << tmp[1][1] << tmp[1][2] << endl;
    cout << mat_calc[2][0] << mat_calc[2][1] << mat_calc[2][2] << " " << matrice[2][0] << matrice[2][1] << matrice[2][2] << " " << tmp[2][0] << tmp[2][1] << tmp[2][2] << endl;
    cout << endl;
    }*/

  for(int i = 0; i < n; ++i)
    for(int j = 0; j < n; ++j)
      mat_calc[i][j] = tmp[i][j];
}

int main(void){
  int n , m , k ;
  cin >> n >> m >> k;
  while(n + m + k != 0){

    for(int i = 0; i < n; ++i)
      for(int j = 0; j < n; ++j){
	matrice[i][j] = false;
	mat_calc[i][j] = false;
      }

    for(int i = 0; i < m; ++i){
      int tp1, tp2;
      cin >> tp1 >> tp2;
      matrice[tp1][tp2] = true;
    }
    mat_calc[0][0] = true;
    
    int cpt = 1;
    while(cpt <= 20 &&
	  (cpt < k || ((cpt >= k) && (mat_calc[0][n-1] == false)))
	  ){

      one_mult(n);
      cpt++;
    }
    if(cpt > 20){
      cout << "LOSER\n";
    }
    else cout << cpt << endl;

    cin >> n >> m >> k;
  }
  
  return 0;
}
