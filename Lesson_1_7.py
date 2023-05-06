import random

def RANDOM (start: int, end: int) -> int:
    return random.randrange(start, end)

def COMPUTERGAME ():
    endRandomNumber = 0
    urinishlarNumber = 0
    

    while True:
    
        endRandomNumber = int(input("Siz bilan Bir o'yin o'ynamoqchiman.men nechagacha son o'ylay min(10) max(1.000)"))

        urinishlarNumber = int(input("Siz nechta urinishga ega bo'lmoqchimiz min(3) max(10)"))

        if endRandomNumber >=10 and endRandomNumber <=1000 and urinishlarNumber >=3  and urinishlarNumber <= 10:
            break
        else:
            print("Siz kiritgan ma'lumotlar tasdiqlnmadi.")
    

    randomNumber = RANDOM(1, endRandomNumber)

    for num in range(1, urinishlarNumber + 1):

        inputnumber = int(input(f"Siz 1 dan {endRandomNumber} gacha son kiriting >>> "))

        if inputnumber < randomNumber:
            print("Siz kichik son kiritdingiz. Katta son kiriting >>> ")
            
        elif  inputnumber > randomNumber:
            print("Siz katta son kiritingiz. Kichik son kiriting >>> ")

        elif inputnumber == randomNumber:
            print(f"Siz yutdingiz.Siz {num} ta urinishda topdingiz >>>") 
            MAIN()

        if urinishlarNumber == num:
            print(f"Siz yutqazdingiz.Men o'ylagan son shu {randomNumber} >>>")
            MAIN()

def PEOPLEGAMES ():
    endRandomNumber = 0
    urinishlarNumber = 0
    

    while True:
    
        endRandomNumber = int(input("Men nechagacha son o'ylay min(10) max(1.00)"))

        urinishlarNumber = int(input("Siz nechta urinishga ega bo'lmoqchisiz min(3) max(15)"))

        if endRandomNumber >=10 and endRandomNumber <=100 and urinishlarNumber >=3  and urinishlarNumber <= 15:
            break
        else:
            print("Siz kiritgan ma'lumotlar tasdiqlnmadi.")

    randomNumber = RANDOM(1, endRandomNumber)

    for num in range(1, urinishlarNumber + 1):
        randomNumber = RANDOM(1, endRandomNumber)
        print(f"Siz o'ylagan son {randomNumber}")
        inputnumber = input(f"Siz o'ylagan son katta bo'lsa (+) kichik bo'lsa (-) to'g'ri bo'lsa (y): >>> ")

        if inputnumber == "+":
            randomNumber = RANDOM(randomNumber, endRandomNumber)

        if inputnumber == "-":
            randomNumber = RANDOM(1, randomNumber)

        if inputnumber == "y":
            print(f"Men o'ylagan son {randomNumber}.Men {num} ta urinishda topdim. >>>")
            MAIN()
            
        if urinishlarNumber == num:
            print("Siz o'ylagan sonni topa olmadim")
            MAIN()
            
def EXIT ():
    return print("See you")

def MENU ():
    print("\n 1) Computer Games \n 2) People Games \n 3) Exit")
    menuNumber = int(input("Menyudan birini tanlang: "))
    while True:
        if menuNumber == 1: 
            COMPUTERGAME()
            break
        elif menuNumber == 2: 
            PEOPLEGAMES()
            break
        elif menuNumber == 3: 
            print("See you")
            break
        else:
            print("Menudan birini kiriting.")
            break
        
def MAIN ():
    MENU()
MAIN()
