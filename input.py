name=input("What is your name?")
print("the name you entered was", name)
greeting="How old are you, " + name+"?"
age = input(greeting)
correction="Has your birthday already happened?"
birthday=input(correction)
if birthday=="Yes":
    year=2021-int(age)
    print(name, ", you were born in: ", year)
else:
    year=2020-int(age)
    print(name, ", you were born in: ", year)