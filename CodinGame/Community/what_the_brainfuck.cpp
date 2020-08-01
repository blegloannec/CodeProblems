#include <iostream>
#include <vector>
#include <stack>
using namespace std;

enum token {PLUS, MINUS, LEFT, RIGHT, OPEN, CLOSE, COMMA, POINT};

struct instr {
  token name;
  int jump;
  instr(token c, int j=1) : name(c), jump(j) {}
};

struct BFInterpreter {
  vector<instr> program;
  
  BFInterpreter(const string &program_string) {
    stack<int> cpt;
    for (char c : program_string) {
      switch (c) {
      case '+': 
	program.push_back(instr(PLUS));
	break;
      case '-':
	program.push_back(instr(MINUS));
	break;
      case '<':
	program.push_back(instr(LEFT));
	break;
      case '>':
	program.push_back(instr(RIGHT));
	break;
      case '.': 
	program.push_back(instr(POINT));
	break;
      case ',':
	program.push_back(instr(COMMA));
	break;
      case '[':
	cpt.push((int)program.size());
	program.push_back(instr(OPEN));
	break;
      case ']':
	if (cpt.empty()) throw string("SYNTAX ERROR");
	program.push_back(instr(CLOSE, cpt.top()));
	program[cpt.top()].jump = (int)program.size();
	cpt.pop();
	break;
      }
    }
    if (!cpt.empty()) throw string("SYNTAX ERROR");
  }
  
  void run(const int tape_size, const vector<int> &input) const {
    vector<unsigned char> tape(tape_size, 0);
    int tp = 0;  // tape pointer
    int pp = 0;  // program pointer
    int ip = 0;  // input pointer
    while (pp<(int)program.size()) {
      switch (program[pp].name) {
      case PLUS:
	if (tape[tp]==255) throw string("INCORRECT VALUE");
	++tape[tp];
	++pp;
	break;
      case MINUS:
	if (tape[tp]==0) throw string("INCORRECT VALUE");
	--tape[tp];
	++pp;
	break;
      case RIGHT:
	++tp;
	if (tp==tape_size) throw string("POINTER OUT OF BOUNDS");
	++pp;
	break;
      case LEFT:
	if (tp==0) throw string("POINTER OUT OF BOUNDS");
	--tp;
	++pp;
	break;
      case OPEN:
	if (tape[tp]==0) pp = program[pp].jump;
	else ++pp;
	break;
      case CLOSE:
	pp = program[pp].jump;
	break;
      case COMMA:
	if (ip==(int)input.size()) throw string("MISSING INPUT");
	if (!(0<=input[ip] && input[ip]<=255)) throw string("INVALID INPUT");
	tape[tp] = input[ip++];
	++pp;
	break;
      case POINT:
	cout << (char)tape[tp];
	++pp;
	break;
      }
    }
  }
};

int main() {
  int L,S,I;
  cin >> L >> S >> I; cin.ignore();
  string Prog;
  for (int i=0; i<L; ++i) {
    string line;
    getline(cin, line);
    Prog += line;
  }
  vector<int> In(I);
  for (int i=0; i<I; ++i) cin >> In[i];
  try {
    BFInterpreter BFI(Prog);
    BFI.run(S, In);
  }
  catch (const string &error) {
    cout << error << endl;
  }
  return 0;
}
