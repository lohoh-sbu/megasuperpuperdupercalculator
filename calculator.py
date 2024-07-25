a = float(input( 'Введіть перше чилсо: '))
action = input("Введіть знак (+,-,*,/): ")
b = float(input("Введіть друге число"))
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    print(a / b)
else :
    print("Ви вели невірну дію")
