from person import Person
class Student(Person):  # Student繼承Person。Person類別裡面的東西複製到Student類別裡面的最上面 
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)