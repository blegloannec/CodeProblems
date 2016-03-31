#include <iostream>
using namespace std;

#define MAX 1000000
char buff[MAX];

bool is_letter(char a) {
  return ((a>='a' && a<='z') || (a>='A' && a<='Z'));
}

int main() {
  int curr,nb;
  bool lit;
  while (cin.getline(buff,MAX)) {
    if (buff[0]==0) return 0;
    curr = 0;
    nb = 0;
    lit = false;
    while (buff[curr] != 0 && buff[curr] != '\n') {
      if (lit == false) {
        if (is_letter(buff[curr])) {
          ++nb;
          lit = true;
        }
      }
      else {
        if (!is_letter(buff[curr])) {
          lit = false;
        }
      }
      ++curr;
    }
    cout << nb << '\n';
  }

  return 0;
}
