#===========================modil pwodwi yo=========================


def pwodwi():
    pwoduiDisponib={"pate kode": 250.00,
                "ji seriz": 150.00,
                "prestige": 150.00,
                "pizza": 1450.50,
                "espageti": 125.50,
                "pen a ze": 105.50,
                "jis sitwon": 160.00}
    cart=[]
    total=0
    

    print("---------Men sa nou genyen ki diponib yo ak tout pri yo------------")
    for key, value in pwoduiDisponib.items():
        print(f"{key}: {value:.2f} Goud")
    print("----------------------------------------------------------")

    while True:
        kantite=0
        food=input("Kisa wap achte? Siw pap chwazi anko peze \"q\" pouw kite sa: ").lower()
        kantite+=1
        if food.lower()=="q" :
            break
        elif pwoduiDisponib.get(food) is not None:
            cart.append(food)


    print("---------YOUR ORDER------------")
    for food in cart:
        total+=pwoduiDisponib.get(food)
        print(kantite,food, end=" ")
    print()
    print("Total lajan se: $",total)


