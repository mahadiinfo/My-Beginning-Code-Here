# 🔹 প্রশ্ন ৬:
# একটা list আছে:
# fruits = ["apple", "banana", "mango"]
# 👉 তুমি কিভাবে এই লিস্টে নতুন একটি item যোগ করবে? যেমন: "orange"

# asn no 6 -----:
fruits = ["apple", "banana", "mango"]
fruits.append("orange ")
print (fruits)



# 🔹 প্রশ্ন ৭:
# নিচের কোডে কী সমস্যা আছে?

# if 5 > 3
#     print("Yes")

# ans n0 3 ------: 

if 5 > 3:
    print("Yes")
    # akhane bola hoise jodi 5 > 3 ar theke boro hoy tahole "yes" print kore daw  



#  🔹 প্রশ্ন ৮:
# একটি ফাংশন লিখো যেটা ১টি নাম (name) ইনপুট হিসেবে নেবে এবং বলবে:
# Hello, <name>!
# উদাহরণ: যদি ইনপুট হয় "Mahadi" → তাহলে আউটপুট হবে:

userinput = input(" Enter Your Name :  ")

print (f" Hello {userinput} Vaiya Apni Kwmon Asen ? ")


# 🔹 প্রশ্ন ৯:
# Python-এ loop কয় ধরনের হয়?
# একটি উদাহরণ দাও while loop দিয়ে।

# ANS NO 9 -----:
# python a loop hoy 2 dhoroner 1 no for loop 2 no while loop for loop is namber type loop mane setar akta ses ase but while loop is infinity type not stop is here 

# while loop die akti game banie dekhalam 
print (" apni jekono akti choiche koren dekhi amr sathe mile kina :   ")

mystore = [ "s", "w", "e"]
while True:
    userinput2 = input (" enter here : ").lower()
    if userinput2 == "q":
         print(" Thank You Youre Choice game over")  
         break
    elif userinput2 in mystore :
           print (" you are right") 
           print (" you want to game quite pleace enter Q ")
    else:
         print (" you are wrong ")
         print (" you want to game quite pleace enter Q ")



# input() ফাংশন দিয়ে ইউজারের কাছ থেকে সংখ্যা নেওয়ার পরে সেটাকে কিভাবে যোগফলের জন্য int এ রূপান্তর করো?

# উদাহরণ:
# num1 = input("Enter a number: ")
# num2 = input("Enter another: ")
# 👉 এখন তুমি কীভাবে num1 আর num2 যোগ করবে?

# ANS NO 10 -------:
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another: "))
print (" yore anser is ",num1+num2)


