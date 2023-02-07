# Python 2.7 survey form.Project dated by 9/1/23

# Import packages
import time
from collections import OrderedDict

# What is User and Answers
User = OrderedDict()
Questions = OrderedDict()

# Date and Time
t = time.localtime(time.time())
localtime = time.asctime(t)
string = "Date and time: " + time.asctime(t)
print(string)
User["Date and Time"] = string

# Introduction
print("All the data is stored")
print("All your answers will be used.")

# The survey
time.sleep(1)
age = int(input("Input your age "))
if age >= 11:
    print("Okay, you can continue.")
else:
    print("Sorry, but you need to be at least 11 y/o")
    exit()
User["Age"] = age
Questions["Age"] = "Input your age "

time.sleep(1)
gender = raw_input("Input you gender ")
User["Gender"] = gender
Questions["Gender"] = "Input your gender "

time.sleep(1)
name = raw_input("Input your name ")
User["Name"] = name
Questions["Name"] = "Input your name "
if name == "Bob":
    print("No")
    quit()

time.sleep(1)
continent = raw_input("Input your current continent ")
country = raw_input("Input your current country ")
state = raw_input("Input your current state ")
city = raw_input("Input your current city ")
User["Continent"] = continent
User["Country"] = country
User["State"] = state
User["City"] = city

Questions["Continent"] = "Input your current continent "
Questions["Country"] = "Input your current country "
Questions["State"] = "Input your state "
Questions["City"] = "Input your current city"

time.sleep(1)
language = raw_input("Which language do you speak fluently? ")
User["Language"] = language
Questions["Language"] = "Which language do you speak fluently? "


# Structured question (Only sport questions)
time.sleep(1)
frequency = raw_input("Frequency of sport by week ")
intensity = raw_input("Intensity ")

highly_active = frequency == "daily"
high_intensity = intensity == "high"
User["Frequency"] = frequency
User["Intensity"] = intensity
User["High intensity"] = high_intensity
User["Highly active"] = highly_active

Questions["Frequency"] = "Frequency of sport by week "
sport_fav = raw_input("Input your favorite sport ")
User["Favorite Sport"] = sport_fav
Questions["Favorite Sport"] = "Input your favorite sport "

OS = raw_input("Which OS do you use? ")
if "Linux" or "linux" in OS:
    linux_distribution = raw_input("Which distribution? ")
    if linux_distribution == "Ubuntu" or "Debian" or "CentOS" or "Gentoo" or "Fedora" or "Scientific Linux":
        print("Good.")
else:
    print("Linux master race! ")
    quit()

time.sleep(1)
coding_know = raw_input("Do you know coding? ")
if coding_know == "No"  or coding_know == "no":
    print("Sorry, but you need to know.")
    quit()
elif coding_know in ("Yes"  "yes"):
    print("Good!")
User["Know Coding"] = coding_know
Questions["Know Coding"] = "Do you know coding? "

if coding_know == "Yes" or "yes":
    language_code = raw_input("In which language do you code? ")
    if language_code in "Java" "Python" "C C++ C# " "PHP" "JavaScript" "CSS" "HTML":
        print("Good to know.")
    elif language_code in "SQL":
        print("Good to know.")
    User["Coding Language"] = language_code
    Questions["Coding Language"] = "In which language do you code? "

time.sleep(1)
score = 0
print("Code Quiz")
print("You'll need to answer with a, b or c")
question_1 = raw_input("Who created python? a: Guido Van Rossum, b: Albert Einstein ")
if question_1 == "b":
    print("False.It was Guido.")
elif question_1 == "":
    print("Not Albert")
    quit()
else:
    print("Correct.")
    score = score + 1
User["Answer 1"] = question_1
Questions["Answer 1"] = "Who created python? a: Guido Van Rossum, b: Albert Einstein "

time.sleep(1)
question_2 = raw_input("When was python created? a: February 20, 1991, b: February 20,1996 ")
if question_2 == "b":
    print("False.It was 1991.")
    print("Not Albert")
    quit()
else:
    print("Correct.")
    score = score + 1
User["Answer 2"] = question_2
Questions["Answer 2"] = "When was python created? a: February 20, 1991, b: February 20,1996 "

time.sleep(1)
question_3 = raw_input("What is SQL ? a: Structured Query Language, b: Safe Query Language ")
if question_3 == "b":
    print("False.It was Structured Query Language.")
else:
    print("Correct.")
    score = score + 1
User["Answer 3"] = question_3
Questions["Answer 3"] = "What is SQL ? a: Structured Query Language, b: Safe Query Language"

time.sleep(1)
question_4 = raw_input("Is the earth round ? a: yes, b: yes, c: no ")
if question_3 == "a" or "b":
    print("Correct")
    score = score + 1
elif question_4 == "" or "c":
    print("You need to have minimum 2 IQ to live on this ROUND planet composed of humans that THINK")
    quit()
User["Answer 4"] = question_4
Questions["Answer 4"] = "Is the earth round ? a: yes, b: yes, c: no "

print("Your score is " + str(score) + "/4" )

# Ordered dict User
User["date and time"] = 1
User["age"] = 2
User["gender"] = 3
User["name"] = 4
User["continent"] = 5
User["country"] = 6
User["state"] = 7
User["city"] = 8
User["Language"] = 9
User["frequency"] = 10
User["intensity"] = 11
User["high intensity"] = 13
User["Highly active"] = 12
User["favorite sport"] = 13
User["know coding"] = 14
User["coding language"] = 15
User["answer 1"] = 16
User["answer 2"] = 17
User["answer 3"] = 18
User["answer 4"] = 19
print(User)

# Ordered dict Questions
Questions["age"] = 1
Questions["gender"] = 3
Questions["name"] = 4
Questions["continent"] = 5
Questions["country"] = 6
Questions["state"] = 7
Questions["city"] = 8
Questions["language"] = 9
Questions["frequency"] = 10
Questions["intensity"] = 11
Questions["favorite sport"] = 12
Questions["know coding"] = 13
Questions["coding language"] = 14
Questions["answer 1"] = 15
Questions["answer 2"] = 16
Questions["answer 3"] = 17
Questions["answer 4"] = 18
print(Questions)

# Open a document.txt
name = 'survey_data.txt'      
fichier = open(name,'w')   
fichier.write(User)
fichier.write(Questions)

fichier.close()


# End of the codes
print("Before the program ends, I recommend you to use my other programs and to play the game Stanley Parable. ")
quit()
