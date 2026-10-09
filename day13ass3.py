def buy_soda():
    price=150
    money_inserted=0
    while money_inserted<price:
        cash=int(input("Insert ₦50 or ₦100 note: "))
        if cash==50 or cash==100:
            money_inserted+=cash
        else:
            print("Invalid note rejected")
        print (money_inserted)
    change=money_inserted-price
    if change>0:
        return f"Dispensing soda. Your change is: ₦{change}"
    else:
        return "Dispensing soda.Exact Price Given"
print(buy_soda())