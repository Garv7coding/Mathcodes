def calculate():
    from math import sqrt
    print(" make sure your equation is in the form of ax^2 + bx + c.")
    a = int(input("What is the coefficient of X^2 in ax^2 ?"))
    b = int(input("What is the coefficient of X in bx ?"))
    c = int(input("What is the constant in this equation ?"))
    #ans1 = abs(b) - (sqrt((b**2)-4*a*c))/(2*a)
    #ans2 = abs(b) + (sqrt((b**2-4)*a*c))/(2*a)
    underthebracket = (b ** 2) - (4 * a * c)
    ans1 = (-b - sqrt(underthebracket)) / (2 * a)
    ans2 = (-b + sqrt(underthebracket)) / (2 * a)
    print("Your two answers are:", ans1, "and", ans2)

print(calculate())