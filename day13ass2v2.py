def track_saving(target_amount):
    while target_amount>0:
        deposit=int(input("Enter deposit amount: ₦"))

        if deposit<0:
            print("Error: You cannot deposit negeative money")
        elif deposit>target_amount:
                    print ("Error! Deposit amount is larger than tatget amount")
        else:
            target_amount-=deposit
        
        print(f"You still need to save :₦{target_amount}")

        

    print ("Congratulations! Savings goal reached")
track_saving(50000)