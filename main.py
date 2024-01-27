print("Hello World!")

# primitive data types
# int, float, str, bool, None
age = 20 # const age = 24
age: int = 20
weight: float = 70.5 # weight = 70.5
name: str = "John" # name = "John" 
is_active: bool = True # is_active = True, is_active = False
weather: None = None # weather = None
print(age, weight, name, is_active, weather)
# print(type(age))

# using str REPL - Read Evaluate Print Loop
print(name.capitalize())
print(name.upper())
print(name.lower())

# list, tuple, set, dict (collections)
names = ["John", "Jane", "Jack", "John"] # names: list[str] = ["John", "Jane", "Jack"]
ages = [20, 30, 40] # ages: list[int] = [] or use list()
print(names)
print(ages)
print(names[0])
print(len(names))

# tuple
point = (-3, 5) # point: tuple[int, int] = (-3, 5)
print(point)
print(point[0], point[1]) # x, y = point # tuple destructuring

# set
names = {"John", "Jane", "Jack", "John"} # names: set[str] = {"John", "Jane", "Jack"}
print(names)

numbers = [2, 3, 4, 2, 3, 4, 4,4, 8, 9]
unique_numbers = set(numbers)
print(numbers, unique_numbers)

# dict
person = {"name": "John", "age": 23, "is_active": True} 
print(person)
print(person["name"])
print(person.get("contact", "N/A"))
person["name"] = "Jane"
print(person)

# functions // js: const add = (a, b) => a + b or function addANumber(a, b) { return a + b }
def say_hello():
    print("Hello World!")

say_hello()

def add(x: int, y: int) -> int:
    return x + y

sum = add(2, 3)
print(sum)
# loops

# dataclasses

# pytest introduction

# fastapi introduction