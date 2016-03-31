// retourne true ssi les segments [a, b] et [c, d] s'intersectent
bool inter_segment(const point &a, const point &b, const point &c, const point &d) {
  return ((long long)(det(a, b, c)) * det(a, d, b) >= 0)
    && ((long long)(det(c, d, a)) * det(c, b, d) >= 0);
}
