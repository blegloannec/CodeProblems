#include <iostream>

using namespace std;

int N, ring;

int tab[101][101];

void updown(int k){
  int x0, y0, l;
  int tmp;
  x0=k, y0=k;
  l=N-2*k;

  for (int i=0;i<l;++i){
    tmp=tab[x0][y0+i];
    tab[x0][y0+i]=tab[x0+l-1][y0+i];
    tab[x0+l-1][y0+i]=tmp;
  }
  for (int j=1;j<=(l-1)/2;++j){
    tmp=tab[x0+j][y0];
    tab[x0+j][y0]=tab[x0+l-1-j][y0];
    tab[x0+l-1-j][y0]=tmp;

    tmp=tab[x0+j][y0+l-1];
    tab[x0+j][y0+l-1]=tab[x0+l-1-j][y0+l-1];
    tab[x0+l-1-j][y0+l-1]=tmp;
  }
}

void leftrigth(int k){
  int x0, y0, l;
  int tmp;
  x0=k, y0=k;
  l=N-2*k;

  for (int i=0;i<l;++i){
    tmp=tab[x0+i][y0];
    tab[x0+i][y0]=tab[x0+i][y0+l-1];
    tab[x0+i][y0+l-1]=tmp;
  }
  for (int j=1;j<=(l-1)/2;++j){
    tmp=tab[x0][y0+j];
    tab[x0][y0+j]=tab[x0][y0+l-1-j];
    tab[x0][y0+l-1-j]=tmp;

    tmp=tab[x0+l-1][y0+j];
    tab[x0+l-1][y0+j]=tab[x0+l-1][y0+l-1-j];
    tab[x0+l-1][y0+l-1-j]=tmp;
  }
}

void indiag(int k){
  int x0, y0, l;
  int tmp;
  x0=k, y0=k;
  l=N-2*k;

  for (int i=1;i<l;++i){
    tmp=tab[x0][y0+i];
    tab[x0][y0+i]=tab[y0+l-1-i][x0+l-1];
    tab[y0+l-1-i][x0+l-1]=tmp;
  }

  for (int i=0;i<l;++i){
    tmp=tab[x0+l-1][y0+i];
    tab[x0+l-1][y0+i]=tab[y0+l-1-i][x0];
    tab[y0+l-1-i][x0]=tmp;
  }

}

void diag(int k){
  int x0, y0, l;
  int tmp;
  x0=k, y0=k;
  l=N-2*k;

  for (int i=0;i<l-1;++i){
    tmp=tab[x0][y0+i];
    tab[x0][y0+i]=tab[y0+i][x0];
    tab[y0+i][x0]=tmp;
  }

  for (int i=0;i<l;++i){
    tmp=tab[x0+l-1][y0+i];
    tab[x0+l-1][y0+i]=tab[y0+i][x0+l-1];
    tab[y0+i][x0+l-1]=tmp;
  }
}


int main(){
  int cas, scas, trans;
  cin >> cas;
  while (cas-->0){
    cin >> N;
    for (int i=0;i<N;++i)
      for (int j=0;j<N;++j)
	cin >> tab[i][j];

    ring=(N+1)/2;

    for (int k=0;k<ring;++k){
      cin >> scas;
      for (int l=0;l<scas;++l){
	cin >> trans;
	if (trans==1)
	  updown(k);
	else if(trans==2)
	  leftrigth(k);
	else if (trans==3)
	  diag(k);
	else
	  indiag(k);
      }
    }

    for (int i=0;i<N;++i){
      for (int j=0;j<N-1;++j)
	cout << tab[i][j] << ' ';
      cout << tab[i][N-1];
      cout << '\n';
    }
  }
}
