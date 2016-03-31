struct triple{
  int u,v,d;
};

triple euclide(int a, int b) {
  triple res;
  int q = a / b;
  int r = a % b;
  if (r == 0) {
    res.u=0;
    res.v=1;
    res.d=b;
    return res;
  }
  triple tmp = euclide (b, r);
  res.d = tmp.d;
  res.u = tmp.v;
  res.v = tmp.u - q*tmp.v;
  return res;
}
