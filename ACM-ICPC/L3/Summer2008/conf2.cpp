/* 
   Functions to convert a configuration to some different
   output formats.
   Bastien Le Gloannec - 10/08/2008
*/

#include <iostream>
using namespace std;


/*
  ------------------- Conversions to ASCII ------------------------
*/

char int2char(int i) {
  if (i<10) return (char)(i+48);
  else if (i<37) return (char)(i-10+65);
  else return (char)(i-37+97);
}

void conf2ascii(int c(int,int), int x0, int y0, int x1, int y1) {
  for (int i=x0; i<=x1; i++) {
    for (int j=y0; j<=y1; j++)
      cout << int2char(c(i,j));
    cout << endl;    
  }
}

char bool2char(bool b) {
  if (b) return '1';
  else return '0';
}

void conf2ascii(bool c(int,int), int x0, int y0, int x1, int y1) {
  for (int i=x0; i<=x1; i++) {
    for (int j=y0; j<=y1; j++) {
      cout << i << j << endl;
      cout << bool2char(c(i,j));
    }
    cout << endl;    
  }
}


/*
  ------------------- Conversions to XHTML -----------------------------
*/

void htmlgen(char c) {
  cout << "<span style=\"cell;cell" << c << "\">" << c << "<\\span>";
}

void conf2html(int c(int,int), int x0, int y0, int x1, int y1) {
  for (int i=x0; i<=x1; i++) {
    for (int j=y0; j<=y1; j++) 
      htmlgen(int2char(c(i,j)));
    cout << "<br \\>" << endl;    
  }
}

void conf2html(bool c(int,int), int x0, int y0, int x1, int y1) {
  for (int i=x0; i<=x1; i++) {
    for (int j=y0; j<=y1; j++) 
      htmlgen(bool2char(c(i,j)));
    cout << "<br \\>" << endl;
  }
}



/*
  ------------------- Conversions to PPM ------------------------------
  TODO
*/
