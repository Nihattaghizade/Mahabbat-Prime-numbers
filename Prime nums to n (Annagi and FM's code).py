n= int(input("Ededi daxil edin: "))
numbers = []
for i in range(2,n+1):
    numbers.append(i)
for i in numbers:
    for j in numbers:
        if j% i == 0  and j!= i:
            numbers.remove(j)
print(numbers)