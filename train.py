#!/bin/python3
import sys

infile=open(sys.argv[1],'r')
lines=infile.readlines()
infile.close()

s=[]
current=[]
results={}
buf=''
for line in lines:
    for char in line:
        if char=='(':
            if len(buf):
                current.append(buf)
                buf=''
            s.append(current)
            current=[]
        elif char==')':
            if len(buf):
                current.append(buf)
                buf=''
            left=current[0]
            if len(current) == 2:
                right=current[1].lower()
            else:
                right=' '.join(current[1:])
            if not left in results:
                results[left]={}
            if not right in results[left]:
                results[left][right]=0
            results[left][right]+=1
            tmp=current[0]
            current=s.pop()
            current.append(tmp)
        elif char==' ':
            if len(buf):
                current.append(buf)
                buf=''
        else:
            buf+=char

outfile=open(sys.argv[2], 'w')
for result in results:
    total=0
    rights=results[result]
    for right in rights:
        total+=rights[right]
    for right in rights:
        outfile.write(result+" # "+right+" # "+str(float(rights[right])/total)+'\n')
outfile.close()
