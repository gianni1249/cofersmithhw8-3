#!/usr/bin/python

import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

print(f1.read())
print(f2.read())

flines1 = open(sys.argv[1]).readlines()
flines2 = open(sys.argv[2]).readlines()

s1 = flines1[1].split()
s2 = flines2[0].split()
print('List 1 = ', s1)
print('Length of list 1 = ', len(s1))
print('List 2 = ', s2)
print('Length of list 2 = ', len(s2))

out = []
i = len(s1) - 1 
x = len(s2) - 1

while i and x >= 0 :
        out.append(s1[i])
        i -= 1 
        out.append(s2[x])
        x -= 1
if i == 0:
    out.append(s1[i])
    
f3=open('output.txt','w')

for element in out:
        f3.write(element)
        f3.write(" ")
f3.close()

print('The out list is: ', out)
print('The out list is printed in output.txt')
