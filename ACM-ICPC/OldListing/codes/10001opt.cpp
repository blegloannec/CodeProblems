// ACM 10001
#include <cstdio>

#define MAX 32

int a,t;
char buff[MAX];

int det[256][16][2] = {
{{0,0},{3,0},{12,0},{15,0},{3,0},{3,0},{15,0},{15,0},{12,0},{15,0},{12,0},{15,0},{15,0},{15,0},{15,0},{15,0}},
{{0,0},{2,1},{12,0},{14,1},{3,0},{3,1},{15,0},{15,1},{12,0},{14,1},{12,0},{14,1},{15,0},{15,1},{15,0},{15,1}},
{{0,0},{1,2},{12,0},{13,2},{3,0},{3,2},{15,0},{15,2},{12,0},{13,2},{12,0},{13,2},{15,0},{15,2},{15,0},{15,2}},
{{0,0},{0,3},{12,0},{12,3},{3,0},{3,3},{15,0},{15,3},{12,0},{12,3},{12,0},{12,3},{15,0},{15,3},{15,0},{15,3}},
{{0,0},{3,0},{8,4},{11,4},{3,0},{3,0},{11,4},{11,4},{12,0},{15,0},{12,4},{15,4},{15,0},{15,0},{15,4},{15,4}},
{{0,0},{2,1},{8,4},{10,5},{3,0},{3,1},{11,4},{11,5},{12,0},{14,1},{12,4},{14,5},{15,0},{15,1},{15,4},{15,5}},
{{0,0},{1,2},{8,4},{9,6},{3,0},{3,2},{11,4},{11,6},{12,0},{13,2},{12,4},{13,6},{15,0},{15,2},{15,4},{15,6}},
{{0,0},{0,3},{8,4},{8,7},{3,0},{3,3},{11,4},{11,7},{12,0},{12,3},{12,4},{12,7},{15,0},{15,3},{15,4},{15,7}},
{{0,0},{3,0},{4,8},{7,8},{3,0},{3,0},{7,8},{7,8},{12,0},{15,0},{12,8},{15,8},{15,0},{15,0},{15,8},{15,8}},
{{0,0},{2,1},{4,8},{6,9},{3,0},{3,1},{7,8},{7,9},{12,0},{14,1},{12,8},{14,9},{15,0},{15,1},{15,8},{15,9}},
{{0,0},{1,2},{4,8},{5,10},{3,0},{3,2},{7,8},{7,10},{12,0},{13,2},{12,8},{13,10},{15,0},{15,2},{15,8},{15,10}},
{{0,0},{0,3},{4,8},{4,11},{3,0},{3,3},{7,8},{7,11},{12,0},{12,3},{12,8},{12,11},{15,0},{15,3},{15,8},{15,11}},
{{0,0},{3,0},{0,12},{3,12},{3,0},{3,0},{3,12},{3,12},{12,0},{15,0},{12,12},{15,12},{15,0},{15,0},{15,12},{15,12}},
{{0,0},{2,1},{0,12},{2,13},{3,0},{3,1},{3,12},{3,13},{12,0},{14,1},{12,12},{14,13},{15,0},{15,1},{15,12},{15,13}},
{{0,0},{1,2},{0,12},{1,14},{3,0},{3,2},{3,12},{3,14},{12,0},{13,2},{12,12},{13,14},{15,0},{15,2},{15,12},{15,14}},
{{0,0},{0,3},{0,12},{0,15},{3,0},{3,3},{3,12},{3,15},{12,0},{12,3},{12,12},{12,15},{15,0},{15,3},{15,12},{15,15}},
{{0,0},{3,0},{12,0},{15,0},{2,1},{3,1},{14,1},{15,1},{12,0},{15,0},{12,0},{15,0},{14,1},{15,1},{14,1},{15,1}},
{{0,0},{2,1},{12,0},{14,1},{2,1},{2,1},{14,1},{14,1},{12,0},{14,1},{12,0},{14,1},{14,1},{14,1},{14,1},{14,1}},
{{0,0},{1,2},{12,0},{13,2},{2,1},{3,3},{14,1},{15,3},{12,0},{13,2},{12,0},{13,2},{14,1},{15,3},{14,1},{15,3}},
{{0,0},{0,3},{12,0},{12,3},{2,1},{2,3},{14,1},{14,3},{12,0},{12,3},{12,0},{12,3},{14,1},{14,3},{14,1},{14,3}},
{{0,0},{3,0},{8,4},{11,4},{2,1},{3,1},{10,5},{11,5},{12,0},{15,0},{12,4},{15,4},{14,1},{15,1},{14,5},{15,5}},
{{0,0},{2,1},{8,4},{10,5},{2,1},{2,1},{10,5},{10,5},{12,0},{14,1},{12,4},{14,5},{14,1},{14,1},{14,5},{14,5}},
{{0,0},{1,2},{8,4},{9,6},{2,1},{3,3},{10,5},{11,7},{12,0},{13,2},{12,4},{13,6},{14,1},{15,3},{14,5},{15,7}},
{{0,0},{0,3},{8,4},{8,7},{2,1},{2,3},{10,5},{10,7},{12,0},{12,3},{12,4},{12,7},{14,1},{14,3},{14,5},{14,7}},
{{0,0},{3,0},{4,8},{7,8},{2,1},{3,1},{6,9},{7,9},{12,0},{15,0},{12,8},{15,8},{14,1},{15,1},{14,9},{15,9}},
{{0,0},{2,1},{4,8},{6,9},{2,1},{2,1},{6,9},{6,9},{12,0},{14,1},{12,8},{14,9},{14,1},{14,1},{14,9},{14,9}},
{{0,0},{1,2},{4,8},{5,10},{2,1},{3,3},{6,9},{7,11},{12,0},{13,2},{12,8},{13,10},{14,1},{15,3},{14,9},{15,11}},
{{0,0},{0,3},{4,8},{4,11},{2,1},{2,3},{6,9},{6,11},{12,0},{12,3},{12,8},{12,11},{14,1},{14,3},{14,9},{14,11}},
{{0,0},{3,0},{0,12},{3,12},{2,1},{3,1},{2,13},{3,13},{12,0},{15,0},{12,12},{15,12},{14,1},{15,1},{14,13},{15,13}},
{{0,0},{2,1},{0,12},{2,13},{2,1},{2,1},{2,13},{2,13},{12,0},{14,1},{12,12},{14,13},{14,1},{14,1},{14,13},{14,13}},
{{0,0},{1,2},{0,12},{1,14},{2,1},{3,3},{2,13},{3,15},{12,0},{13,2},{12,12},{13,14},{14,1},{15,3},{14,13},{15,15}},
{{0,0},{0,3},{0,12},{0,15},{2,1},{2,3},{2,13},{2,15},{12,0},{12,3},{12,12},{12,15},{14,1},{14,3},{14,13},{14,15}},
{{0,0},{3,0},{12,0},{15,0},{1,2},{3,2},{13,2},{15,2},{12,0},{15,0},{12,0},{15,0},{13,2},{15,2},{13,2},{15,2}},
{{0,0},{2,1},{12,0},{14,1},{1,2},{3,3},{13,2},{15,3},{12,0},{14,1},{12,0},{14,1},{13,2},{15,3},{13,2},{15,3}},
{{0,0},{1,2},{12,0},{13,2},{1,2},{1,2},{13,2},{13,2},{12,0},{13,2},{12,0},{13,2},{13,2},{13,2},{13,2},{13,2}},
{{0,0},{0,3},{12,0},{12,3},{1,2},{1,3},{13,2},{13,3},{12,0},{12,3},{12,0},{12,3},{13,2},{13,3},{13,2},{13,3}},
{{0,0},{3,0},{8,4},{11,4},{1,2},{3,2},{9,6},{11,6},{12,0},{15,0},{12,4},{15,4},{13,2},{15,2},{13,6},{15,6}},
{{0,0},{2,1},{8,4},{10,5},{1,2},{3,3},{9,6},{11,7},{12,0},{14,1},{12,4},{14,5},{13,2},{15,3},{13,6},{15,7}},
{{0,0},{1,2},{8,4},{9,6},{1,2},{1,2},{9,6},{9,6},{12,0},{13,2},{12,4},{13,6},{13,2},{13,2},{13,6},{13,6}},
{{0,0},{0,3},{8,4},{8,7},{1,2},{1,3},{9,6},{9,7},{12,0},{12,3},{12,4},{12,7},{13,2},{13,3},{13,6},{13,7}},
{{0,0},{3,0},{4,8},{7,8},{1,2},{3,2},{5,10},{7,10},{12,0},{15,0},{12,8},{15,8},{13,2},{15,2},{13,10},{15,10}},
{{0,0},{2,1},{4,8},{6,9},{1,2},{3,3},{5,10},{7,11},{12,0},{14,1},{12,8},{14,9},{13,2},{15,3},{13,10},{15,11}},
{{0,0},{1,2},{4,8},{5,10},{1,2},{1,2},{5,10},{5,10},{12,0},{13,2},{12,8},{13,10},{13,2},{13,2},{13,10},{13,10}},
{{0,0},{0,3},{4,8},{4,11},{1,2},{1,3},{5,10},{5,11},{12,0},{12,3},{12,8},{12,11},{13,2},{13,3},{13,10},{13,11}},
{{0,0},{3,0},{0,12},{3,12},{1,2},{3,2},{1,14},{3,14},{12,0},{15,0},{12,12},{15,12},{13,2},{15,2},{13,14},{15,14}},
{{0,0},{2,1},{0,12},{2,13},{1,2},{3,3},{1,14},{3,15},{12,0},{14,1},{12,12},{14,13},{13,2},{15,3},{13,14},{15,15}},
{{0,0},{1,2},{0,12},{1,14},{1,2},{1,2},{1,14},{1,14},{12,0},{13,2},{12,12},{13,14},{13,2},{13,2},{13,14},{13,14}},
{{0,0},{0,3},{0,12},{0,15},{1,2},{1,3},{1,14},{1,15},{12,0},{12,3},{12,12},{12,15},{13,2},{13,3},{13,14},{13,15}},
{{0,0},{3,0},{12,0},{15,0},{0,3},{3,3},{12,3},{15,3},{12,0},{15,0},{12,0},{15,0},{12,3},{15,3},{12,3},{15,3}},
{{0,0},{2,1},{12,0},{14,1},{0,3},{2,3},{12,3},{14,3},{12,0},{14,1},{12,0},{14,1},{12,3},{14,3},{12,3},{14,3}},
{{0,0},{1,2},{12,0},{13,2},{0,3},{1,3},{12,3},{13,3},{12,0},{13,2},{12,0},{13,2},{12,3},{13,3},{12,3},{13,3}},
{{0,0},{0,3},{12,0},{12,3},{0,3},{0,3},{12,3},{12,3},{12,0},{12,3},{12,0},{12,3},{12,3},{12,3},{12,3},{12,3}},
{{0,0},{3,0},{8,4},{11,4},{0,3},{3,3},{8,7},{11,7},{12,0},{15,0},{12,4},{15,4},{12,3},{15,3},{12,7},{15,7}},
{{0,0},{2,1},{8,4},{10,5},{0,3},{2,3},{8,7},{10,7},{12,0},{14,1},{12,4},{14,5},{12,3},{14,3},{12,7},{14,7}},
{{0,0},{1,2},{8,4},{9,6},{0,3},{1,3},{8,7},{9,7},{12,0},{13,2},{12,4},{13,6},{12,3},{13,3},{12,7},{13,7}},
{{0,0},{0,3},{8,4},{8,7},{0,3},{0,3},{8,7},{8,7},{12,0},{12,3},{12,4},{12,7},{12,3},{12,3},{12,7},{12,7}},
{{0,0},{3,0},{4,8},{7,8},{0,3},{3,3},{4,11},{7,11},{12,0},{15,0},{12,8},{15,8},{12,3},{15,3},{12,11},{15,11}},
{{0,0},{2,1},{4,8},{6,9},{0,3},{2,3},{4,11},{6,11},{12,0},{14,1},{12,8},{14,9},{12,3},{14,3},{12,11},{14,11}},
{{0,0},{1,2},{4,8},{5,10},{0,3},{1,3},{4,11},{5,11},{12,0},{13,2},{12,8},{13,10},{12,3},{13,3},{12,11},{13,11}},
{{0,0},{0,3},{4,8},{4,11},{0,3},{0,3},{4,11},{4,11},{12,0},{12,3},{12,8},{12,11},{12,3},{12,3},{12,11},{12,11}},
{{0,0},{3,0},{0,12},{3,12},{0,3},{3,3},{0,15},{3,15},{12,0},{15,0},{12,12},{15,12},{12,3},{15,3},{12,15},{15,15}},
{{0,0},{2,1},{0,12},{2,13},{0,3},{2,3},{0,15},{2,15},{12,0},{14,1},{12,12},{14,13},{12,3},{14,3},{12,15},{14,15}},
{{0,0},{1,2},{0,12},{1,14},{0,3},{1,3},{0,15},{1,15},{12,0},{13,2},{12,12},{13,14},{12,3},{13,3},{12,15},{13,15}},
{{0,0},{0,3},{0,12},{0,15},{0,3},{0,3},{0,15},{0,15},{12,0},{12,3},{12,12},{12,15},{12,3},{12,3},{12,15},{12,15}},
{{0,0},{3,0},{12,0},{15,0},{3,0},{3,0},{15,0},{15,0},{8,4},{11,4},{12,4},{15,4},{11,4},{11,4},{15,4},{15,4}},
{{0,0},{2,1},{12,0},{14,1},{3,0},{3,1},{15,0},{15,1},{8,4},{10,5},{12,4},{14,5},{11,4},{11,5},{15,4},{15,5}},
{{0,0},{1,2},{12,0},{13,2},{3,0},{3,2},{15,0},{15,2},{8,4},{9,6},{12,4},{13,6},{11,4},{11,6},{15,4},{15,6}},
{{0,0},{0,3},{12,0},{12,3},{3,0},{3,3},{15,0},{15,3},{8,4},{8,7},{12,4},{12,7},{11,4},{11,7},{15,4},{15,7}},
{{0,0},{3,0},{8,4},{11,4},{3,0},{3,0},{11,4},{11,4},{8,4},{11,4},{8,4},{11,4},{11,4},{11,4},{11,4},{11,4}},
{{0,0},{2,1},{8,4},{10,5},{3,0},{3,1},{11,4},{11,5},{8,4},{10,5},{8,4},{10,5},{11,4},{11,5},{11,4},{11,5}},
{{0,0},{1,2},{8,4},{9,6},{3,0},{3,2},{11,4},{11,6},{8,4},{9,6},{8,4},{9,6},{11,4},{11,6},{11,4},{11,6}},
{{0,0},{0,3},{8,4},{8,7},{3,0},{3,3},{11,4},{11,7},{8,4},{8,7},{8,4},{8,7},{11,4},{11,7},{11,4},{11,7}},
{{0,0},{3,0},{4,8},{7,8},{3,0},{3,0},{7,8},{7,8},{8,4},{11,4},{12,12},{15,12},{11,4},{11,4},{15,12},{15,12}},
{{0,0},{2,1},{4,8},{6,9},{3,0},{3,1},{7,8},{7,9},{8,4},{10,5},{12,12},{14,13},{11,4},{11,5},{15,12},{15,13}},
{{0,0},{1,2},{4,8},{5,10},{3,0},{3,2},{7,8},{7,10},{8,4},{9,6},{12,12},{13,14},{11,4},{11,6},{15,12},{15,14}},
{{0,0},{0,3},{4,8},{4,11},{3,0},{3,3},{7,8},{7,11},{8,4},{8,7},{12,12},{12,15},{11,4},{11,7},{15,12},{15,15}},
{{0,0},{3,0},{0,12},{3,12},{3,0},{3,0},{3,12},{3,12},{8,4},{11,4},{8,12},{11,12},{11,4},{11,4},{11,12},{11,12}},
{{0,0},{2,1},{0,12},{2,13},{3,0},{3,1},{3,12},{3,13},{8,4},{10,5},{8,12},{10,13},{11,4},{11,5},{11,12},{11,13}},
{{0,0},{1,2},{0,12},{1,14},{3,0},{3,2},{3,12},{3,14},{8,4},{9,6},{8,12},{9,14},{11,4},{11,6},{11,12},{11,14}},
{{0,0},{0,3},{0,12},{0,15},{3,0},{3,3},{3,12},{3,15},{8,4},{8,7},{8,12},{8,15},{11,4},{11,7},{11,12},{11,15}},
{{0,0},{3,0},{12,0},{15,0},{2,1},{3,1},{14,1},{15,1},{8,4},{11,4},{12,4},{15,4},{10,5},{11,5},{14,5},{15,5}},
{{0,0},{2,1},{12,0},{14,1},{2,1},{2,1},{14,1},{14,1},{8,4},{10,5},{12,4},{14,5},{10,5},{10,5},{14,5},{14,5}},
{{0,0},{1,2},{12,0},{13,2},{2,1},{3,3},{14,1},{15,3},{8,4},{9,6},{12,4},{13,6},{10,5},{11,7},{14,5},{15,7}},
{{0,0},{0,3},{12,0},{12,3},{2,1},{2,3},{14,1},{14,3},{8,4},{8,7},{12,4},{12,7},{10,5},{10,7},{14,5},{14,7}},
{{0,0},{3,0},{8,4},{11,4},{2,1},{3,1},{10,5},{11,5},{8,4},{11,4},{8,4},{11,4},{10,5},{11,5},{10,5},{11,5}},
{{0,0},{2,1},{8,4},{10,5},{2,1},{2,1},{10,5},{10,5},{8,4},{10,5},{8,4},{10,5},{10,5},{10,5},{10,5},{10,5}},
{{0,0},{1,2},{8,4},{9,6},{2,1},{3,3},{10,5},{11,7},{8,4},{9,6},{8,4},{9,6},{10,5},{11,7},{10,5},{11,7}},
{{0,0},{0,3},{8,4},{8,7},{2,1},{2,3},{10,5},{10,7},{8,4},{8,7},{8,4},{8,7},{10,5},{10,7},{10,5},{10,7}},
{{0,0},{3,0},{4,8},{7,8},{2,1},{3,1},{6,9},{7,9},{8,4},{11,4},{12,12},{15,12},{10,5},{11,5},{14,13},{15,13}},
{{0,0},{2,1},{4,8},{6,9},{2,1},{2,1},{6,9},{6,9},{8,4},{10,5},{12,12},{14,13},{10,5},{10,5},{14,13},{14,13}},
{{0,0},{1,2},{4,8},{5,10},{2,1},{3,3},{6,9},{7,11},{8,4},{9,6},{12,12},{13,14},{10,5},{11,7},{14,13},{15,15}},
{{0,0},{0,3},{4,8},{4,11},{2,1},{2,3},{6,9},{6,11},{8,4},{8,7},{12,12},{12,15},{10,5},{10,7},{14,13},{14,15}},
{{0,0},{3,0},{0,12},{3,12},{2,1},{3,1},{2,13},{3,13},{8,4},{11,4},{8,12},{11,12},{10,5},{11,5},{10,13},{11,13}},
{{0,0},{2,1},{0,12},{2,13},{2,1},{2,1},{2,13},{2,13},{8,4},{10,5},{8,12},{10,13},{10,5},{10,5},{10,13},{10,13}},
{{0,0},{1,2},{0,12},{1,14},{2,1},{3,3},{2,13},{3,15},{8,4},{9,6},{8,12},{9,14},{10,5},{11,7},{10,13},{11,15}},
{{0,0},{0,3},{0,12},{0,15},{2,1},{2,3},{2,13},{2,15},{8,4},{8,7},{8,12},{8,15},{10,5},{10,7},{10,13},{10,15}},
{{0,0},{3,0},{12,0},{15,0},{1,2},{3,2},{13,2},{15,2},{8,4},{11,4},{12,4},{15,4},{9,6},{11,6},{13,6},{15,6}},
{{0,0},{2,1},{12,0},{14,1},{1,2},{3,3},{13,2},{15,3},{8,4},{10,5},{12,4},{14,5},{9,6},{11,7},{13,6},{15,7}},
{{0,0},{1,2},{12,0},{13,2},{1,2},{1,2},{13,2},{13,2},{8,4},{9,6},{12,4},{13,6},{9,6},{9,6},{13,6},{13,6}},
{{0,0},{0,3},{12,0},{12,3},{1,2},{1,3},{13,2},{13,3},{8,4},{8,7},{12,4},{12,7},{9,6},{9,7},{13,6},{13,7}},
{{0,0},{3,0},{8,4},{11,4},{1,2},{3,2},{9,6},{11,6},{8,4},{11,4},{8,4},{11,4},{9,6},{11,6},{9,6},{11,6}},
{{0,0},{2,1},{8,4},{10,5},{1,2},{3,3},{9,6},{11,7},{8,4},{10,5},{8,4},{10,5},{9,6},{11,7},{9,6},{11,7}},
{{0,0},{1,2},{8,4},{9,6},{1,2},{1,2},{9,6},{9,6},{8,4},{9,6},{8,4},{9,6},{9,6},{9,6},{9,6},{9,6}},
{{0,0},{0,3},{8,4},{8,7},{1,2},{1,3},{9,6},{9,7},{8,4},{8,7},{8,4},{8,7},{9,6},{9,7},{9,6},{9,7}},
{{0,0},{3,0},{4,8},{7,8},{1,2},{3,2},{5,10},{7,10},{8,4},{11,4},{12,12},{15,12},{9,6},{11,6},{13,14},{15,14}},
{{0,0},{2,1},{4,8},{6,9},{1,2},{3,3},{5,10},{7,11},{8,4},{10,5},{12,12},{14,13},{9,6},{11,7},{13,14},{15,15}},
{{0,0},{1,2},{4,8},{5,10},{1,2},{1,2},{5,10},{5,10},{8,4},{9,6},{12,12},{13,14},{9,6},{9,6},{13,14},{13,14}},
{{0,0},{0,3},{4,8},{4,11},{1,2},{1,3},{5,10},{5,11},{8,4},{8,7},{12,12},{12,15},{9,6},{9,7},{13,14},{13,15}},
{{0,0},{3,0},{0,12},{3,12},{1,2},{3,2},{1,14},{3,14},{8,4},{11,4},{8,12},{11,12},{9,6},{11,6},{9,14},{11,14}},
{{0,0},{2,1},{0,12},{2,13},{1,2},{3,3},{1,14},{3,15},{8,4},{10,5},{8,12},{10,13},{9,6},{11,7},{9,14},{11,15}},
{{0,0},{1,2},{0,12},{1,14},{1,2},{1,2},{1,14},{1,14},{8,4},{9,6},{8,12},{9,14},{9,6},{9,6},{9,14},{9,14}},
{{0,0},{0,3},{0,12},{0,15},{1,2},{1,3},{1,14},{1,15},{8,4},{8,7},{8,12},{8,15},{9,6},{9,7},{9,14},{9,15}},
{{0,0},{3,0},{12,0},{15,0},{0,3},{3,3},{12,3},{15,3},{8,4},{11,4},{12,4},{15,4},{8,7},{11,7},{12,7},{15,7}},
{{0,0},{2,1},{12,0},{14,1},{0,3},{2,3},{12,3},{14,3},{8,4},{10,5},{12,4},{14,5},{8,7},{10,7},{12,7},{14,7}},
{{0,0},{1,2},{12,0},{13,2},{0,3},{1,3},{12,3},{13,3},{8,4},{9,6},{12,4},{13,6},{8,7},{9,7},{12,7},{13,7}},
{{0,0},{0,3},{12,0},{12,3},{0,3},{0,3},{12,3},{12,3},{8,4},{8,7},{12,4},{12,7},{8,7},{8,7},{12,7},{12,7}},
{{0,0},{3,0},{8,4},{11,4},{0,3},{3,3},{8,7},{11,7},{8,4},{11,4},{8,4},{11,4},{8,7},{11,7},{8,7},{11,7}},
{{0,0},{2,1},{8,4},{10,5},{0,3},{2,3},{8,7},{10,7},{8,4},{10,5},{8,4},{10,5},{8,7},{10,7},{8,7},{10,7}},
{{0,0},{1,2},{8,4},{9,6},{0,3},{1,3},{8,7},{9,7},{8,4},{9,6},{8,4},{9,6},{8,7},{9,7},{8,7},{9,7}},
{{0,0},{0,3},{8,4},{8,7},{0,3},{0,3},{8,7},{8,7},{8,4},{8,7},{8,4},{8,7},{8,7},{8,7},{8,7},{8,7}},
{{0,0},{3,0},{4,8},{7,8},{0,3},{3,3},{4,11},{7,11},{8,4},{11,4},{12,12},{15,12},{8,7},{11,7},{12,15},{15,15}},
{{0,0},{2,1},{4,8},{6,9},{0,3},{2,3},{4,11},{6,11},{8,4},{10,5},{12,12},{14,13},{8,7},{10,7},{12,15},{14,15}},
{{0,0},{1,2},{4,8},{5,10},{0,3},{1,3},{4,11},{5,11},{8,4},{9,6},{12,12},{13,14},{8,7},{9,7},{12,15},{13,15}},
{{0,0},{0,3},{4,8},{4,11},{0,3},{0,3},{4,11},{4,11},{8,4},{8,7},{12,12},{12,15},{8,7},{8,7},{12,15},{12,15}},
{{0,0},{3,0},{0,12},{3,12},{0,3},{3,3},{0,15},{3,15},{8,4},{11,4},{8,12},{11,12},{8,7},{11,7},{8,15},{11,15}},
{{0,0},{2,1},{0,12},{2,13},{0,3},{2,3},{0,15},{2,15},{8,4},{10,5},{8,12},{10,13},{8,7},{10,7},{8,15},{10,15}},
{{0,0},{1,2},{0,12},{1,14},{0,3},{1,3},{0,15},{1,15},{8,4},{9,6},{8,12},{9,14},{8,7},{9,7},{8,15},{9,15}},
{{0,0},{0,3},{0,12},{0,15},{0,3},{0,3},{0,15},{0,15},{8,4},{8,7},{8,12},{8,15},{8,7},{8,7},{8,15},{8,15}},
{{0,0},{3,0},{12,0},{15,0},{3,0},{3,0},{15,0},{15,0},{4,8},{7,8},{12,8},{15,8},{7,8},{7,8},{15,8},{15,8}},
{{0,0},{2,1},{12,0},{14,1},{3,0},{3,1},{15,0},{15,1},{4,8},{6,9},{12,8},{14,9},{7,8},{7,9},{15,8},{15,9}},
{{0,0},{1,2},{12,0},{13,2},{3,0},{3,2},{15,0},{15,2},{4,8},{5,10},{12,8},{13,10},{7,8},{7,10},{15,8},{15,10}},
{{0,0},{0,3},{12,0},{12,3},{3,0},{3,3},{15,0},{15,3},{4,8},{4,11},{12,8},{12,11},{7,8},{7,11},{15,8},{15,11}},
{{0,0},{3,0},{8,4},{11,4},{3,0},{3,0},{11,4},{11,4},{4,8},{7,8},{12,12},{15,12},{7,8},{7,8},{15,12},{15,12}},
{{0,0},{2,1},{8,4},{10,5},{3,0},{3,1},{11,4},{11,5},{4,8},{6,9},{12,12},{14,13},{7,8},{7,9},{15,12},{15,13}},
{{0,0},{1,2},{8,4},{9,6},{3,0},{3,2},{11,4},{11,6},{4,8},{5,10},{12,12},{13,14},{7,8},{7,10},{15,12},{15,14}},
{{0,0},{0,3},{8,4},{8,7},{3,0},{3,3},{11,4},{11,7},{4,8},{4,11},{12,12},{12,15},{7,8},{7,11},{15,12},{15,15}},
{{0,0},{3,0},{4,8},{7,8},{3,0},{3,0},{7,8},{7,8},{4,8},{7,8},{4,8},{7,8},{7,8},{7,8},{7,8},{7,8}},
{{0,0},{2,1},{4,8},{6,9},{3,0},{3,1},{7,8},{7,9},{4,8},{6,9},{4,8},{6,9},{7,8},{7,9},{7,8},{7,9}},
{{0,0},{1,2},{4,8},{5,10},{3,0},{3,2},{7,8},{7,10},{4,8},{5,10},{4,8},{5,10},{7,8},{7,10},{7,8},{7,10}},
{{0,0},{0,3},{4,8},{4,11},{3,0},{3,3},{7,8},{7,11},{4,8},{4,11},{4,8},{4,11},{7,8},{7,11},{7,8},{7,11}},
{{0,0},{3,0},{0,12},{3,12},{3,0},{3,0},{3,12},{3,12},{4,8},{7,8},{4,12},{7,12},{7,8},{7,8},{7,12},{7,12}},
{{0,0},{2,1},{0,12},{2,13},{3,0},{3,1},{3,12},{3,13},{4,8},{6,9},{4,12},{6,13},{7,8},{7,9},{7,12},{7,13}},
{{0,0},{1,2},{0,12},{1,14},{3,0},{3,2},{3,12},{3,14},{4,8},{5,10},{4,12},{5,14},{7,8},{7,10},{7,12},{7,14}},
{{0,0},{0,3},{0,12},{0,15},{3,0},{3,3},{3,12},{3,15},{4,8},{4,11},{4,12},{4,15},{7,8},{7,11},{7,12},{7,15}},
{{0,0},{3,0},{12,0},{15,0},{2,1},{3,1},{14,1},{15,1},{4,8},{7,8},{12,8},{15,8},{6,9},{7,9},{14,9},{15,9}},
{{0,0},{2,1},{12,0},{14,1},{2,1},{2,1},{14,1},{14,1},{4,8},{6,9},{12,8},{14,9},{6,9},{6,9},{14,9},{14,9}},
{{0,0},{1,2},{12,0},{13,2},{2,1},{3,3},{14,1},{15,3},{4,8},{5,10},{12,8},{13,10},{6,9},{7,11},{14,9},{15,11}},
{{0,0},{0,3},{12,0},{12,3},{2,1},{2,3},{14,1},{14,3},{4,8},{4,11},{12,8},{12,11},{6,9},{6,11},{14,9},{14,11}},
{{0,0},{3,0},{8,4},{11,4},{2,1},{3,1},{10,5},{11,5},{4,8},{7,8},{12,12},{15,12},{6,9},{7,9},{14,13},{15,13}},
{{0,0},{2,1},{8,4},{10,5},{2,1},{2,1},{10,5},{10,5},{4,8},{6,9},{12,12},{14,13},{6,9},{6,9},{14,13},{14,13}},
{{0,0},{1,2},{8,4},{9,6},{2,1},{3,3},{10,5},{11,7},{4,8},{5,10},{12,12},{13,14},{6,9},{7,11},{14,13},{15,15}},
{{0,0},{0,3},{8,4},{8,7},{2,1},{2,3},{10,5},{10,7},{4,8},{4,11},{12,12},{12,15},{6,9},{6,11},{14,13},{14,15}},
{{0,0},{3,0},{4,8},{7,8},{2,1},{3,1},{6,9},{7,9},{4,8},{7,8},{4,8},{7,8},{6,9},{7,9},{6,9},{7,9}},
{{0,0},{2,1},{4,8},{6,9},{2,1},{2,1},{6,9},{6,9},{4,8},{6,9},{4,8},{6,9},{6,9},{6,9},{6,9},{6,9}},
{{0,0},{1,2},{4,8},{5,10},{2,1},{3,3},{6,9},{7,11},{4,8},{5,10},{4,8},{5,10},{6,9},{7,11},{6,9},{7,11}},
{{0,0},{0,3},{4,8},{4,11},{2,1},{2,3},{6,9},{6,11},{4,8},{4,11},{4,8},{4,11},{6,9},{6,11},{6,9},{6,11}},
{{0,0},{3,0},{0,12},{3,12},{2,1},{3,1},{2,13},{3,13},{4,8},{7,8},{4,12},{7,12},{6,9},{7,9},{6,13},{7,13}},
{{0,0},{2,1},{0,12},{2,13},{2,1},{2,1},{2,13},{2,13},{4,8},{6,9},{4,12},{6,13},{6,9},{6,9},{6,13},{6,13}},
{{0,0},{1,2},{0,12},{1,14},{2,1},{3,3},{2,13},{3,15},{4,8},{5,10},{4,12},{5,14},{6,9},{7,11},{6,13},{7,15}},
{{0,0},{0,3},{0,12},{0,15},{2,1},{2,3},{2,13},{2,15},{4,8},{4,11},{4,12},{4,15},{6,9},{6,11},{6,13},{6,15}},
{{0,0},{3,0},{12,0},{15,0},{1,2},{3,2},{13,2},{15,2},{4,8},{7,8},{12,8},{15,8},{5,10},{7,10},{13,10},{15,10}},
{{0,0},{2,1},{12,0},{14,1},{1,2},{3,3},{13,2},{15,3},{4,8},{6,9},{12,8},{14,9},{5,10},{7,11},{13,10},{15,11}},
{{0,0},{1,2},{12,0},{13,2},{1,2},{1,2},{13,2},{13,2},{4,8},{5,10},{12,8},{13,10},{5,10},{5,10},{13,10},{13,10}},
{{0,0},{0,3},{12,0},{12,3},{1,2},{1,3},{13,2},{13,3},{4,8},{4,11},{12,8},{12,11},{5,10},{5,11},{13,10},{13,11}},
{{0,0},{3,0},{8,4},{11,4},{1,2},{3,2},{9,6},{11,6},{4,8},{7,8},{12,12},{15,12},{5,10},{7,10},{13,14},{15,14}},
{{0,0},{2,1},{8,4},{10,5},{1,2},{3,3},{9,6},{11,7},{4,8},{6,9},{12,12},{14,13},{5,10},{7,11},{13,14},{15,15}},
{{0,0},{1,2},{8,4},{9,6},{1,2},{1,2},{9,6},{9,6},{4,8},{5,10},{12,12},{13,14},{5,10},{5,10},{13,14},{13,14}},
{{0,0},{0,3},{8,4},{8,7},{1,2},{1,3},{9,6},{9,7},{4,8},{4,11},{12,12},{12,15},{5,10},{5,11},{13,14},{13,15}},
{{0,0},{3,0},{4,8},{7,8},{1,2},{3,2},{5,10},{7,10},{4,8},{7,8},{4,8},{7,8},{5,10},{7,10},{5,10},{7,10}},
{{0,0},{2,1},{4,8},{6,9},{1,2},{3,3},{5,10},{7,11},{4,8},{6,9},{4,8},{6,9},{5,10},{7,11},{5,10},{7,11}},
{{0,0},{1,2},{4,8},{5,10},{1,2},{1,2},{5,10},{5,10},{4,8},{5,10},{4,8},{5,10},{5,10},{5,10},{5,10},{5,10}},
{{0,0},{0,3},{4,8},{4,11},{1,2},{1,3},{5,10},{5,11},{4,8},{4,11},{4,8},{4,11},{5,10},{5,11},{5,10},{5,11}},
{{0,0},{3,0},{0,12},{3,12},{1,2},{3,2},{1,14},{3,14},{4,8},{7,8},{4,12},{7,12},{5,10},{7,10},{5,14},{7,14}},
{{0,0},{2,1},{0,12},{2,13},{1,2},{3,3},{1,14},{3,15},{4,8},{6,9},{4,12},{6,13},{5,10},{7,11},{5,14},{7,15}},
{{0,0},{1,2},{0,12},{1,14},{1,2},{1,2},{1,14},{1,14},{4,8},{5,10},{4,12},{5,14},{5,10},{5,10},{5,14},{5,14}},
{{0,0},{0,3},{0,12},{0,15},{1,2},{1,3},{1,14},{1,15},{4,8},{4,11},{4,12},{4,15},{5,10},{5,11},{5,14},{5,15}},
{{0,0},{3,0},{12,0},{15,0},{0,3},{3,3},{12,3},{15,3},{4,8},{7,8},{12,8},{15,8},{4,11},{7,11},{12,11},{15,11}},
{{0,0},{2,1},{12,0},{14,1},{0,3},{2,3},{12,3},{14,3},{4,8},{6,9},{12,8},{14,9},{4,11},{6,11},{12,11},{14,11}},
{{0,0},{1,2},{12,0},{13,2},{0,3},{1,3},{12,3},{13,3},{4,8},{5,10},{12,8},{13,10},{4,11},{5,11},{12,11},{13,11}},
{{0,0},{0,3},{12,0},{12,3},{0,3},{0,3},{12,3},{12,3},{4,8},{4,11},{12,8},{12,11},{4,11},{4,11},{12,11},{12,11}},
{{0,0},{3,0},{8,4},{11,4},{0,3},{3,3},{8,7},{11,7},{4,8},{7,8},{12,12},{15,12},{4,11},{7,11},{12,15},{15,15}},
{{0,0},{2,1},{8,4},{10,5},{0,3},{2,3},{8,7},{10,7},{4,8},{6,9},{12,12},{14,13},{4,11},{6,11},{12,15},{14,15}},
{{0,0},{1,2},{8,4},{9,6},{0,3},{1,3},{8,7},{9,7},{4,8},{5,10},{12,12},{13,14},{4,11},{5,11},{12,15},{13,15}},
{{0,0},{0,3},{8,4},{8,7},{0,3},{0,3},{8,7},{8,7},{4,8},{4,11},{12,12},{12,15},{4,11},{4,11},{12,15},{12,15}},
{{0,0},{3,0},{4,8},{7,8},{0,3},{3,3},{4,11},{7,11},{4,8},{7,8},{4,8},{7,8},{4,11},{7,11},{4,11},{7,11}},
{{0,0},{2,1},{4,8},{6,9},{0,3},{2,3},{4,11},{6,11},{4,8},{6,9},{4,8},{6,9},{4,11},{6,11},{4,11},{6,11}},
{{0,0},{1,2},{4,8},{5,10},{0,3},{1,3},{4,11},{5,11},{4,8},{5,10},{4,8},{5,10},{4,11},{5,11},{4,11},{5,11}},
{{0,0},{0,3},{4,8},{4,11},{0,3},{0,3},{4,11},{4,11},{4,8},{4,11},{4,8},{4,11},{4,11},{4,11},{4,11},{4,11}},
{{0,0},{3,0},{0,12},{3,12},{0,3},{3,3},{0,15},{3,15},{4,8},{7,8},{4,12},{7,12},{4,11},{7,11},{4,15},{7,15}},
{{0,0},{2,1},{0,12},{2,13},{0,3},{2,3},{0,15},{2,15},{4,8},{6,9},{4,12},{6,13},{4,11},{6,11},{4,15},{6,15}},
{{0,0},{1,2},{0,12},{1,14},{0,3},{1,3},{0,15},{1,15},{4,8},{5,10},{4,12},{5,14},{4,11},{5,11},{4,15},{5,15}},
{{0,0},{0,3},{0,12},{0,15},{0,3},{0,3},{0,15},{0,15},{4,8},{4,11},{4,12},{4,15},{4,11},{4,11},{4,15},{4,15}},
{{0,0},{3,0},{12,0},{15,0},{3,0},{3,0},{15,0},{15,0},{0,12},{3,12},{12,12},{15,12},{3,12},{3,12},{15,12},{15,12}},
{{0,0},{2,1},{12,0},{14,1},{3,0},{3,1},{15,0},{15,1},{0,12},{2,13},{12,12},{14,13},{3,12},{3,13},{15,12},{15,13}},
{{0,0},{1,2},{12,0},{13,2},{3,0},{3,2},{15,0},{15,2},{0,12},{1,14},{12,12},{13,14},{3,12},{3,14},{15,12},{15,14}},
{{0,0},{0,3},{12,0},{12,3},{3,0},{3,3},{15,0},{15,3},{0,12},{0,15},{12,12},{12,15},{3,12},{3,15},{15,12},{15,15}},
{{0,0},{3,0},{8,4},{11,4},{3,0},{3,0},{11,4},{11,4},{0,12},{3,12},{8,12},{11,12},{3,12},{3,12},{11,12},{11,12}},
{{0,0},{2,1},{8,4},{10,5},{3,0},{3,1},{11,4},{11,5},{0,12},{2,13},{8,12},{10,13},{3,12},{3,13},{11,12},{11,13}},
{{0,0},{1,2},{8,4},{9,6},{3,0},{3,2},{11,4},{11,6},{0,12},{1,14},{8,12},{9,14},{3,12},{3,14},{11,12},{11,14}},
{{0,0},{0,3},{8,4},{8,7},{3,0},{3,3},{11,4},{11,7},{0,12},{0,15},{8,12},{8,15},{3,12},{3,15},{11,12},{11,15}},
{{0,0},{3,0},{4,8},{7,8},{3,0},{3,0},{7,8},{7,8},{0,12},{3,12},{4,12},{7,12},{3,12},{3,12},{7,12},{7,12}},
{{0,0},{2,1},{4,8},{6,9},{3,0},{3,1},{7,8},{7,9},{0,12},{2,13},{4,12},{6,13},{3,12},{3,13},{7,12},{7,13}},
{{0,0},{1,2},{4,8},{5,10},{3,0},{3,2},{7,8},{7,10},{0,12},{1,14},{4,12},{5,14},{3,12},{3,14},{7,12},{7,14}},
{{0,0},{0,3},{4,8},{4,11},{3,0},{3,3},{7,8},{7,11},{0,12},{0,15},{4,12},{4,15},{3,12},{3,15},{7,12},{7,15}},
{{0,0},{3,0},{0,12},{3,12},{3,0},{3,0},{3,12},{3,12},{0,12},{3,12},{0,12},{3,12},{3,12},{3,12},{3,12},{3,12}},
{{0,0},{2,1},{0,12},{2,13},{3,0},{3,1},{3,12},{3,13},{0,12},{2,13},{0,12},{2,13},{3,12},{3,13},{3,12},{3,13}},
{{0,0},{1,2},{0,12},{1,14},{3,0},{3,2},{3,12},{3,14},{0,12},{1,14},{0,12},{1,14},{3,12},{3,14},{3,12},{3,14}},
{{0,0},{0,3},{0,12},{0,15},{3,0},{3,3},{3,12},{3,15},{0,12},{0,15},{0,12},{0,15},{3,12},{3,15},{3,12},{3,15}},
{{0,0},{3,0},{12,0},{15,0},{2,1},{3,1},{14,1},{15,1},{0,12},{3,12},{12,12},{15,12},{2,13},{3,13},{14,13},{15,13}},
{{0,0},{2,1},{12,0},{14,1},{2,1},{2,1},{14,1},{14,1},{0,12},{2,13},{12,12},{14,13},{2,13},{2,13},{14,13},{14,13}},
{{0,0},{1,2},{12,0},{13,2},{2,1},{3,3},{14,1},{15,3},{0,12},{1,14},{12,12},{13,14},{2,13},{3,15},{14,13},{15,15}},
{{0,0},{0,3},{12,0},{12,3},{2,1},{2,3},{14,1},{14,3},{0,12},{0,15},{12,12},{12,15},{2,13},{2,15},{14,13},{14,15}},
{{0,0},{3,0},{8,4},{11,4},{2,1},{3,1},{10,5},{11,5},{0,12},{3,12},{8,12},{11,12},{2,13},{3,13},{10,13},{11,13}},
{{0,0},{2,1},{8,4},{10,5},{2,1},{2,1},{10,5},{10,5},{0,12},{2,13},{8,12},{10,13},{2,13},{2,13},{10,13},{10,13}},
{{0,0},{1,2},{8,4},{9,6},{2,1},{3,3},{10,5},{11,7},{0,12},{1,14},{8,12},{9,14},{2,13},{3,15},{10,13},{11,15}},
{{0,0},{0,3},{8,4},{8,7},{2,1},{2,3},{10,5},{10,7},{0,12},{0,15},{8,12},{8,15},{2,13},{2,15},{10,13},{10,15}},
{{0,0},{3,0},{4,8},{7,8},{2,1},{3,1},{6,9},{7,9},{0,12},{3,12},{4,12},{7,12},{2,13},{3,13},{6,13},{7,13}},
{{0,0},{2,1},{4,8},{6,9},{2,1},{2,1},{6,9},{6,9},{0,12},{2,13},{4,12},{6,13},{2,13},{2,13},{6,13},{6,13}},
{{0,0},{1,2},{4,8},{5,10},{2,1},{3,3},{6,9},{7,11},{0,12},{1,14},{4,12},{5,14},{2,13},{3,15},{6,13},{7,15}},
{{0,0},{0,3},{4,8},{4,11},{2,1},{2,3},{6,9},{6,11},{0,12},{0,15},{4,12},{4,15},{2,13},{2,15},{6,13},{6,15}},
{{0,0},{3,0},{0,12},{3,12},{2,1},{3,1},{2,13},{3,13},{0,12},{3,12},{0,12},{3,12},{2,13},{3,13},{2,13},{3,13}},
{{0,0},{2,1},{0,12},{2,13},{2,1},{2,1},{2,13},{2,13},{0,12},{2,13},{0,12},{2,13},{2,13},{2,13},{2,13},{2,13}},
{{0,0},{1,2},{0,12},{1,14},{2,1},{3,3},{2,13},{3,15},{0,12},{1,14},{0,12},{1,14},{2,13},{3,15},{2,13},{3,15}},
{{0,0},{0,3},{0,12},{0,15},{2,1},{2,3},{2,13},{2,15},{0,12},{0,15},{0,12},{0,15},{2,13},{2,15},{2,13},{2,15}},
{{0,0},{3,0},{12,0},{15,0},{1,2},{3,2},{13,2},{15,2},{0,12},{3,12},{12,12},{15,12},{1,14},{3,14},{13,14},{15,14}},
{{0,0},{2,1},{12,0},{14,1},{1,2},{3,3},{13,2},{15,3},{0,12},{2,13},{12,12},{14,13},{1,14},{3,15},{13,14},{15,15}},
{{0,0},{1,2},{12,0},{13,2},{1,2},{1,2},{13,2},{13,2},{0,12},{1,14},{12,12},{13,14},{1,14},{1,14},{13,14},{13,14}},
{{0,0},{0,3},{12,0},{12,3},{1,2},{1,3},{13,2},{13,3},{0,12},{0,15},{12,12},{12,15},{1,14},{1,15},{13,14},{13,15}},
{{0,0},{3,0},{8,4},{11,4},{1,2},{3,2},{9,6},{11,6},{0,12},{3,12},{8,12},{11,12},{1,14},{3,14},{9,14},{11,14}},
{{0,0},{2,1},{8,4},{10,5},{1,2},{3,3},{9,6},{11,7},{0,12},{2,13},{8,12},{10,13},{1,14},{3,15},{9,14},{11,15}},
{{0,0},{1,2},{8,4},{9,6},{1,2},{1,2},{9,6},{9,6},{0,12},{1,14},{8,12},{9,14},{1,14},{1,14},{9,14},{9,14}},
{{0,0},{0,3},{8,4},{8,7},{1,2},{1,3},{9,6},{9,7},{0,12},{0,15},{8,12},{8,15},{1,14},{1,15},{9,14},{9,15}},
{{0,0},{3,0},{4,8},{7,8},{1,2},{3,2},{5,10},{7,10},{0,12},{3,12},{4,12},{7,12},{1,14},{3,14},{5,14},{7,14}},
{{0,0},{2,1},{4,8},{6,9},{1,2},{3,3},{5,10},{7,11},{0,12},{2,13},{4,12},{6,13},{1,14},{3,15},{5,14},{7,15}},
{{0,0},{1,2},{4,8},{5,10},{1,2},{1,2},{5,10},{5,10},{0,12},{1,14},{4,12},{5,14},{1,14},{1,14},{5,14},{5,14}},
{{0,0},{0,3},{4,8},{4,11},{1,2},{1,3},{5,10},{5,11},{0,12},{0,15},{4,12},{4,15},{1,14},{1,15},{5,14},{5,15}},
{{0,0},{3,0},{0,12},{3,12},{1,2},{3,2},{1,14},{3,14},{0,12},{3,12},{0,12},{3,12},{1,14},{3,14},{1,14},{3,14}},
{{0,0},{2,1},{0,12},{2,13},{1,2},{3,3},{1,14},{3,15},{0,12},{2,13},{0,12},{2,13},{1,14},{3,15},{1,14},{3,15}},
{{0,0},{1,2},{0,12},{1,14},{1,2},{1,2},{1,14},{1,14},{0,12},{1,14},{0,12},{1,14},{1,14},{1,14},{1,14},{1,14}},
{{0,0},{0,3},{0,12},{0,15},{1,2},{1,3},{1,14},{1,15},{0,12},{0,15},{0,12},{0,15},{1,14},{1,15},{1,14},{1,15}},
{{0,0},{3,0},{12,0},{15,0},{0,3},{3,3},{12,3},{15,3},{0,12},{3,12},{12,12},{15,12},{0,15},{3,15},{12,15},{15,15}},
{{0,0},{2,1},{12,0},{14,1},{0,3},{2,3},{12,3},{14,3},{0,12},{2,13},{12,12},{14,13},{0,15},{2,15},{12,15},{14,15}},
{{0,0},{1,2},{12,0},{13,2},{0,3},{1,3},{12,3},{13,3},{0,12},{1,14},{12,12},{13,14},{0,15},{1,15},{12,15},{13,15}},
{{0,0},{0,3},{12,0},{12,3},{0,3},{0,3},{12,3},{12,3},{0,12},{0,15},{12,12},{12,15},{0,15},{0,15},{12,15},{12,15}},
{{0,0},{3,0},{8,4},{11,4},{0,3},{3,3},{8,7},{11,7},{0,12},{3,12},{8,12},{11,12},{0,15},{3,15},{8,15},{11,15}},
{{0,0},{2,1},{8,4},{10,5},{0,3},{2,3},{8,7},{10,7},{0,12},{2,13},{8,12},{10,13},{0,15},{2,15},{8,15},{10,15}},
{{0,0},{1,2},{8,4},{9,6},{0,3},{1,3},{8,7},{9,7},{0,12},{1,14},{8,12},{9,14},{0,15},{1,15},{8,15},{9,15}},
{{0,0},{0,3},{8,4},{8,7},{0,3},{0,3},{8,7},{8,7},{0,12},{0,15},{8,12},{8,15},{0,15},{0,15},{8,15},{8,15}},
{{0,0},{3,0},{4,8},{7,8},{0,3},{3,3},{4,11},{7,11},{0,12},{3,12},{4,12},{7,12},{0,15},{3,15},{4,15},{7,15}},
{{0,0},{2,1},{4,8},{6,9},{0,3},{2,3},{4,11},{6,11},{0,12},{2,13},{4,12},{6,13},{0,15},{2,15},{4,15},{6,15}},
{{0,0},{1,2},{4,8},{5,10},{0,3},{1,3},{4,11},{5,11},{0,12},{1,14},{4,12},{5,14},{0,15},{1,15},{4,15},{5,15}},
{{0,0},{0,3},{4,8},{4,11},{0,3},{0,3},{4,11},{4,11},{0,12},{0,15},{4,12},{4,15},{0,15},{0,15},{4,15},{4,15}},
{{0,0},{3,0},{0,12},{3,12},{0,3},{3,3},{0,15},{3,15},{0,12},{3,12},{0,12},{3,12},{0,15},{3,15},{0,15},{3,15}},
{{0,0},{2,1},{0,12},{2,13},{0,3},{2,3},{0,15},{2,15},{0,12},{2,13},{0,12},{2,13},{0,15},{2,15},{0,15},{2,15}},
{{0,0},{1,2},{0,12},{1,14},{0,3},{1,3},{0,15},{1,15},{0,12},{1,14},{0,12},{1,14},{0,15},{1,15},{0,15},{1,15}},
{{0,0},{0,3},{0,12},{0,15},{0,3},{0,3},{0,15},{0,15},{0,12},{0,15},{0,12},{0,15},{0,15},{0,15},{0,15},{0,15}}
};




bool accepte(int start) {
  int s = start;
  for (int i=0; i<t; i++) {
    s = det[a][s][(int)buff[i]-(int)'0'];
    if (s==0) return false;
  }
  return ((start & s)!=0);
}

bool accepte() {
  return (accepte(1) || accepte(2) || accepte(4) || accepte(8));
}


int main() {
 
  while (scanf("%d %d %s", &a, &t, buff)==3) { 
    if (accepte()) printf("REACHABLE\n");
    else printf("GARDEN OF EDEN\n");
  }

  return 0;
}