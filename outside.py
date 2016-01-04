def outside(parses,d1,d2,a,b,n):
    whole=(0,n-1)
    for s in parses[whole]:
        a[whole][s]=1.0
    for i in range(n-1,-1,-1):
        for j in range(0,n-i):
            k=j+i
            parse=parses[(j,k)]
            alpha=a[(j,k)]
            for left in parse:
                for d in range(k+1,n):
                    for right in parses[(k+1,d)]:
                        lefts = [x for x in d2[' '.join((left,right))]]
                        for parent in lefts:
                            if left!=right:
                                alpha[left]+=a[(j,d)][parent]*d1[parent][' '.join((left,right))]*b[(k+1,d)][right]
            for right in parse:
                for d in range(0,j):
                    for left in parses[(d,j-1)]:
                        lefts=[x for x in d2[' '.join((left,right))]]
                        for parent in lefts:
                            alpha[right]+=a[(d,k)][parent]*d1[parent][' '.join((left,right))] * b[(d,j-1)][left]
