#  প্রশ্ন ১:
# একটি function বানাও যেটি একটি সংখ্যা নেবে এবং বলবে সেটি বিজোড় (odd) নাকি জোড় (even)।

# উদাহরণ:
# check_number(7) ➜ "Odd"
# check_number(12) ➜ "Even"
#  ANS NO 1 -------: 
def check_namber():
    user_input = int(input (" pleace enter your namber :  "))
    if user_input % 2 == 0:
        return " your namber is even "
    else:
        return ' your namber is odd'
print(check_namber())



    
# 🔹 প্রশ্ন ২:
# তুমি একটা list পেয়েছো:
# marks = [60, 45, 80, 90, 33, 70]
# 👉 একটা প্রোগ্রাম বানাও যেটা এই list থেকে 50-এর নিচের সব নম্বর বাদ দিয়ে শুধু পাশ করা নম্বর গুলো প্রিন্ট করবে।


marks = [60, 45, 80, 90, 33, 70]
passed_namber = []
   
for mark in marks:   
   if mark >= 50 :
    passed_namber.append(mark)

print (passed_namber)



# প্রশ্ন ৩:
# একটি function লেখো যেটা ইউজারের নাম ইনপুট নেবে এবং বলবে এই নামের দৈর্ঘ্য (length) কত অক্ষরের।

# উদাহরণ:
# name_length("Mahadi") ➜ 6
# ANS NO 3 

def user_input_lenth():
    userinput = input (" enter your name : ")
    
    username = len(userinput)
    
    print (f"your name lenth is ",username) 

# user_input_lenth()   





# প্রশ্ন ৪:
# একটি dictionary আছে:
# students = {
#   "Rafi": 80,
#   "Jhuma": 95,
#   "Sifat": 60,
#   "Badhon": 40
# }
# 👉 তুমি কিভাবে শুধু যাদের নাম্বার ৫০-এর উপরে, তাদের নাম প্রিন্ট করবে?

# ANS NO 4 

students = {
  "Rafi": 80,
  "Jhuma": 95,
  "Sifat": 60,
  "Badhon": 40,
  "tuhin" : 44,
  
}
for name, mark in students.items():
    if mark >= 50 :
        print (name,mark)  



# প্রশ্ন ৫:
# একটা প্রোগ্রাম বানাও যেটা ইউজারের কাছ থেকে একটা বাক্য (sentence) নিবে এবং বলবে সেখানে মোট কতটি শব্দ (word) আছে।

# উদাহরণ:
# Input: "Ami ajke boro khushi"
# Output: 4 টি শব্দ


# ANS  NO 5 
userinput = input (" Enter Here :     ")
word = userinput.split()
word2 = len(word)
print (word2)