contact = {}

def ShowContsctList() :
    for key in contact:
        print ("NAME: {} \n"
               "NAMBER:{}".format(key,contact.get(key)))
        

while True:
    choice = int(input ("1. Add Contact\n" 
                        "2. Searce Contact\n " \
                        "3. Show All Contact\n" \
                        "4. Edit Contact\n" \
                        "5. Delete Contact\n" \
                        "6. Exit\n" \
                       "Pleace Silect Your Choice :    "))


    if choice == 1 :
        name = input (" Your Name :   ").lower()
        namber = input ("Your Namber :     ").lower()
        contact[name] = namber 


    elif choice == 2 :
        ContactNamber = input (" Enter Your Contact Name:       ").lower()
        if  ContactNamber in contact:
            print (f" Name is :{ContactNamber}"
                   f" Namber is:{contact[ContactNamber]}")
            
        else: 
            print (" Youre Contact Namber Is Not Faund <@>")

            
    elif choice == 3: 
        if not contact:
            print(" Your Contact List Is Empty  <@>")   

        else:

            ShowContsctList()
    elif choice == 4:
       editcontact = input("Enter Contact Name: ").lower()
       if editcontact in contact:
        newname = input("Change Your Name: ").lower()
        newnumber = input("Change Your Number: ")
        old_value = contact[editcontact]
        del contact[editcontact]
        contact[newname] = newnumber

        print("Contact updated successfully.")
        ShowContsctList()
       
       else:
        print("Contact not found.")
    elif choice == 5 :
       del_contact = input(" Enter Contact Name :     ").lower()
       if del_contact in contact:
          makesure = input (f" You Are Sure Delete {del_contact}Contact?"
                            "MAKE SURE  Y / N :          ").lower()
          if makesure == "y":
             del contact[del_contact]
             print(" Contact Delete Saccefully ")
          else:
             print (" Contact Delete Unsuccefull ")
       
       else:
          print(f" Not Faund the {del_contact} Contact") 


    else :
       break



    # project complite alhamdulillah