# x = True
# #check if a number is prime or not
# num = int(input("Check if a number is prime or not:     "))
# for i in range(2, num):
#     if num % i == 0:
#         print("It isn't a prime number")
#         exit()
#     print("It is")


def isPrime(number=1):
    if number == 1:
        return False
    else:
        for i in range (2, number):
            if number % i == 0:
                return False
    return True

def main():
    number = int(input("Please provide me a number = "))
    print(isPrime(number))


if __name__ == "__main__":
    main()
