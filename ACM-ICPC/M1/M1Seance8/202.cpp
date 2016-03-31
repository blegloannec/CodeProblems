#include <iostream>
using namespace std;

int n, d;
int reste, quotient;


void remains(int a_diviser){
  quotient = a_diviser / d;
  reste = a_diviser - quotient * d;
};


int main(void){
  int cas = 0;
  while(cin >> n){
    if(cas != 0) cout << endl;
    cas++;
    cin >> d;
    cout << n << "/" << d << " = ";
    
    remains(n);
    cout << quotient << '.';
    int cpt = 0;

    //    cout << "..." << quotient << " r " << reste << endl;
    int vus_a[d];
    for(int i = 0; i < d; ++i){
      vus_a[i] = -1;
    }
    int decimales[d];
    // pas forcé nécessaire
    for(int i = 0; i < d; ++i){
      decimales[i] = 0;
    }
    

    vus_a[reste] = true;
    bool fin = false;
    while(!fin){

      reste *= 10;
      remains(reste);
      decimales[cpt] = quotient;
      //cout << "...." << cpt << " " << quotient << " r " << reste << endl;
      if(reste == 0){
	//alors on écrit toutes les décimales puis (0)
	for(int i = 0; i <= cpt; ++i){
	  cout << decimales[i];
	}
	cout << "(0)\n";
	cout << "   1 = number of digits in repeating cycle\n";
	fin = true;
      }
      
      if(vus_a[reste] > -1){
	//alors cycle de la position de vus_a[reste] à cpt-1
	for(int i = 0; i < vus_a[reste]-1; ++i){
	  cout << decimales[i];
	}
	cout << "(";
	for(int i = vus_a[reste]-1; i < min(cpt+1, vus_a[reste] + 50 - 1); ++i){
	  cout << decimales[i];
	}; 
	if(cpt+1 - vus_a[reste]+1 > 50) cout << "...";
	cout << ")\n";
	
	cout << "   " << cpt - vus_a[reste] + 2 << " = number of digits in repeating cycle\n";
	fin = true;
      }
      vus_a[reste] = cpt;
      cpt++;
    };  
  
  };

  cout << endl;
  return 0;
}
