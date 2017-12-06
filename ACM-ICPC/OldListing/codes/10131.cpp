#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 1001

struct elephant {
  int first,second,num;
  elephant(int f, int s, int n) : first(f), second(s), num(n) {}
};

vector<elephant> t;

int ordre(const elephant &a, const elephant &b) {
  return a.first < b.first;
}

int v[MAX];
int w[MAX];


int main() {
  int a,b,n,k,imax;
  vector<int> seq;
  n = 1;
  while (cin >> a >> b) {
    t.push_back(elephant(a,b,n));
    ++n;
  }
  if (n==1) {
    cout << "0\n";
    return 0;
  }
  sort(t.begin(), t.end(), ordre);
  v[0] = 1;
  w[0] = 0;
  imax = 0;
  for (int i=1; i<(int)t.size(); ++i) {
    v[i] = 1;
    w[i] = i;
    for (int j=0; j<i; ++j) {
      if ((t[i].first != t[j].first) && (t[i].second < t[j].second) && (v[i] < v[j]+1)) {
        v[i] = v[j]+1;
        w[i] = j;
      }
    }
    if (v[imax] < v[i]) imax = i;
  }
  k = imax;
  cout << v[imax] << '\n';
  while (w[k]!=k) {
    seq.push_back(k);
    k = w[k];
  }
  seq.push_back(k);
  for (int i=(int)seq.size()-1; i>=0; --i)
    cout << t[seq[i]].num << '\n';
  seq.clear();
  return 0;
}
