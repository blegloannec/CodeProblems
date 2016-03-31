//remplit le crible des nombres premiers jusqu'a n-1 dans le tableau prime
bool prime[MAX];

void eratosthene(int n){
  int m=sqrt(n);
  for(int i=0;i<n;i++)
    prime[i]= (i%2!=0);
  prime[1]=false;
  prime[2]=true;
  for(int i=3;i<=m;i+=2){
    if (prime[i])
      for(int j=2*i;j<n;j+=i)
	prime[j]=false;
  }
}
