num = input("Enter your number for factorial:   ")

factorial = 1

if int (num) >=1:
    for i in range (1, int(num)+1):
        factorial = factorial * i

print("Factorial of", num,  "is: ", factorial)