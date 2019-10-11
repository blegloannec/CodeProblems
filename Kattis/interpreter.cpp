// adapted from ACM-ICPC 10033
#include <iostream>
#include <vector>
using namespace std;

int p = 0;
vector<int> reg(10,0);
vector<string> ram(1000,"000");
const int Z = '0';

bool step() {
  int a,s;
  switch (ram[p][0]) {
  case '0':
    if (reg[ram[p][2]-Z]==0) ++p;
    else p = reg[ram[p][1]-Z];
    break;
  case '1':
    return false;
    break;
  case '2':
    reg[ram[p][1]-Z] = ram[p][2]-Z; 
    ++p;
    break;
  case '3':
    reg[ram[p][1]-Z] = (reg[ram[p][1]-Z] + (ram[p][2]-Z)) % 1000; 
    ++p;
    break;
  case '4':
    reg[ram[p][1]-Z] = (reg[ram[p][1]-Z] * (ram[p][2]-Z)) % 1000; 
    ++p;
    break;
  case '5':
    reg[ram[p][1]-Z] = reg[ram[p][2]-Z]; 
    ++p;
    break;
  case '6':
    reg[ram[p][1]-Z] = (reg[ram[p][1]-Z] + reg[ram[p][2]-Z]) % 1000; 
    ++p;
    break;
  case '7':
    reg[ram[p][1]-Z] = (reg[ram[p][1]-Z] * reg[ram[p][2]-Z]) % 1000; 
    ++p;
    break;
  case '8':
    a = reg[ram[p][2]-Z];
    reg[ram[p][1]-Z] = (ram[a][0]-Z)*100 + (ram[a][1]-Z)*10 + (ram[a][2]-Z);
    ++p;
    break;
  case '9':
    a = reg[ram[p][2]-Z];
    s = reg[ram[p][1]-Z];
    ram[a][0] = (s/100) + Z;
    ram[a][1] = ((s/10)%10) + Z;
    ram[a][2] = (s%10) + Z;
    ++p;
    break;
  default:
    ++p;
    break;
  }
  return true;
}

int main(){
  while (cin >> ram[p++]) {}
  p = 0;
  int cpt = 1;
  while (step()) ++cpt;
  cout << cpt << endl;
}
