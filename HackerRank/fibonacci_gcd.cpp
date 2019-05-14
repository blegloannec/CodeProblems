/*
  Pretty easy knowing that gcd(F_a,F_b) = F_gcd(a,b)
  Fibonacci is a strong divisibility sequence
  https://en.wikipedia.org/wiki/Divisibility_sequence
*/
#include <iostream>
using namespace std;
using ent = long long;

const ent P = 1000000007;

struct Matrix2 {
  ent m00, m01, m10, m11;
  
  Matrix2(ent a=1, ent b=0, ent c=0, ent d=1) :
    m00(a), m01(b), m10(c), m11(d) {}
  
  Matrix2 operator*(const Matrix2 &B) const {
    return Matrix2(((m00*B.m00)%P+(m01*B.m10)%P)%P,
		   ((m00*B.m01)%P+(m01*B.m11)%P)%P,
		   ((m10*B.m00)%P+(m11*B.m10)%P)%P,
		   ((m10*B.m01)%P+(m11*B.m11)%P)%P);
  }
  
  Matrix2 pow(ent n) const {
    if (n==0) return Matrix2();
    if ((n&1)==0) return ((*this)*(*this)).pow(n>>1);
    return (*this)*((*this)*(*this)).pow(n>>1);
  }
};

ent gcd(ent a, ent b) {
  return b==0 ? a : gcd(b,a%b);
}

ent fibo(ent n) {
  return Matrix2(0,1,1,1).pow(n).m11;
}

int main() {
  int N;
  cin >> N;
  ent g = 0;
  for (int i=0; i<N; ++i) {
    ent a;
    cin >> a;
    g = gcd(a,g);
  }
  cout << fibo(g-1) << endl;
  return 0;
}
