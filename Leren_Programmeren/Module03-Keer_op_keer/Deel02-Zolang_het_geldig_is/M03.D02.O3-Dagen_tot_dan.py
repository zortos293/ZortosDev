Dagen = ["ma","di","wo","do","vr","za","zo"]
x = 0
DagenInput = int(input("Tot welke dag wil je dat het uitput\n[MA=1/DI=2/WO=3/DO=4/VR=5/ZA=6/ZO=7]")) -1

while x <= DagenInput:
    print(Dagen[x])
    x = x +1


