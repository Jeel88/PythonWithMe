class Student:

    school = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

    @classmethod
    def change_school(cls, school):
        cls.school = school

    @staticmethod
    def is_adult(age):
        return age >= 18


student1 = Student("Jeel", 20)

student1.display()

print(Student.school)

Student.change_school("XYZ College")

print(Student.school)

print(Student.is_adult(20))


class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


dog = Dog()

dog.speak()


class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount


account = BankAccount(5000)

print(account.balance)

account.balance = 8000

print(account.balance)


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


person = Person("Jeel")

print(person)