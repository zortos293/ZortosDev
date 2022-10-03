my_dict = {}
show_lijst = False

while show_lijst == False:
    product = input("Product naam: ")
    productint = input("Product stuks: ")
    if product.lower() in my_dict:
        my_dict[product.lower()] = my_dict[product.lower()] + int(productint)
    else:
        my_dict[product.lower()] = int(productint)
    w = input("wil je meer Producten toevoegen?")    
    if w != 'y'.lower():
        break
    
print(f'\n-[BOODSCHAPPENLIJST]-')
for key,value in my_dict.items():
    print(f'{value}x {key}')
print(f'--------------------')