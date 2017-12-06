#include <iostream>

using namespace std;


void p(string b,string a){
  cout << a;
  cout << " ";
  cout << b;
  cout << "\n";
}


int main(){
  p("        8","         6");
  p("       49","        35");
  p("      288","       204");
  p("     1681","      1189");
  p("     9800","      6930");
  p("    57121","     40391");
  p("   332928","    235416");
  p("  1940449","   1372105");
  p(" 11309768","   7997214");
  p(" 65918161","  46611179");
  
  return 0;
}

/*fait a partir de ca

#include <iostream>
#include <gmpxx.h>

using namespace std;

int main(){  
  mpz_t i;
  mpz_t j;
  mpz_t k;
  mpz_init (i);
  mpz_init (j);
  mpz_init (k);
  while (true){
    mpz_add_ui(i,i,1);
    mpz_add_ui(k,i,1);
    mpz_mul(k,k,i);
    mpz_divexact_ui(j,k,2);
    if (mpz_perfect_square_p (j)){
      mpz_sqrt(j, j);
      cout << "i: " << i << " j: " << j << "\n";
    }
  }
  
  return 0;
}
*/
