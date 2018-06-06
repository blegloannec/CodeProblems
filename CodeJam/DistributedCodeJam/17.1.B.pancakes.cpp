#include <iostream>
#include "message.h"
#include "pancakes.h"
using namespace std;

typedef long long ll;

int id,nodes;
ll il,ir,S,res;

void local_computation() {
  res = 0;
  for (ll i=il; i<ir; ++i)
    if (i>0 && GetStackItem(i)<GetStackItem(i-1)) ++ res;
}

void recv_update() {
  Receive(id-1);
  res += GetLL(id-1);
}

void send_data() {
  PutLL(id+1,res);
  Send(id+1);
}

int main() {
  // init
  id = MyNodeId();
  nodes = NumberOfNodes();
  S = GetStackSize();
  if (S<nodes) {
    nodes = S;
    if (id>=nodes) return 0;
  }
  ll w = S%nodes==0 ? S/nodes : S/(nodes-1);
  il = id*w, ir = min((id+1)*w,S);
  
  // local computation
  local_computation();
  
  // update data taking into account the previous node data
  if (id>0) recv_update();

  // send data to next node
  if (id<nodes-1) send_data();
  else cout << res+1 << endl;
  
  return 0;
}
