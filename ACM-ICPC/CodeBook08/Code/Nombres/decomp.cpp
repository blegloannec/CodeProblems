//decomposition classique en nombre premier
//requiert l utilisation d'eratosthene
//ou l'utilisation de is_prime
void decom(int n){
  int m=n;
  if (m<0){
    m=-m;
    cout << "-1 ";
  }
  while (m%2==0){
    m/=2;
    cout << "2 ";
  }
  int i=3;
  while (i<=sqrt(m)) {
    if (prime[i]) //ou is_prime(i)
      while (m%i==0){
	m/=i;
	cout << i << ' ';
      }
    i+=2;
  }
  if (m!=1)
    cout << m;
}
