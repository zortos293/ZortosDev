vraag1 = input("Is de kaas geel? [y/n] :")
if vraag1 == "y":
    vraag1_ja = input("Zitten ergaten in? [y/n] :")
    if vraag1_ja == "y":
        vraag1_ja_ja= input("Is de kaas belagelijk duur? [y/n] :")
        if vraag1_ja_ja== "y":
            print("Je kaassoort is : Emmenthaler")
        else:
            print("Je kaassoort is : Leerdammer")
    else:
        vraag1_ja_nee = input("Is de kaas hard als steen? [y/n] :")
        if vraag1_ja_nee == "y":
            print("Je kaassoort is : Parmigiano Reggiano")
        else:
            print("Je kaassoort is : Goudse Kaas")    
else:
    vraag_nee_1 = input("Heeft de kaasblauweschimmel? [y/n] :")    
    if vraag_nee_1 == "y":
        vraag_nee_ja = input("Heeft de kaaseen korst? [y/n] :")
        if vraag_nee_ja == "y":
            print("Je kaassoort is : Blue de Rochbaron")
        else:
            print("Je kaassoort is : Foume d'Ambert")    
    else:
        vraag_nee_nee_1 = input("Heeft de kaas een korst? [y/n] :") 
        if vraag_nee_nee_1 == "y":
            print("Je kaassoort is : Camembert")
        else:
            print("Je kaassoort is : Mozzarella")        
