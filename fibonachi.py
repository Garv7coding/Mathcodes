str_numbers = [0, 1]
x = 0
z = int(input("How much fibonachi would you like to generate?  "))
for i in range(z):
    fibonachiseq = str_numbers[x] + str_numbers[x + 1]
    str_numbers.append(fibonachiseq)
    x = x + 1

print(str_numbers)
lista = []

for i in str_numbers:
    lista.append(str(i))
data = ",".join(lista)

file = open("numbers.csv", "w")
file.write(data)
print(file)
file.close()