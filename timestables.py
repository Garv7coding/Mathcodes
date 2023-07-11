# Times tables
def Timestables():
    timestables = []
    x = int(input("Which times tables do you want?  "))
    y = int(input("How many of it do you want?  "))

    for i in range(y + 1):
        if i > 0:
            a = x * i
            timestables.append(a)
            a = 0
    print(timestables)
    lista = []

    for i in timestables:
        lista.append(str(i))
    data = ",".join(lista)

    file = open("timestables.csv", "w")
    file.write(data)
    file.close()


def main():
    Timestables()

if __name__ == "__main__":
    main()