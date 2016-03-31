#include <iostream>
#include <math.h>
#include <string>
#define EPSILON 1e-6
#define PLUSQUEMAX 1500
using namespace std;

struct segment{
  double x1, y1;
  double x2, y2;
  segment(double a1, double a2, double a3, double a4): x1(a1), y1(a2), x2(a3), y2(a4){};
  segment(void): x1((double) 0.0), y1((double) 0.0), x2((double) 0.0), y2((double) 0.0) {};
};

double my_min(double a, double b){
  if(a < b) return a;
  else return b;
};

double my_max(double a, double b){
  if(a < b) return b;
  else return a;
};

// attention, je pars du principe que dans tout segment, x1 < x2
double intersect_x(int y, segment s, bool gauche){ 
  double non_tr ;
  if(gauche)
    non_tr = (double) PLUSQUEMAX;
  else 
    non_tr = (double) -1.0;

  if(s.y1 == s.y2){
    if(s.y1 == y) {
      if(gauche) return s.x1;
      else return s.x2;
    }
    else return non_tr;
  }
  double my_x = ((((double) y) - s.y1)/(s.y2 - s.y1)) * (s.x2 - s.x1) + s.x1;
  if(my_x < (s.x1 - EPSILON) || my_x > (s.x2 + EPSILON)) 
    return (double) non_tr; 
  else {
    return my_x;
  }
}

int my_ceil(double x){
  return (int) round(x + (double)0.5 - (double) EPSILON);
}

int my_floor(double x){
  return (int) round(x - (double) 0.5 + (double) EPSILON);
}

void test(void){
  cout << "15 " << my_ceil(14.8) << " " << my_floor(15.2) << endl;
  cout << "15 " << my_ceil(15.0) << " " << my_floor(15.0) << endl;
  segment s1(1.5, 6.8, 6.8, 1.5);
  cout << my_floor(intersect_x(2, s1, false));
}

int main(void){
  //test();
  double x1, y1, x2, y2, x3, y3;
  double y_max, y_min;
  int xi_1, xi_2; //seront les deux points d'intersection à la hauteur y
  int res;
  struct segment s1, s2, s3;
  while(cin >> x1){
    cin >> y1 >> x2 >> y2 >> x3 >> y3;
    if(x1 == 0 && x2 == 0 && x3 == 0 && y1 == 0 && y2 == 0 && y3 == 0) return 0;
    
    y_max = my_max(y1, my_max(y2, y3));
    y_min = my_min(y1, my_min(y2, y3));

    if (x1 < x2)
      s1 = segment(x1, y1, x2, y2);
    else
      s1 = segment(x2, y2, x1, y1);

    if (x1 < x3)
      s2 = segment(x1, y1, x3, y3);
    else
      s2 = segment(x3, y3, x1, y1);
    

    if (x2 < x3)
      s3 = segment(x2, y2, x3, y3);
    else
      s3 = segment(x3, y3, x2, y2);

    res = 0;
    for(int i = max(1,my_ceil(y_min)); i <= min(99,my_floor(y_max)); ++i){ //cf attention les arbres ne sont qu'entre 1 et 99
      xi_1 = max(my_floor(intersect_x(i, s1, false)),
		 my_floor(intersect_x(i, s2, false))); 
      xi_1 = max(xi_1, my_floor(intersect_x(i, s3, false)));
      
      xi_2 = min(my_ceil(intersect_x(i, s1, true)), 
		my_ceil(intersect_x(i, s2, true)));
      xi_2 = min(xi_2, my_ceil(intersect_x(i, s3, true)));
      //cout << "ligne " << i << " inter : " << xi_1 << " - " << xi_2 << endl;

      if(xi_1 != PLUSQUEMAX && xi_1 != -1){
	if(xi_1 > 99) xi_1 = 99; //cf les arbres ne sont qu'entre 1 et 99 ...
	if(xi_2 < 1) xi_2 = 1; //faudrait mettre 2 tests de plus non ?
	res += xi_1 - xi_2 + 1;
      } 
    };
    string str_res = "";  //pour aligner à droite sur 4 caractères
    if(res < 1000) str_res += " ";
    if(res < 100) str_res += " ";
    if(res < 10) str_res += " ";
    cout << str_res << res << endl;
  }
  return 0;
}