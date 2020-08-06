def rotateByOne(li,n):
    li.append(li[0])
    for i in range(1,n):
        li[i-1] = li[i]
    li.pop(len(li)-2)
    return li



li = [1,2,3,4,5]
print("The rotated list is = ",rotateByOne(li,len(li)))

