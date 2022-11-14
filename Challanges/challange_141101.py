Numbers = []

for aantal in range(10):

    nummer_int = int(input(f'Voer nummer {aantal} in : '))
    Numbers.append(nummer_int)
    
Numbers.sort()

def is_integer_num(number_list : list):
    deelbaar_list = []
    for deel_list in number_list:
        if (deel_list / 3)%1 == 0:
            deelbaar_list.append(deel_list)
    return deelbaar_list



print(f'Het grootste Getal is : {Numbers[-1]}')
print(f'Het kleinste Getal is : {Numbers[0]}')
deelbaar_nummers = is_integer_num(Numbers)
print(deelbaar_nummers)