class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_name=last_name
        self.age=age


    def full_name(self):
        return f"My name is {self.first_name}, {self.last_name}"

    def year_of_birth(self):
        return f"You were born on August{2022-self.age}"

    def initial(self):
        return  f"{self.first_name[0],{self.last_name[0]}}"        
        