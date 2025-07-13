# প্রশ্ন ১:
# একটা প্রোগ্রাম লেখো যেটা একটা text file তৈরি করবে।
# ইউজার যেটা টাইপ করবে, সেটা ওই ফাইলে লিখে রাখবে।

# উদাহরণ:
# Input: "Ami Python shikchi"
# Output: ei text ta file e save hobe → data.txt
# ANS NO 1

userinput = input(" enter your text :    ")
file_data= "data.txt"

try:
    with open(file_data, "w"  ) as f:
        f.write(userinput)
        print (f"youre text {userinput} succesfully added in in your text file")

except IOError as e:
    print (f" sorry yore somthing with wrong the issue is {e}")




# প্রশ্ন ২:
# নিচের list থেকে যাদের নাম্বার ৫০-এর নিচে তাদের জন্য "Fail" 
# আর যাদের ৫০-এর বেশি তাদের জন্য "Pass" প্রিন্ট করবে।

# marks = [40, 75, 30, 90, 60]
# Output হবে:
# 40 - Fail  
# 75 - Pass  
# 30 - Fail  
# 90 - Pass  
# 60 - Pass

# ANS NO 2

marks = [40, 75, 30, 90, 60]

for mark in marks:
    if mark >= 50:
        print (f"{mark} - pass")

    else:
        print(f"{mark} - fall")

       

# প্রশ্ন ৩:
# Exception Handling দিয়ে একটা প্রোগ্রাম লেখো যেটা ইউজারের কাছ থেকে সংখ্যা নিবে।
# যদি ইউজার ভূল করে সংখ্যা না দিয়ে কিছু লেখে, তাহলে:

# "Please enter a valid number"
# এই মেসেজ দেখাবে, আর প্রোগ্রাম error দিবে না।

try:
    userinput = int(input("please enter a namber : "))
    print (" your namber is ", userinput)


except ValueError :
    print(" pleace enter for only namber 1-9")
 

# প্রশ্ন ৪:
# একটা Class বানাও যার নাম Person।

# এর মধ্যে দুইটা attribute থাকবে: name আর age

# Constructor দিয়ে সেট করবে

# একটা method থাকবে যেটা বলবে:
# My name is <name> and I am <age> years old.

# ans no 4
userinputname = input (" your name enter here:  ")
userinputage = input (" your age here only: ")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def show_info(self): 
    print(f"My name is {self.name} and my age is {self.age} years old.")
    

my_person = Person(userinputname,userinputage)
my_person.show_info()




# প্রশ্ন ৫ (Bonus):
# একটা Function লিখো যেটা একটা বাক্যের মধ্যে কতটা vowel আছে সেটা গুনে দেবে।

# উদাহরণ:
# Input: "Bangladesh is beautiful"
# Output: 9 ta vowel

while True:
    def vowel_counter (text):
        vowel= {'a', 'e', 'i', 'o', 'u'}
        vowel_count_store = 0

        for vowel_check in text:
            if vowel_check.lower() in vowel:
                vowel_count_store +=1

        return vowel_count_store
    
    Userinput =input(" Enter Here : ")
    mein_checker = vowel_counter(Userinput)     
    if mein_checker > 0:
        print (" Your Vowel Count Is",mein_checker )
 
    else:
        print ("no vowel ditect!")   


