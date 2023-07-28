#append()
a=[56,4,66,73,9]
b=[12,33,44,"aswin",0.44]
a.append(b)
print(a)

#clear()
b=["aswin","kumar","achu"]
b.clear()
print(b)

#copy()
c=["aswin","kumar","achu"]
c1=c.copy()
print(c1)

#count()
d=["aswin","kumar","achu","aswin","achu","aswin"]
print(d.count("achu"))

#extend()
e=[56,4,66,73,9]
f=[12,33,44,"aswin",0.44]
e.extend(f)
print(e)

#remove()
g=["aswin","kumar","achu","aswin","achu","aswin"]
g.remove("achu")
print(g)

#index()
h=[56,4,66,73,9,66]
h1=h.index(66)
print(h1)

#insert()
i=["aswin","kumar","achu"]
i.insert(0,"niwsa")
print(i)

#pop()
j=[12,33,44,"aswin",0.44]
j1=j.pop()
print(j1)

#reverse()
k=[12,33,44,"aswin",0.44]
k.reverse()
print(k)

#sort()
l=["aswin","kumar","achu"]
l.sort(reverse=True)
print(l)