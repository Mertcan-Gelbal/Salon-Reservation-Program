# ------------------------------------ FILE OPEN -----------------------------------
if (open("discount.txt","r",encoding="utf-8")) != 0:
    file = open("discount.txt","r")
    # print("File information read.")
    
    file.seek(2)
    maximumTicket = file.read(2)
        
    categoryFee= [1,2,3,4]
    j=0
    for i in range(9,31,7):
        file.seek(i)
        categoryFee[j] = file.read(3)
        j+=1
    # print(categoryFee)        
    discount = [1,1,1,1,1,1,1,1,1,1,1,1]
    j=0
    for i in range(40,160,10):
        file.seek(i)
        discount[j] = file.read(2)
        j+=1
    # print(discount)
else:
    print("The file is empty, please check the discount information.")
# The 0th index indicates the maximum number of ticket purchases.
# A set of 18 elements category 1-4 regular price discounts up to 5-19
# -------------------------------------- Salon --------------------------------------
Salon = [['-' for y in range(20)] for x in range(20)]
# -------------------------------------- Funct --------------------------------------
gain = 0
def addTicket():
    global gain
    while True:
        try:
            while True:
                category=int(input("Which category will you buy tickets from?(1-4)"))
                if(category <= 4 and category>=1):
                    break
                else:
                    print("Please enter valid category.")
                    continue
            while True:
                ticket = int(input("Enter the number of tickets. (You can purchase a maximum of 10 tickets.)"))
                if(ticket <= 10):
                    break
                else:
                    print("You can buy a maximum of 10 tickets.")
                    continue
            break
        except ValueError:
            print("Please enter appropriate values.")
            continue
    if category == 1: # (6-15 , 0-10)
        if 2<ticket and 5>=ticket:
            Total = int(int(categoryFee[0])*(ticket-(ticket*int(discount[0])/100)))
        elif 5<ticket and 8>=ticket:
            Total = int(int(categoryFee[0])*(ticket-(ticket*int(discount[1])/100)))
        elif 8<ticket and int(maximumTicket)>=ticket:
            Total = int(int(categoryFee[0])*(ticket-(ticket*int(discount[2])/100)))
        else:
            Total = int(int(categoryFee[0])*(ticket))
        print("Total = ",Total)
        for i in range(0,10):
            for j in range(5,15):     
                if(Salon[9][14] == "X"):
                    print("Category is full...")
                    break
                elif(Salon[i][j] == "-"):
                    if ticket != 0:
                        print("Seat numbers:",(i+1),"-",(j+1))
                        Salon[i][j] = "X"
                        ticket-=1
                    else:
                        break
                elif (Salon[i][j] == "X"):
                    continue
                else:
                    pass
    if category == 2: # (0-5 , 0-10) and (16-20 , 0-10)
        if 2<ticket and 4>=ticket:
            Total = int(int(categoryFee[1])*(ticket-(ticket*int(discount[3])/100)))
        elif 4<ticket and 7>=ticket:
            Total = int(int(categoryFee[1])*(ticket-(ticket*int(discount[4])/100)))
        elif 7<ticket and int(maximumTicket)>=ticket:
            Total = int(int(categoryFee[1])*(ticket-(ticket*int(discount[5])/100)))
        else:
            Total = int(int(categoryFee[1])*(ticket))
        print("Total = ",Total)
        for i in range(0,10):
            for j in range(0,5):
                if j == 5 and Salon[i][4-j] == "X":
                    break
                else:
                    if ticket != 0:
                        if Salon[i][(4-j)] == "-":
                            Salon[i][(4-j)] = "X"
                            print("Seat numbers:",(i+1),"-",(j+1))
                            ticket-=1
                    else:
                        continue
            for j in range(15,20):
                if ticket!=0:
                        if Salon[i][j] == "-":
                            Salon[i][j] = "X"
                            print("Seat numbers:",(i+1),"-",(j+1))
                            ticket-=1
                else:
                    continue     
              
    if category == 3: # (6-15 , 10-20)
        if 2<ticket and 5>=ticket:
            Total = int(int(categoryFee[2])*(ticket-(ticket*int(discount[6])/100)))
        elif 5<ticket and 8>=ticket:
            Total = int(int(categoryFee[2])*(ticket-(ticket*int(discount[7])/100)))
        elif 8<ticket and int(maximumTicket)>=ticket:
            Total = int(int(categoryFee[2])*(ticket-(ticket*int(discount[8])/100)))
        else:
            Total = int(int(categoryFee[2])*(ticket))
        print("Total = ",Total)
        for i in range(10,20):
            for j in range(5,15):     
                if(Salon[19][14] == "X"):
                    print("Category is full...")
                    break
                elif(Salon[i][j] == "-"):
                    if ticket != 0:
                        print("Seat numbers:",(i+1),"-",(j+1))
                        Salon[i][j] = "X"
                        ticket -= 1
                    else:
                        break
                elif (Salon[i][j] == "X"):
                    continue
                else:
                    pass
    if category == 4: # (0-5 , 10-20) and (16-20 , 10-20)
        if 2<ticket and 4>=ticket:
            Total = int(int(categoryFee[3])*(ticket-(ticket*int(discount[9])/100)))
        elif 4<ticket and 7>=ticket:
            Total = int(int(categoryFee[3])*(ticket-(ticket*int(discount[10])/100)))
        elif 7<ticket and int(maximumTicket)>=ticket:
            Total = int(int(categoryFee[3])*(ticket-(ticket*int(discount[11])/100)))
        else:
            Total = int(int(categoryFee[3])*(ticket))
        print("Total = ",Total)
        for i in range(10,20):
            for j in range(0,5):
                if j == 5 and Salon[i][4-j] == "X":
                    break
                else:
                    if ticket != 0:
                        if Salon[i][(4-j)] == "-":
                            Salon[i][(4-j)] = "X"
                            print("Seat numbers:",(i+1),"-",(j+1))
                            ticket-=1
                    else:
                        continue
            for j in range(15,20):
                if ticket!=0:
                        if Salon[i][j] == "-":
                            Salon[i][j] = "X"
                            print("Seat numbers:",(i+1),"-",(j+1))
                            ticket-=1
                else:
                    continue
    gain += Total
    salonShow()

def salonShow():
    for i in range(0,20): # Y axis
        if(i == 10):
            print()
        for j in range(0,20):  # x axis
            if((j == 5) or (j==15)):
                print("",end=" ")
            print(Salon[i][j],end=" ")
        print()

def newEvent():
    for i in range(0,20):
        for j in range(0,20):
            Salon[i][j] = "-"
    salonShow()
    
def totalGain():
    print("Total Gain: ",gain)
# -------------------------------------- Main ---------------------------------------
while True:
    print("--------------------------")
    print("    ---- MAIN MENU ----   ")
    print("--------------------------")
    print("1. Reservation")
    print("2. Print Hall")
    print("3. New Event")
    print("4. Total Gain")
    print("0. Exit")
    print("-------------------------")
    
    try:
        transaction = int(input("Please enter your transaction: "))
    except ValueError:
        print("Please enter an integer.")
        continue
    

    if transaction == 1:
        print("Reservation is in progress.")
        addTicket()
    elif transaction == 2:
        print("The hall is printing.")
        salonShow()
    elif transaction == 3:
        print("A new event is being prepared.")
        newEvent()
    elif transaction == 4:
        print("Total Gain is calculated.")
        totalGain()
    elif transaction == 0:
        print("Exiting the program.")
        break
    else:
        print("Please enter a number between 0 and 4.") 
file.close()