// ACM 213
#include <iostream>
using namespace std;

char key[300];
char c;
int t,r;

int indice[8] = {0,0,1,4,11,26,57,120};
int maxi[8] = {0,1,3,7,15,31,63,127};

void read_char() {
  cin >> c;
  while (c=='\n') cin >> c;
}

bool read_size() {
  t = 0;
  for (int i=0; i<3; i++) {
    t *= 2;
    read_char();
    if (c=='1') ++t;
  }
  return (t>0);
}

bool read_block() {
  r = 0;
  for (int i=0; i<t; i++) {
    r *= 2;
    read_char();
    if (c=='1') ++r;
  }
  if (r<maxi[t]) cout << key[indice[t]+r];
  return (r<maxi[t]);
}


int main() {
  
  while (cin.getline(key,sizeof(key))) {
    while (read_size())
      while (read_block()) {}
    cout << '\n';
    cin.getline(key,sizeof(key));
  }
  
  return 0;
}
