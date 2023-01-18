#Python 2.7 survey form.Project dated by 9/1/23
import time
from collections import OrderedDict
print("All the data is stored")
print("All your answers will be used.")
print("Welcome to my survey, User")
User = OrderedDict()

time.sleep(1)
age = int(input("Input your age "))
if age >= 11:
    print("Okay, you can continue.")
else:
    print("Sorry, but you need to be at least 10 y/o")
    exit()
User["Age"] = age

time.sleep(1)
gender = raw_input("Input you gender ")
User["Gender"] = gender

time.sleep(1)
name = raw_input("Input your name ")
User["Name"] = name
#if name == "Bob":
#    print("No")
#    exit()

time.sleep(1)
continent = raw_input("Input your current continent ")
country = raw_input("Input your current country ")
state = raw_input("Input your current state ")
city =raw_input("Input your current city ")
User["Continent"] = continent
User["Country"] = country
User["State"] = state
User["City"] = city

time.sleep(1)
sport_fav = raw_input("Input your favorite sport ")
User["Favorite Sport"] = sport_fav

time.sleep(1)
coding_know = raw_input("Do you know coding? ")
if coding_know == "No"  or coding_know == "no":
    print("Sorry, but you need to know.")
    exit()
elif coding_know in ("Yes"  "yes"):
    print("Good!")
User["Know Coding"] = coding_know

if coding_know == "Yes" or "yes":
    language_code = raw_input("In wich languge do you code? ")
    if language_code in ("Java" "Python" "C C++ C# " "PHP"):
        print("Backend, Database and Robotic programmers are the best.")
    elif language_code in ("SQL"):
        print("Backend, Database and Robotic programmers are the best.")
    elif language_code in ("Arduino"):
        print("Backend, Database and Robotic programmers are the best.")
    else:
        print("Backend, Database and Robotic programmers are the best.")
        exit()
    User["Coding Language"] = language_code

time.sleep(1)
score = 0
print("Code Quiz")
print("You'll need to answer with a or b")
question_1 = raw_input("Who created python? a: Guido Van Rossum, b: Albert Enstein ")
if question_1 == "b":
    print("False.It was Guido.")
else:
    print("Correct.")
    score = score + 1
User["Answer 1"] = question_1

time.sleep(1)
question_2 = raw_input("When was python created? a: February 20, 1991, b: February 20,1996 ")
if question_2 == "b":
    print("False.It was 1991.")
else:
    print("Correct.")
    score = score + 1
User["Answer 2"] = question_2

time.sleep(1)
question_3 = raw_input("What is SQL ? a: Structured Query Language, b: Safe Query Language ")
if question_3 == "b":
    print("False.It was Structured Query Language.")
else:
    print("Correct.")
    score = score + 1
User["Answer 3"] = question_3

time.sleep(1)
question_4 = raw_input("Is the earth round ? a: yes, b: yes ")
if question_3 == "a" or "b":
    print("Correct")
    score = score + 1
else:
    print("Correct.")
    score = score + 1
User["Answer 4"] = question_4

print("Your score is " + str(score) + "/4" )
User["age"] = 1
User["gender"] = 2
User["name"] = 3
User["continent"] = 4
User["country"] = 5
User["state"] = 6
User["city"] = 7
User["favorite sport"] = 8
User["know coding"] = 9
User["coding language"] = 10
User["answer 1"] = 11
User["answer 2"] = 12
User["answer 3"] = 13
User["answer 4"] = 14
print(User)
