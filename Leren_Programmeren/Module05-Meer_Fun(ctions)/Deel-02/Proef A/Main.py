import Variables


while True :
        Amount_question = int(input("Hoeveel bolletjes wilt u?\n> "))
        if Amount_question > 8:
            print("Sorry, dat is te veel.")
            stap1(0,hoorntjes,bakjes)
        elif Amount_question <= 3:
            stap2(Amount_question,hoorntjes,bakjes)
        elif Amount_question <= 8:
            print(f"Dan krijgt u van mij {Amount_question} bolletje(s).")
            stap3(Amount_question,hoorntjes,bakjes)
        else:
            print("Sorry, dat begrijp ik niet.")
            stap1(bolletjes,hoorntjes,bakjes)
