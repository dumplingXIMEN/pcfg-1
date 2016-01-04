#!/bin/python3
import sys
from collections import defaultdict
from inside import inside
from outside import outside
from tree import tree

d1=defaultdict(lambda: defaultdict(float))
d2=defaultdict(lambda: defaultdict(float))
a=defaultdict(lambda: defaultdict(float))
b=defaultdict(lambda: defaultdict(float))
s=defaultdict(lambda: defaultdict(float))
p=defaultdict(lambda: defaultdict(float))

infile=open(sys.argv[1],'r')
lines=infile.readlines()
for line in lines:
    l,r,prob=tuple(line.split(" # "))
    d1[l][r]=float(prob)
    d2[r][l]=float(prob)
infile.close()

sentence="A boy with a telescope saw a girl"
words=sentence.lower().split(' ')
length=len(words)

parses=defaultdict(list)
inside(parses,d1,d2,words,b,s,p,length)
outside(parses,d1,d2,a,b,length)

output=open(sys.argv[2],'w')
output.write(tree(words,p,'S',0,length-1) + '\n')
output.write(str(s[(0,length-1)]['S']) + '\n')
results=[]
for i in parses:
    for j in parses[i]:
        if a[i][j]:
            results.append(str(j)+' # '+str(i[0]+1)+' # '+str(i[1]+1)+' # '+str(b[i][j])+' # '+str(a[i][j]))
results.sort()

for result in results:
    output.write(result+'\n')
output.close()
