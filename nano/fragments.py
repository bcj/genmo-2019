import random as r
a=open("a.txt").read()
b=open("b.txt").read()
s=" "
d=set((a+s+b).split(s))
c=[]
for a,b in zip(a,b):
 if a!=b or a==s:
  w="".join(c)
  print(r.choice([x for x in d if w in x]) if c else "",end=s)
  c=[]
 else:
  c+=[a]