#!/usr/bin/env python3

from math import exp

# constantes
eta = 0.5

# input
nb_in,nb_out,nb_layers,nb_tests,nb_examples,training_iterations = map(int,input().split())
nb_layers += 2
layer_size = [nb_in]+list(map(int,input().split()))+[nb_out]
tests = []
for _ in range(nb_tests):
    tests.append(list(map(int,input())))
examples = []
for _ in range(nb_examples):
    examples.append([list(map(int,x)) for x in input().split()])
    
# weights
Wtheta = [[0]*layer_size[i] for i in range(nb_layers)]
W = [[[0]*layer_size[i+1] for _ in range(layer_size[i])] for i in range(nb_layers-1)] 

def InitWeights():
    X = 1103527590
    for i in range(nb_layers-1):
        for v in range(layer_size[i+1]):
            for u in range(layer_size[i]):
                W[i][u][v] = X/(1<<31)
                X = (1103515245*X+12345)%(1<<31)
            Wtheta[i+1][v] = X/(1<<31)
            X = (1103515245*X+12345)%(1<<31)

# evaluation
def Evaluate(I):
    O = [I]
    for i in range(1,nb_layers):
        O.append([])
        for u in range(layer_size[i]):
            O[i].append(Wtheta[i][u])
            for v in range(layer_size[i-1]):
                O[i][u] += O[i-1][v]*W[i-1][v][u]
            O[i][u] = 1 / (1 + exp(-O[i][u]))
    return O

# backpropagation (descente de gradient)
def Backpropagation(O,T):
    Delta = [[] for _ in range(nb_layers)]
    for u in range(nb_out): # output nodes
        Delta[-1].append(O[-1][u]*(1-O[-1][u])*(O[-1][u]-T[u]))
    for i in range(nb_layers-2,0,-1): # hidden nodes
        for u in range(layer_size[i]):
            Delta[i].append(0)
            for v in range(layer_size[i+1]):
                Delta[i][u] += Delta[i+1][v]*W[i][u][v]
            Delta[i][u] *= O[i][u]*(1-O[i][u])
    for i in range(1,nb_layers):
        for v in range(layer_size[i]):
            for u in range(layer_size[i-1]):
                W[i-1][u][v] -= eta*Delta[i][v]*O[i-1][u]
            Wtheta[i][v] -= eta*Delta[i][v]

# training
def Training():
    for _ in range(training_iterations):
        for (I,T) in examples:
            Backpropagation(Evaluate(I),T)

def main():
    InitWeights()
    Training()
    for I in tests:
        O = Evaluate(I)
        print(''.join(str(round(x)) for x in O[-1]))

main()
