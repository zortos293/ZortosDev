dagen  = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag',"Zatedag", "Zondag")
werkdagen_str = "De werkdagen zijn: "
for teller in range(5):
    werkdagen_str += dagen[teller] + ", "
print(f'Alle dagen van de week zijn: {dagen}')
print(werkdagen_str)
print(f'De weekenddagen zijn: {", ".join(dagen[-2:])}')
print(f'Alle dagen van de week in omgekeerde volgorde zijn: {", ".join(reversed(dagen))}')
print(f'De werkdagen in omgekeerde volgorde zijn: {", ".join(reversed(dagen[:-2]))}')
print(f'De weekenddagen in omgekeerde volgorde zijn: {", ".join(reversed(dagen[-2:]))}')