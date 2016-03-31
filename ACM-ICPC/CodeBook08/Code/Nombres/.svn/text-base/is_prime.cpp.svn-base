typedef long long ent;

//exp_mod(a,b,n) retourne a**b%n
ent exp_mod(ent a,ent b, ent n){
  if (b==0) return 1;
  ent tmp=exp_mod(a,b/2,n);
  if ((b%2)==0)
    return (tmp*tmp)%n;
  else
    return (tmp*tmp*a)%n;
}

bool temoin(int a, ent n){
  //u,t tq n-1=2**t*u, u impair
  ent u=n-1,t=0;
  while (u%2==0){
    u/=2;
    t++;
  }
  ent xi=exp_mod(a,u,n),xj;
  for(int i=1;i<=t;i++){
    xj=(xi*xi)%n;
    if (xj==1 && xi!=1 && xi!=(n-1))
      return true;
    xi=xj;
  }
  return (xj!=1);
}

//data magique
int data[]={31, 73, 2, 7, 61};

bool magic(ent n, int deb, int l){
  for(int i=deb;i<deb+l;i++)
    if (n!=data[i] && temoin(data[i], n)) return false;
  return true;
}

bool miller(ent n){

  if (n==1) return false;
  if (n==2) return true;
  if (n%2==0) return false;

  if (n<9080191LL) return magic(n,0,2);
  if (n<388880279LL) return magic(n,2,3);

  for(int i=3;i<=sqrt(n);i+=2)
    if (n%i==0) return false;
  return true;

}
