a=input("Dati pimul sir: ")
b=input("Dati al doilea sir: ")
lista=[]
listb=[]
for i in a:
    lista.append(i)
for x in b:
    listb.append(x)
multima=set(lista)
multimb=set(listb)
print("reuniunea: ",multima.union(multimb))
print("intersectia: ",multima.intersection(multimb))
print("diferenta: ",multima.difference(multimb))