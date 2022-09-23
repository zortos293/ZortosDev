weekend = ("Zatedag", "Zondag")
werkdagen  = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag')

weekendstr = ', '.join(weekend)
werkdagenstr = ', '.join(werkdagen)
weekendback = ', '.join(weekend[::-1])
werkdagenback = ', '.join(werkdagen[::-1])

print(f'Alle dagen van de week zijn: {werkdagenstr} {weekendstr}')
print(f'De werkdagen zijn: {werkdagenstr}')
print(f'Alle dagen van de week in omgekeerde volgorde zijn: {weekendback} {werkdagenback}')
print(f'De werkdagen in omgekeerde volgorde zijn: {werkdagenback}')
print(f'De weekenddagen in omgekeerde volgorde zijn: {weekendback}')