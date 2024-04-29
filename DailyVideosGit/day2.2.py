

class Student:
    college_name="PUSOE"

    def __init__(self,name,age):
        self.name=name
        self.age=age
std1=Student("Nischal",41)
# access instance variable
print(f"Student Name:{std1.name}")
print(f"Student Age:{std1.age}")

# college Details
print(f"College Name: {Student.college_name}")

std1.name="Nischal"
std1.age=21
print(f"Student Name: {std1.name}")
print(f"Student Age: {std1.age}")

print("\n")

Student.college_name="PU"
print("School Name:",Student.college_name)

   