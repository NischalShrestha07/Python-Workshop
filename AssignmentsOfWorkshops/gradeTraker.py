


# marksObtained=[50,60,78,23,79,84,90,98]
name=input("Enter Your name:")

if marks1>100 or marks2>100 or marks3>100 or marks4>100 or marks5>100:
    if marks1<0:
         marks1=int(input("Enter the marks obtained in Subject 1:"))
         marks2=int(input("Enter the marks obtained in Subject 2:"))
         marks3=int(input("Enter the marks obtained in Subject 3:"))
         marks4=int(input("Enter the marks obtained in Subject 4:"))
         marks5=int(input("Enter the marks obtained in Subject 5:"))
    
    

marksObtained=[marks1,marks2,marks3,marks4,marks5]

print(f"The marks Obtained by the student are:")
for mark in marksObtained:
    print(mark)

print("")

avgMarks=(marks1+marks2+marks3+marks4+marks5)/5    
print(f"The average marks obtained by {name} is: {avgMarks}")

highestMarks=max(marksObtained)
lowestMarks=min(marksObtained)

print(f"The highest marks obtained by the {name} is:{highestMarks}")
print(f"The lowest marks obtained by the {name} is:{lowestMarks}")