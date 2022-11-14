a = int(input("vul nummer a : "))
b = int(input("vul nummer b : "))

if a > b:
    max = a
    print(f"a is het grootste getal: {max}")
    print(f"Het maximum is: {max}")
elif b > a:
    min = a
    print(f"a is het kleinste getal {min}")
    print(f"Het minimum is: {min}")
else:
    if a == b:
        print("a en b zijn even groot")
    

