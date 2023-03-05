import re
import math
tekst = """En ze stu[re]n [i]ngekleurde prentbriefkaarten van plekken waarvan ze zich niet reali[s]eren dat ze er nooit geweest zijn [a]an ' Iedereen op nummer 22, weer is prachti[g], onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s] vettig , maar we hebben een geweldig leuk restaurantje gevonden in de achterstraatjes waar ze Heine[ke]n hebben en kaas en uien chips en iemand die "Een beetje verliefd" speel[t] op een a[c]cordeon ' en je zit vier dagen vast op Schip[h]ol voor je vijfdaagse vliegvakantie met niks anders te eten dan uitgedroogde voorverpakte boterhammen..."""

def tussen_haken(tekst) -> list:
    grab = re.findall(r"\[([A-Za-z0-9_ ]+)\]", tekst)
    return grab

print(tussen_haken(tekst))


def numberToPower (number, power) -> int:
    return int(math.pow(number, power))

print(numberToPower(10, 6))

def make_sequences(n):
    return 1 + sum(map(make_sequences, range(1, n//2+1)))

print(make_sequences(10))
