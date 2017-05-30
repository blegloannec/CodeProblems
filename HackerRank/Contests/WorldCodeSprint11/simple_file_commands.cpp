#include <iostream>
#include <unordered_map>
#include <set>
using namespace std;

unordered_map<string,int> max_no;
unordered_map< string, set<int> > free_no;

int create_file(string &name) {
  if (max_no.find(name)==max_no.end()) {
    max_no[name] = 0;
    return 0;
  }
  else if (free_no[name].empty()) {
    int n = ++max_no[name];
    return n;
  }
  else {
    int n = *free_no[name].begin();
    free_no[name].erase(free_no[name].begin());
    return n;
  }
}

void delete_file(string &name) {
  size_t i = name.find('(');
  if (i==string::npos)
    free_no[name].insert(0);
  else {
    string base = name.substr(0,i);
    int n = stoi(name.substr(i+1,name.size()-i-2));
    free_no[base].insert(n);
  }
}

int main() {
  int q;
  string c,a,b;
  cin >> q;
  for (int i=0; i<q; ++i) {
    cin >> c >> a;
    if (c=="crt") {
      int n = create_file(a);
      if (n==0)	cout << "+ " << a << endl;
      else cout << "+ " << a << '(' << n << ')' << endl;
    }
    else if (c=="del") {
      delete_file(a);
      cout << "- " << a << endl;
    }
    else { // c == "rnm"
      cin >> b;
      delete_file(a);
      int n = create_file(b);
      if (n==0)	cout << "r " << a << " -> " << b << endl;
      else cout << "r " << a << " -> " << b << '(' << n << ')' << endl;
    }
  }
  return 0;
}
