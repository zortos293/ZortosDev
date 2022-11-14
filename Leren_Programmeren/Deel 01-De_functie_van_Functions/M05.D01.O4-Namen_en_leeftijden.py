def ask():
    dict_ask = []
    name = input("Wat is je naam? : ")
    age = input("Wat is je leeftijd? : ")
    dict_ask.append({"name": name, "age": age})
    return dict_ask


persoonsgegevens = []
while True:
    persoonsgegevens.append(ask())
    if input("Wil je nog een persoon toevoegen? (y/stop)").lower() == "stop":
        break

for persoon in persoonsgegevens:
    print(f"{persoon[0]['name']} is {persoon[0]['age']} jaar oud.")