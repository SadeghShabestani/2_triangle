import termcolor2

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))

if a + b > c and a + c > b and b + c > a:
    print(termcolor2.colored("You Can Draw A Triangle ", color="green"))
else:
    print(termcolor2.colored("You Can Not Draw a Triangle", color="red"))
