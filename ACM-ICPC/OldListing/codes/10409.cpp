#include <iostream>

using namespace std;

int top, north, west;

int main(){
  int n,atop, anorth, awest;
  string tmp;
  cin >> n;
  while(n>0){
    top=1;
    north=2;
    west=3;
    while (n-->0){
      cin >> tmp;
      atop= top;
      anorth= north;
      awest= west;
      if (tmp=="north"){
	top= 7-anorth;
	north= atop;
      }
      else if (tmp=="south"){
	top= anorth;
	north= 7-atop;
      }
      else if (tmp=="west"){
	top= 7-awest;
	west= atop;
      }
      else {
	top= awest;
	west= 7-atop;
      }
    }
    cout << top << '\n';
    cin >> n;
  }
}
