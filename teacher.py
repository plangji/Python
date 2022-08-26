class students:
    
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName= lastName
        self.age = age
        self.email = f'{firstName}{lastName}@gmail.com'
        

    def fullnames(self):
        return f'\nFirstName: {self.firstName}\nLastName: {self.lastName}\nAge: {self.age}\nEmail: {self.email}\nGrade: {self.gradeLevel}'
    
    def fullNames(self):
        return f'\nFirstName: {self.firstName}\nLastName: {self.lastName}\nAge: {self.age}\nEmail: {self.email}'

S1 = students('James', 'John', 23)

class teachers(students):
    def __init__(self, firstName, lastName, age, gradeLevel):
        super().__init__(firstName, lastName, age)
        self.gradeLevel = gradeLevel

  
T1 = teachers('Emmanuel', 'John', 49, 12)
T2 = teachers('Philip', 'Jenny', 30, 9)
print(T1.fullnames())
print(S1.fullNames())