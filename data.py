# user information
# name, age, date_of_birth

user = {
    "name": "John Doe",
    "age": 23,
    "date_of_birth": "1998-12-31"
}


user = {
    "names": "John Doe",
    "age": 23,
    "date_of_birth": "1998-12-31"
}

def add(x: int, y: int) -> int:
    return x + y

total = add(3, 2)
total2 = add(y=5, x=-4)

class User:
    # constructor
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def greet(self) -> None:
        print(f"Welcome to the app 🚀 {self.name}")
    
    def can_vote(self) -> bool:
        return self.age >= 18

    def save(self) -> str:
        # save into the database
        print("User saved successfully")
        return "1234"



# instantiating a class
user = User("John Doe", 23)
user.greet()
print(user.name)
user.name = "James Doe"
user.greet()
print(user.can_vote())
user.save()

# dataclasses
from dataclasses import dataclass
# decorator

@dataclass
class Student:
    name: str
    level: int
    gender: str
    programme: str

    def greet(cls) -> None:
        print(f"Welcome to the app 🚀 {cls.name}")

student = Student("John Doe", 100, "male", "Computer Science")
print(student.programme)
student.programme = "IT"
print(student.programme)
student.greet()
