tupplee=eval(input("Enter hetrogenous elements: "))
t1=()         #we can write tuple( as well as () for creating tuple :)
t2=tuple()
t3=tuple()
t4=tuple()
for i in tupplee:
    if(type(i)==str):
        t1=t1+(i,)
    elif(type(i)==int):
        t2=t2+(i,)
    elif(type(i)==float):
        t3=t3+(i,)
    elif(type(i)==complex):
        t4=t4+(i,)
        
print("String elements: ",t1)
print("Integer type elements: ",t2)
print("Float tpye elements: ",t3)
print("Complex elements: ",t4)
