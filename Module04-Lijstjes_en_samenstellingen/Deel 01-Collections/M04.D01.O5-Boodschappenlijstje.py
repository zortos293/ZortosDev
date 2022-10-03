my_dict = {}
show_lijst = False
first_time = False

while show_lijst == False:
    if first_time == False:
        first_time = True
        product = input("Product naam: ")
        productint = input("Product stuks: ")
        if product.lower() in my_dict:
            
            my_dict[product.lower()] = my_dict[product.lower()] + int(productint)
        else:
            my_dict[product.lower()] = int(productint)
    else:
        w = input("wil je meer Producten toevoegen?")    
        if w == 'y'.lower():
            product = input("Product naam: ")
            productint = input("Product stuks: ")
            if product.lower() in my_dict:

                my_dict[product.lower()] = my_dict[product.lower()] + int(productint)
            else:
                my_dict[product.lower()] = int(productint)
        else:
            show_lijst = True
            print(f'\n\n-[BOODSCHAPPENLIJST]-')
            for key,value in my_dict.items():
                print(f'{value}x {key}')
            print(f'--------------------')