#file = open("text.txt", "w")
#file.write("DinoShark\nMouseDragon\n")
#file.close()
#print(file)

def calculation():
  choice = input("What arithmetical function would you like to choose out of +, -, * and /:  ")
  n1 = int(input("Enter number 1:  "))
  n2 = int(input("Enter number 2:  "))
  if choice == "+":
    ans = n1 + n2
  if choice == "-":
    ans = n1 - n2
  if choice == "*":
    ans = n1 * n2
  if choice == "/":
    ans = n1 / n2
  answer = str(ans)
  file = open("calculations.txt","w")
  file.write(answer)
  file.close()
  file = open("calculations.txt", "r")
  quicklist = file.readlines()
  print(quicklist)
  file.close()

def score():
  import datetime
  currenttime = datetime.datetime.now()
  timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")
  score = input("Enter your score:  ")
  print(score, "recorded at: ", timestamp)
  file = open("scores.txt", "w")
  file.write(score)
  file.write(" recorded at: ")
  file.write(timestamp)
  print(file)
  file.close()

x = input("score or calculations:  ")
if x == "score":
  print(score())
if x == "calculation":
  print(calculation())