def inside(parses,d1,d2,words,b,s,p,n):
    for i in range(0,n):
        for j in range(0,n-i):
            k=j+i
            parse=parses[(j,k)]
            beta=b[(j,k)]
            if j==k:
                lefts=[x for x in d2[words[j]]]
                left=lefts[0]
                parse.append(left)
                beta[left]=d1[left][words[j]]
                s[(j,k)][left]=beta[left]
            else:
                for d in range(j,k):
                    for left in parses[(j,d)]:
                        for right in parses[(d+1,k)]:
                            lefts=[x for x in d2[' '.join((left,right))]]
                            for parent in lefts:
                                parse.append(parent)
                                beta[parent]+=d1[parent][' '.join((left,right))]*b[(j,d)][left]*b[(d+1,k)][right]
                                prob=d1[parent][' '.join((left,right))]*s[(j,d)][left]*s[(d+1,k)][right]
                                if prob>s[(j,k)][parent]:
                                    s[(j,k)][parent]=prob
                                    p[(j,k)][parent]=(d,left,right)
