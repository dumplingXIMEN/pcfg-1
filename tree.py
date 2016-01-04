def tree(words, p, m, l, r):
    if l==r:
        return '('+m+' '+words[l]+')'
    d,left,right=p[(l,r)][m]
    l1=tree(words,p,left,l,d)
    r1=tree(words,p,right,d+1,r)
    return '('+m+l1+r1+')'
