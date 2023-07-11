from random import randint
x = 11
print("Guess the ASCII Simon says")
while x > 0:
  comnd = randint(1,127)
  a = chr(comnd)
  b = input(("simon says:  " ))

  if b == a:
    print("You got it! 👍")
    x = x - 1
    break
  else:
    print("you failed")