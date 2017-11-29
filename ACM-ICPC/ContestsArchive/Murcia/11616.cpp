#include <iostream>
using namespace std;

string s;

void toroman() {
  int curr = 0;
  if (s.size()>=4) {
    switch (s[curr]) {
    case '1':
      cout << "M";
      break;
    case '2':
      cout << "MM";
      break;
    case '3':
      cout << "MMM";
      break;
    case '4':
      cout << "MMMM";
      break;
    }
    ++curr;
  }
  if (s.size()>=3) {
    switch (s[curr]) {
    case '1':
      cout << "C";
      break;
    case '2':
      cout << "CC";
      break;
    case '3':
      cout << "CCC";
      break;
    case '4':
      cout << "CD";
      break;
    case '5':
      cout << "D";
      break;
    case '6':
      cout << "DC";
      break;
    case '7':
      cout << "DCC";
      break;
    case '8':
      cout << "DCCC";
      break;
    case '9':
      cout << "CM";
      break;
    }
    ++curr;
  }
  if (s.size()>=2) {
    switch (s[curr]) {
    case '1':
      cout << "X";
      break;
    case '2':
      cout << "XX";
      break;
    case '3':
      cout << "XXX";
      break;
    case '4':
      cout << "XL";
      break;
    case '5':
      cout << "L";
      break;
    case '6':
      cout << "LX";
      break;
    case '7':
      cout << "LXX";
      break;
    case '8':
      cout << "LXXX";
      break;
    case '9':
      cout << "XC";
      break;
    }
    ++curr;
  }
  if (s.size()>=1) {
    switch (s[curr]) {
    case '1':
      cout << "I";
      break;
    case '2':
      cout << "II";
      break;
    case '3':
      cout << "III";
      break;
    case '4':
      cout << "IV";
      break;
    case '5':
      cout << "V";
      break;
    case '6':
      cout << "VI";
      break;
    case '7':
      cout << "VII";
      break;
    case '8':
      cout << "VIII";
      break;
    case '9':
      cout << "IX";
      break;
    }
    ++curr;
  }
  cout << endl;
}

void toint() {
  int curr = 0;
  int res = 0;
  while (curr<(int)s.size()) {
  switch (s[curr]) {
  case 'M':
    res += 1000;
    break;
  case 'D':
    res += 500;
    break;
  case 'L':
    res += 50;
    break;
  case 'V':
    res += 5;
    break;
  case 'I':
    if (curr<(int)s.size()-1 && s[curr+1]=='V') {
      res += 4;
      ++curr;
    }
    else if (curr<(int)s.size()-1 && s[curr+1]=='X') {
      res += 9;
      ++curr;
    }
    else 
      res += 1;
    break;
  case 'C':
    if (curr<(int)s.size()-1 && s[curr+1]=='M') {
      res += 900;
      ++curr;
    }
    else if (curr<(int)s.size()-1 && s[curr+1]=='D') {
      res += 400;
      ++curr;
    }
    else 
      res += 100;
    break;
  case 'X':
    if (curr<(int)s.size()-1 && s[curr+1]=='L') {
      res += 40;
      ++curr;
    }
    else if (curr<(int)s.size()-1 && s[curr+1]=='C') {
      res += 90;
      ++curr;
    }
    else 
      res += 10;
    break;
  }
  ++curr;
  }
  cout << res << endl;
}

int main() {
  
  while (cin >> s) {
    if (s[0]>='0' && s[0]<='9')
      toroman();
    else
      toint();
  }
  
  return 0;
}
