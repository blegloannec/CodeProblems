#include <iostream>

using namespace std;

 int main(){
  long long n,m;
  while (cin >> n >> m)
     if (n>=m)
       cout << (n-m) << '\n';
     else
       cout << (m-n) << '\n';
}
