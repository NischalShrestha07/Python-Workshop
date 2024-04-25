#DIFFERENT DATA ACCESSING WAYS USING FOR LOOPS

fruits=["nischal","krishna","hari","shyam"]
for hello in fruits:
    print(hello)
    print(hello.upper())    
    
numbers={1,2,3,4,5,6}    
for num in numbers:
    print(num)


grades={
    'Nischal':5,
    'Naruto':65,
    'Boruto':95,
    'Karsa':56,
    'Krishna':45
}
# print(f"{grades[0]} has scored ")
for name in grades:
    print(f"{name} scored {grades[name]}")


print(grades.values)        