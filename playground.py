# build an app that accepts a number of student scores, prints back the scores and calculates the sum of it.
# scores: str = input("Enter scores seperated by a single space: ")

# todo: handle exceptions
# scores_in_str: list[str] = scores.split(" ")
# scores_in_int: list[int] = []
# for score in scores_in_str:
#     scores_in_int.append(int(score))

# print("Your scores:", scores_in_int)
# print("Total scores is: ", sum(scores_in_int))


# name = input("Name of Student 🌚: ")
# print(f"Your name is {name} 🔥")

# answer = input("What is the capital of Ghana 🇬🇭? ")

# if answer.upper() == "Accra".upper():
#     print("yaayyyyyy, you got it. 🐓")
# else:
#     print("noppeee, it's wrong. 😭")

# Build a system that accepts the numeric months of the year (1 - 12) and based on the input, print the name of the month (January - December).

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

value = int(input("Enter the month number (1 - 12): "))
print(months.get(value, "Month is invalid. 🤷🏽‍♂️"))

# using the match case statement
match value:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case _:
        print("Month is invalid. 🤷🏽‍♂️")
