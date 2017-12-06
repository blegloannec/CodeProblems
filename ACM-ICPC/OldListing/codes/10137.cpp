//10137

#include <iostream>
#include <math.h>

using namespace std;

double a[1000];
int n;

int main(void){
  cin >> n;
  while(n != 0){
    double moy = 0;
    for(int i = 0; i < n; ++i){
      cin >> a[i];
      moy += a[i];
    }
    moy /= (double) n;
    double sum1 = 0;
    double sum2 = 0;
    for(int i = 0; i < n; ++i){
      sum1 += (a[i] < moy) ? round((-a[i]+moy)*100.0)/100.0 : 0;
      sum2 += (a[i] > moy) ? (round(100*(a[i]-moy)) / 100.0) : 0;
    }
    cout.precision(2);
    cout << "$" << fixed << min(sum1, sum2) << endl;
    cin >> n;
  }
  return 0;
}
