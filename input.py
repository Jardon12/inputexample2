name=input("What is your name?")
print("the name you entered was", name)
while True:
    try:
        greeting="How old are you, " + name+"?"
        age = int(input(greeting))
        break
    except ValueError:
        print("Please put your age in numbers...")
        continue
correction = "Has your birthday already happened?"
birthday = input(correction)
if birthday == "Yes":
    year = 2021 - int(age)
    print(name, ", you were born in: ", year)
else:
    year = 2020 - int(age)
    print(name, ", you were born in: ", year)
