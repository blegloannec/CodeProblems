#include <iostream>

using namespace std;

int indice;
int reg[10];
char ram[1000][4];
int compteur;
bool halt;

void init(){
  indice=0;
  halt=false;
  compteur=0;
  for (int i=0;i<10;++i)
    reg[i]=0;
  for (int i=0;i<1000;++i)
    for (int j=0;j<3;++j)
      ram[i][j]='0';
}

void simul(){
  int a,s;
  switch (ram[indice][0]){
  case '0':
    if (reg[ram[indice][2]-48]==0)
      indice++;
    else
      indice= reg[ram[indice][1]-48];
    break;

  case '1':
    halt= (ram[indice][1]=='0' && ram[indice][2]=='0');
    indice++;
    break;

  case '2':
    reg[ram[indice][1]-48]= ram[indice][2]-48; 
    indice++;
    break;
    
  case '3':
    reg[ram[indice][1]-48]=(reg[ram[indice][1]-48]+(ram[indice][2]-48)) % 1000; 
    indice++;
    break;
    
  case '4':
    reg[ram[indice][1]-48]=(reg[ram[indice][1]-48]*(ram[indice][2]-48)) % 1000; 
    indice++;
    break;
    
  case '5':
    reg[ram[indice][1]-48]= reg[ram[indice][2]-48]; 
    indice++;
    break;
    
  case '6':
    reg[ram[indice][1]-48]=(reg[ram[indice][1]-48]+reg[ram[indice][2]-48]) % 1000; 
    indice++;
    break;
    
  case '7':
    reg[ram[indice][1]-48]=(reg[ram[indice][1]-48]*reg[ram[indice][2]-48]) % 1000; 
    indice++;
    break;
    
  case '8':
    a=reg[ram[indice][2]-48];
    reg[ram[indice][1]-48]= (ram[a][0]-48)*100 + (ram[a][1]-48)*10 + (ram[a][2]-48);
    indice++;
    break;
    
  case '9':
    a=reg[ram[indice][2]-48];
    s=reg[ram[indice][1]-48];
    ram[a][0]=(s/100)+48;
    ram[a][1]=((s/10)%10)+48;
    ram[a][2]=(s%10)+48;
    indice++;
    break;
  
  default:
    indice++;
    break;
  } 
}

int main(){
  int cas;
  bool deb =false;
  char buff[100];
  buff[0]=0;
  cin >> cas;
  cin.ignore();
  while (cas-->0) {
    if (deb)
      cout << '\n';
    deb=true;
    init();
    while ((buff[0]==0)||(buff[0]=='\n')) cin.getline(buff,sizeof(buff));
    while (sscanf(buff,"%s\n",ram[indice++])==1)
      cin.getline(buff,sizeof(buff));
    indice=0;

    while (!halt){
      compteur++;
      simul();
      // cout << "compteur: " << compteur << '\n';
      //cout << "indice: " << indice << '\n';
      //for (int i=0;i<10;++i)
      //	cout << "reg" << i << ": " << reg[i] << '\n';
      //cout << '\n';
    }

    cout << compteur << '\n';
  }
}
