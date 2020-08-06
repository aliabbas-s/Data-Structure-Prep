def ran(li,count):
    copy =  [ li[i] for i in range(0,len(li)) if li[i]!=0 ]
    print(copy)
    count = len(li) - len(copy)
    for j in range(count):
        copy.append(0)
    return copy

li = [1,2,0,0,0,0,0,0,3,0,0,5]
count = 0
print("The list without zeros is = ",ran(li,count))