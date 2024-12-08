def rem(l,word):
    word = word.strip()
    if(word in l):
        l.remove(word)
    return l

l1 = ['sarmad','talha','ameen','torjan']
a =rem(l1,'torjan')
print(a)