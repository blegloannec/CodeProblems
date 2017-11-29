#include <iostream>
#include <map>
#include <set>
using namespace std;

map<string,int> PwS, PwH;
int nb_spam, nb_ham;
map<string,int>::iterator it;
set<string> dejavu;
string word;

double PSw() {
  double p0,p1;
  it = PwS.find(word);
  if (it == PwS.end())
    p0 = 0.;
  else 
    p0 = (double)(it->second)/(double)nb_spam;
  it = PwH.find(word);
  if (it == PwH.end())
    p1 = 0.;
  else 
    p1 = (double)(it->second)/(double)nb_ham;
  if (p0+p1 == 0.) 
    return 0.4;
  else return p0/(p0+p1);
}

double PpSw() {
  double P = PSw();
  if (P < 0.01)
    return 0.01;
  else if (P > 0.99)
    return 0.99;
  else 
    return P;
}

int main() {
  string msg, header;
  
  nb_spam = nb_ham = 0;

  while (cin >> msg >> header) {
    if (header=="SPAM") {
      dejavu.clear();
      ++nb_spam;
      while (cin >> word) {
	if (word == "==") 
	  break;
	it = PwS.find(word);
	if (it == PwS.end())
	  PwS.insert(pair<string,int>(word,1));
	else {
	  if (dejavu.find(word) == dejavu.end()) {
	    it->second += 1;
	    dejavu.insert(word);
	  }
	}
      }
    }
    else if (header=="HAM") { 
      dejavu.clear();
      ++nb_ham;
      while (cin >> word) {
	if (word == "==") 
	  break;
	it = PwH.find(word);
	if (it == PwH.end())
	  PwH.insert(pair<string,int>(word,1));
	else {
	  if (dejavu.find(word) == dejavu.end()) {
	    it->second += 1;
	    dejavu.insert(word);
	  }
	}
      }
    }
    else {
      double p0,p1,p2;
      p1 = p2 = 1.0;
      while (cin >> word) {
	if (word == "==") 
	  break;
	p0 = PpSw();
	p1 *= p0;
	p2 *= (1-p0);
      }
      p0 = p1/(p1+p2);
      if (p0 >= 0.6) 
	cout << "Spam\n";
      else if (p0 <= 0.4)
	cout << "Ham\n";
      else 
	cout << "Unsure\n";
    }
  }

  return 0;
}
