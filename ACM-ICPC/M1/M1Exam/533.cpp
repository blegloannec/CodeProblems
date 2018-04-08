#include <iostream>
#include <cstdio>
using namespace std;

/*
    Equation   := Expression '=' Expression
    Expression := Term { ('+' | '-') Term }
    Term       := Factor { '*' Factor }
    Factor     := Number | 'x' | '(' Expression ')'
    Number     := Digit | Digit Number
    Digit      := '0' | '1' | ... | '9'
*/


char buff[1000];
int curr,cas;

inline char current() {
  return buff[curr];
}

inline char next() {
  return buff[++curr];
}

inline bool is_digit(char c) {
  return ('0' <= c && c <= '9');
}

void parse_number(int &b) {
  b = 0;
  while (is_digit(current())) {
    b = 10*b + (current()-'0');
    next();
  }
}

void parse_expression(int &a, int &b);

void parse_factor(int &a, int &b) {
  if (current() == 'x') {
    a = 1;
    b = 0;
    next();
  }
  else if (current() == '(') {
    next(); // (
    parse_expression(a,b);
    next(); // )
  }
  else {
    parse_number(b);
    a = 0;
  }
}

void parse_term(int &a, int &b) {
  parse_factor(a,b);
  while (current() == '*') {
    int c,d;
    next();
    parse_factor(c,d);
    // (ax + b)(cx + d) = (ad+cb)x + bd
    a = a*d + c*b;
    b *= d;
  }
}

void parse_expression(int &a, int &b) {
  parse_term(a,b);
  while (current() == '+' || current() == '-') {
    int c,d;
    char op = current();
    next();
    parse_term(c,d);
    if (op=='+') {
      a = a+c;
      b = b+d;
    }
    else {
      a = a-c;
      b = b-d;
    }
  }
}

void solve() {
  int a,b,c,d;
  // ax + b = cx + d
  curr = 0;
  parse_expression(a,b);
  next(); // =
  parse_expression(c,d);
  // (a-c)x = d-b
  cout << "Equation #" << cas << '\n';
  if (a-c == 0) {
    if (d-b == 0) 
      cout << "Infinitely many solutions.\n";
    else 
      cout << "No solution.\n";
  }
  else 
    printf("x = %.6f\n", (double)(d-b)/(double)(a-c));
}

int main() {
  cas = 1;
  while (cin.getline(buff,sizeof(buff))) {
    if (buff[0]==0) return 0;
    if (cas>1) cout << '\n';
    solve();
    ++cas;
  }
  return 0;
}
