
def first(count):
    for i in range(0,len(x)):
        if input_number == x[i]:
            count += 1
            return i
    if count == 0:
        return "Not found"

x = [1, 2, 3, 4, 5, 6]
input_number = int(input("enter a number to be searched"))
count = 0
print("The Location of the number is = ",first(count))