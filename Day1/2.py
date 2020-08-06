x = [1,2,3,4,5,6]

for i in range(0,len(x)):
    if i < len(x)//2:
        x[i],x[len(x)-(i+1)] = x[len(x)-(i+1)],x[i]
print(x)