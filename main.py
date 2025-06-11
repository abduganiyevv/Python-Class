class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

persons = [
    Person("Ali", 19),
    Person("Vali", 22),
    Person("Hasan", 25),
    Person("Husan", 21),
    Person("Zafar", 30),
    Person("Kamol", 28),
    Person("Shoxrux", 24),
    Person("Javlon", 27),
    Person("Dilshod", 26),
    Person("Anvar", 29),
    Person("Farruh", 23),
    Person("Sardor", 20),
    Person("Bekzod", 22),
    Person("Rustam", 31),
    Person("Islom", 33),
    Person("Jahongir", 35),
    Person("Oybek", 19),
    Person("Sherzod", 24),
    Person("Bobur", 21),
    Person("Aziz", 20),
]

a = 0

for person in persons:
    a += person.age
print(a)


    
# oldest_person = max(persons, key=lambda person: person.age)
# print(person.name)

