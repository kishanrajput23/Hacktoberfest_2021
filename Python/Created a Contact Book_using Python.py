import sys
def initial_phonebook():
    rows, cols = int(input('Please enter the initial number of contacts: ')), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (Only):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print("....................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter Name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting because of blank field...")
            if j == 1:
                temp.append(int(input("Enter Number*: ")))
            if j == 2:
                temp.append(str(input("Enter e-mail address*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy)*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter category(Family/Friends/Work/Others)*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
    print("***********************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("***********************************************************")
    print("\t Now you can perform the following operations on this phone book\n")
    print("1. Add a new conact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phone book")
    choice = int(input("Please enter your choice : "))
    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: *")))
        if i == 1:
            dip.append(int(input("Enter number: *")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: *")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): *")))
        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others): *")))
    pb.append(dip)
    return pb

def remove_existing(pb):
    query = str(input("plz enter the contact name you want to remove : "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    if temp == 0:
        print("Sorry , you have entered an invalid query.\ Plz recheck and try again later.")
        return pb

def delete_all(pb):
    return pb.clear()

def search_existing(pb):
        choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter: "))
        temp = []
        check = -1
        if choice == 1:
            query = str(input("plz enter the name of contact you want to search: "))
            for i in range(len(pb)):
                if query == pb[i][0]:
                    check = i
                    temp.append(pb[i])
        elif choice == 2:
            query = int(input("plz enter the number of contact you want to search: "))
            for i in range(len(pb)):
                if query == pb[i][1]:
                    check = i
                    temp.append(pb[i])
        elif choice == 3:
            query = str(input("plz enter the email-id of contact you want to search: "))
            for i in range(len(pb)):
                if query == pb[i][2]:
                    check = i
                    temp.append(pb[i])
        elif choice == 4:
            query = str(input("plz enter the DOB of contact you want to search: "))
            for i in range(len(pb)):
                if query == pb[i][3]:
                    check = i
                    temp.append(pb[i])
        elif choice == 5:
            query = str(input("plz enter the Category(Family/Friends/Work/Others) of contact you want to search: "))
            for i in range(len(pb)):
                if query == pb[i][4]:
                    check = i
                    temp.append(pb[i])
        else:
            print("Invalid search criteria")
            return -1
        if check == -1:
            return -1
        else:
            display_all(temp)
            return check

def display_all(pb):
    if not pb:
        print("List is empty : []")
    else:
        for i in range(len(pb)):
            print(pb[i])

def thanks():
    print("*************************************************************")
    print("Thank you for using our Smartphone Directory system.")
    print("Please visit again!!")
    print("**************************************************************")
    sys.exit("Goodbbye, Have a nice day ahead!")
print("...............................................................")
print("Hello dear user, welcome to our Smartphone Directory system")
print("You may now proceed to explore this directory")
print("......................................................")

ch = 1
pb = initial_phonebook()
while ch in (1,2,3,4,5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb= remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact doesn't exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()
        

                
