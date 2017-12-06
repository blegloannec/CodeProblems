#include <iostream>

using namespace std;

int nombre[10];
int s; //taille d'un trait
int indice;

char tabhaut[10]={'-',' ','-','-',' ','-','-','-','-','-'};
char tabmil[10]={' ',' ','-','-','-','-','-',' ','-','-'};
char tabbas[10]={'-',' ','-','-',' ','-','-',' ','-','-'};
char tabverthaut[20]={'|','|',' ','|',' ','|',' ','|','|','|','|',' ','|',' ',' ','|','|','|','|','|'};
char tabvertbas[20]={'|','|',' ','|','|',' ',' ','|',' ','|',' ','|','|','|',' ','|','|','|',' ','|'};

void a1(){
  for (int i=indice;i<10;++i){
    cout << ' ';
    for (int j=0;j<s;++j)
      cout << tabhaut[nombre[i]];
    cout << ' ';
    if (i!=9)
    cout << ' ';
  }
  cout << '\n';
}

void a3(){
  for (int i=indice;i<10;++i){
    cout << ' ';
    for (int j=0;j<s;++j)
      cout << tabmil[nombre[i]];
    cout << ' ';
    if (i!=9)
      cout << ' ';
  }
  cout << '\n';
}

void a5(){
  for (int i=indice;i<10;++i){
    cout << ' ';
    for (int j=0;j<s;++j)
      cout << tabbas[nombre[i]];
    cout << ' ';
    if (i!=9)
      cout << ' ';
  }
  cout << '\n';
}

void a2(){
  for (int a=0;a<s;++a){
    for (int i=indice;i<10;++i){
      cout << tabverthaut[nombre[i]*2];
      for (int j=0;j<s;++j)
	cout << ' ';
      cout << tabverthaut[nombre[i]*2+1];
      if (i!=9)
	cout << ' ';
    }
    cout << '\n';
  }
}

void a4(){
  for (int a=0;a<s;++a){
    for (int i=indice;i<10;++i){
      cout << tabvertbas[nombre[i]*2];
      for (int j=0;j<s;++j)
	cout << ' ';
      cout << tabvertbas[nombre[i]*2+1];
      if (i!=9)
	cout << ' ';
    }
    cout << '\n';
  }
}

void affich(){
  a1();
  a2();
  a3();
  a4();
  a5();
}

int main(){
  int n;
  char a[10];
  bool h=false;
  cin >> s;
  while (s!=0){
    //if (h)
    //   cout << '\n';
    //h=true;
    indice=9;

    for (int i=0;i<10;++i)
      a[i]=0;

    scanf("%s\n",a);

    int fina=9;
    while (a[fina]==0)
      fina--;

    while(fina>=0)
    {
      nombre[indice]= a[fina]-48;
      //  cout << "ind:" << indice << '\n';
      indice--;
      fina--;
    }
    //  for (int i=0;i<10;++i)
    //  cout << nombre[i] << ' ';
    //cout << '\n';
    indice++;
    affich();
    cout << '\n';
    cin >> s;
  }
}
