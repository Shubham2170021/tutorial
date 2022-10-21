
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1_lower_case=name1.lower()
name2_lower_case=name2.lower()

name1_count=name1_lower_case.count("t")+name1_lower_case.count("r")+name1_lower_case.count("u")+name1_lower_case.count("e")+name2_lower_case.count("t")+name2_lower_case.count("r")+name2_lower_case.count("u")+name2_lower_case.count("e")
name2_count=name2_lower_case.count("l")+name2_lower_case.count("o")+name2_lower_case.count("v")+name2_lower_case.count("e")+name1_lower_case.count("l")+name1_lower_case.count("o")+name1_lower_case.count("v")+name1_lower_case.count("e")


total_score=str(name1_count)+str(name2_count)
love_score=int(total_score)

if love_score<=10 or love_score>=90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")









