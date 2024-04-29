


# marksObtained=[50,60,78,23,79,84,90,98]


marks1=int(input("Enter the marks obtained in Subject 1:"))
marks2=int(input("Enter the marks obtained in Subject 2:"))
marks3=int(input("Enter the marks obtained in Subject 3:"))
marks4=int(input("Enter the marks obtained in Subject 4:"))
marks5=int(input("Enter the marks obtained in Subject 5:"))
marksObtained=[marks1,marks2,marks3,marks4,marks5]

print(f"The marks Obtained by the student are:")
for mark in marksObtained:
    print(mark)


avgMarks=(marks1+marks2+marks3+marks4+marks5)/5    
print(f"The average marks is: {avgMarks}")
