#KEVIN TEH TING QIAN
#TP068904


while True:
    print("\t\t\t\tFRESHCO ONLINE GROCERY STORE")
    print("\t\t\t\t\tWELCOME")
    print("\t\t\tADMIN\t\tREGISTERED CUSTOMER\t\tNEW CUSTOMER")
    iden = input("Please choose one identity:").upper()                   #prompt user for identity

    a = "ADMIN"
    b = "REGISTERED CUSTOMER"
    c = "NEW CUSTOMER"

    list = {}
    orderlist = {}

    def cusorder():                                                                 #open orderlist.txt and write 
        with open("orderlist.txt", "a") as file:
            file.write("USER: " + username + " " + str(orderlist) + " TOTAL: " 
            + str(total) + "\n")

    def viewspeccusorder():                                                         #open orderlist.txt to view specific customer order
        specus = input("Insert the username that U want to view:")                  #prompt user insert username
        print("\n")
        with open("orderlist.txt", "r") as file:
            f = file.readlines()
            for i in f:                                                                 
                F = i.split()
                if specus in F:
                    print(i)

    def viewcusorder():                                                             #open orderlist.txt to view customer order
        with open("orderlist.txt", "r") as file:
            print(file.read())

    def umlist(line_number, texta, textb):                                          #open groslist.txt to update or modify detail
        with open("groslist.txt") as file:
            lines = file.readlines()
  
        if (line_number <= len(lines)):                                             #if the line number in file
            lines[line_number - 1] = texta + " " + str(textb) + "\n"
            with open("groslist.txt", "w") as file:
                for line in lines:
                    file.write(line)
  
        else:                                                                       #if line number not in file
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")  
        
    def grosadd():                                                                  #open groslist.txt for add new grocery  
        with open("groslist.txt",mode="a",encoding="utf-8") as file:
            adgro = input("What grocery want to add:").upper()                      #input the grocery
            adpri = input("Price:")                                                 #insert price
            file.write("\n" + adgro + " " + str(adpri))

    def grolist():                                                                  #open groslist.txt to view grocery list
        with open("groslist.txt",mode="r") as file:
            count = 0
            line = file.readlines()            
            print("   GROCERY      ________PRICE________")
            for item in line:                                                       #for the grocery in file
                count += 1
                gro = item.split()[0]
                pri = item.split()[1]
                groslists = (f"{count}. {gro}: \t\tRM {pri}")
                list.update({gro: float(pri)})
                print(groslists)

    def grosdlt():                                                                  #open groslist.txt to delete grocery
        gros_dlt = input("What grosery want to delete:").upper()                    #input with grocery want to delete
        with open("groslist.txt",mode="r",encoding="utf-8") as file:
            gros = file.readlines()
        with open("groslist.txt",mode="w",encoding="utf-8") as itemdlt:
            for item in gros:                                                       #for grocery in file
                gros = item.strip("\n").upper()
                if gros_dlt not in gros:
                    itemdlt.write(item)

    def host():                                                                     #open hostlist.txt to read host username and password
        host = {}
        with open("hostlist.txt" , "r+") as file:
            for line in file:
                user, passwo = line.split(', ')
                host[user] = passwo
        return host

    def userlist():                                                                 #open user.txt for read users username and password
        userss = {}
        with open("user.txt" , mode="r") as file:
            for line in file:
                user, passwo = line.split(", ")
                passwo = passwo.strip()
                userss[user] = passwo
        return userss

    def userinfo():                                                                 #open userinfo.txt to write user personal information
        with open("userinfo.txt" , "a") as file:
            file.writelines(newid + "\t\t" + newrepass + "\t\t" + name + "\t\t" + str(yob) + "\t\t" +  gen + "\n")

    def viewuserinfo(infoname):                                                     #open userinfo.txt to let user view their on personal information
        with open("userinfo.txt" , "r") as file:
            for line in file:
                if infoname in line:
                    return(line)

    def newuser():                                                                  #open user.txt to let user write their own username and password
        newcus= {}
        with open("user.txt" , "a") as file:
            file.write("\n" + newid + ", " + newrepass)

    def rating(infoname):                                                           #open rate.txt to input user rating
        with open("rate.txt" , "a") as file:
            file.write(username + " Rate: " + str(rate) + "\n")

    def viewrate():                                                                #open rate.txt to let admin view rate
        with open("rate.txt" , "r") as file:
            return(file.read())

####################################################################

    if iden == a:                                                                  #if user is admin
        while True:
            admin = host()
            print("\nUsername")
            username = input("")
            print("Password")
            password = input("")

            if username not in admin:
                print(f"\nUser not found {username}\n")
            elif admin[username] != password: 
                print(f"\nIncorrect password for user {username}\n")
            else:
                print("\nWelcome\n")
                break
            
        print("\n\t\t\t\t\tGroceries\n")
        
        grolist()

        print("\n")
        while True:
            print("\n1. UPDATE/MODIFY GROCERY DETAIL\n2. DELETE GROCERY DETAIL\n3. ADD GROCERY\n4. VIEW CROCERY LIST\n5. SEARCH ORDER OF SPECIFIC CUSTOMER\n6. VIEW ORDER OF CUSTOMERS\n7. VIEW CUSTOMER RATING\n8. EXIT")
            ADFUN = input("Which number do you want:")                              #prompt user input number
            if ADFUN == "1":                                                        #number = 1
                grolist()                                                           #show the result
                line_number = int(input("Which Line U want to modify: "))           #input line number that want
                texta = input("Grocery: ").upper()                                  #insert new grocery
                textb = int(input("Price: "))                                       #insert new price
                umlist(line_number, texta, textb)                                   #show the result

            elif ADFUN == "2":                                                      #number = 2
                grosdlt()                                                           #show the result
                grolist()                                                           #show the result
                
            elif ADFUN == "3":                                                      #number = 3
                grosadd()                                                           #show the result
            
            elif ADFUN == "4":                                                      #number = 4
                print("\t\t\t\t\tGROCERY LIST:")
                grolist()                                                           #show the result
                
            elif ADFUN == "5":                                                      #number = 5
                viewspeccusorder()                                                  #show the result
            
            elif ADFUN == "6":                                                      #number = 6
                viewcusorder()                                                      #show the result

            elif ADFUN == "7":                                                      #number = 7
                aa = 1
                print(viewrate())                                                   #show the result

            elif ADFUN == "8":                                                      #number = 8
                print("SEE U NEXT TIME")
                break                                                               #stop the loop
            else:                                                                   #invalid number
                print("ERROR number, pls try again.")
                
    elif iden == b:
        while True:
            users = userlist()
            print("\nUsername")
            username = input("")                                                    #input username
            print("Password")
            password = input("")                                                    #input password

            if username not in users:                                               #username input wrong
                print(f"\nUser not found {username}\n")
            elif users[username] != password:                                       #password input wrong
                print(f"\nIncorrect password for user {username}\n")
            else:                                                                   #username and password correct
                print("\nWelcome\t" + username + "\n")
                break

        print("\n\t\t\t\t\tGroceries")                                              #view groceries detail
        grolist()                                                                   #print grocery list

        askpur = input("Want to purchase?(yes/no):").upper()                        #ask for purchase
        while askpur != "YES" and askpur != "NO":                                   #answer not in YES or NO
            print("ERROR INPUT")
            askpur = input("Want to purchase?(yes/no):").upper()                    #ask for purchase 

        while askpur == "YES":                                                      #answer in YES
            purgro = input("Add grocery U want:").upper()                           #ask for what grocery to add
            if purgro in list:                                                      #find grocery in list
                try:
                    purqty = int(input("Quantity:"))                                #ask for quantity
                except ValueError:                                                  #input not in number quantity
                    print("ERROR TYPE")
                    continue

                orderlist.update({purgro:{"QUANTITY":purqty,"SUBTOTAL":list[purgro]*purqty}})
                print(orderlist)                                                    #print current order list
                askpur = input("Want do more purchase?(yes/no):").upper()           #ask for purchase
                while askpur != "YES" and askpur != "NO":
                    print("ERROR INPUT")
                    askpur = input("Want do more purchase?(yes/no):").upper()       #ask for more purchase
            else:                                                                   #grocery not found
                print("Grocery no exist")
                askpur = input("Want do more purchase?(yes/no):").upper()           #ask for more purchase
                while askpur != "YES" and askpur != "NO":                           #answer not in YES or NO
                    print("ERROR INPUT")
                    askpur = input("Want do more purchase?(yes/no):").upper()       #ask for more purchase
        else:                                                                       #print order list
            print("\n\n")
            print("\n\t\t\t\t\t\t\tORDER LIST")
            print("\t\t\t\t\tItem         Quantity        Subtotal")
            total = 0
            for gro in orderlist:
                print(f"\t\t\t\t\t{gro}      \t{orderlist[gro]['QUANTITY']}              {orderlist[gro]['SUBTOTAL']}")
                total = orderlist[gro]['SUBTOTAL'] + total
        
            print(f"\t\t\t\t\t***TOTAL:***\t\t       {total}")
            cusorder()                                                              #print the total order list and cost
            if total != 0:
                print("\n\n\t\t\t\t\t\t\tPAYMENT")
                bank = input("\n\n\t\t\tChoose a bank for payment(HLB PPB CIMB):  ").upper()
                while True:
                    if bank != "HLB" and bank != "PPB" and bank != "CIMB":
                        print("\nINVALID BANK PLS TRY AGAIN")
                        bank = input("\nChoose a bank(HLB PPB CIMB):  ").upper
                    else:
                        while True:                                  
                            try:
                                bankacc = int(input("\nInsert ur bank acc:  "))                                            #try if age in number
                                break
                            except ValueError:                                                      #age not in number
                                print("ERROR TYPE")
                        print("\n\n\t\t\tPayment successful!!!\n")
                        break
 
        infoname = username
        print("\n\nPERSONAL INFORMATION:")                                            #registered customer personal info
        print("USERNAME\tPASSWORD\tNAME\t\tBORN YEAR\tGENDER")

        print(viewuserinfo(infoname))                                                 #print the detail

        print("\n\n\n\t\t\t\tThis is the end of this system.\n\t\t\t\tWhat rating will U give us(0 - 100):")
        while True:
            try:
                rate = int(input("Rate: "))                                         #user insert rating
                if rate > 100:                                                      #rating bigger than the value
                    print("Waoo, over 100, too much, pls lower or equal 100")
                    #rate = int(input("Rate: "))
                elif rate < 0:                                                      #rating smaller than the value
                    print("Sure give us like this :( , can more higher a bit TT")
                    #rate = int(input("Rate: "))
                else:
                    break
            except ValueError:                                                      #rating not in number
                print("ERROR TYPE, RATE IN NUMBER")
        rating(infoname)
        print("Ur rate to us is" + ": " + str(rate) + ", THANKSSSSSSSSS")           #show the customer rating and say thanks

    elif iden == c:
        print("\nGroceries:")                                                       #view groceries detail
        grolist()
        print("\n\t\t\tREGISTRATION")
        
        name = input("NAME:")                                                       #insert user name 
        while True:                                  
            try:
                yob = int(input("Year of Birth:"))                                            #try if age in number
                break
            except ValueError:                                                      #age not in number
                print("ERROR TYPE")
        while True:
            gen = input("GENDER(M/F):").upper()                                     #inpur gender           
            if gen != "M" and gen != "F":                                           #gender not in F and F
                print("Invalid Gender, try again")
            else:                                                                   #gender in M or F
                #userinfo()
                break

        newid = input("USER ID:")                                                   #insert user ID
        newpass = input("Password:")
        while True:                                             
            newrepass = input("REWRITE PASSWORD:")                                  #rewrite password
            if newrepass != newpass:                                                #password not same
                print("\nINCORRECT")
            else:                                                                   #password same
                newuser()
                userinfo()
                print("")
                break
            
        print("\t\t\t\t\t\tREGISTRATION DONE")                                      #registration done

    else:
        print("\t\t\t\t\t\tNOT RECOGNIZED")                                         #invalid indentity

    print("\t\t\t\t\t\tEXIT\n\n")                                                   #exit
   