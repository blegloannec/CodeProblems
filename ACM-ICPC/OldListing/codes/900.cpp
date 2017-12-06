#include <iostream>

using namespace std;

long long res[51];


long long fibonacci(int n)
{
  if (n<2) return 1;
  if (res[n]!=(-1)) return res[n];
  else{
    long long a1=(fibonacci (n-1));
    long long a2=(fibonacci (n-2));
    long long u= a1 +a2;
    res[n]=u;
    return u;
  }
}

int main()
{
  int n;
  for (int i=0;i<51;i++)
    res[i]= (-1);
  cin >> n;
  while (n!=0){
    cout << (fibonacci(n)) << '\n';
    cin >> n;
  }
  return 0;
}
