# def greet():
#     print("Hello, Rebeka") 
# greet()    

# def greet(name):
#     print(f"Namaste, {name}") 
# greet("Ronaldo")    
# greet("Nischal")    
# greet("Cristiano")    

# WAY 1:
def addition(m,n):
    return m+n
print(addition(4,5))    

# WAY 2:
def sum(m,n):
    # return n+10
    print(m+n+10)
sum(10,10)    
# sum(10)

# WAY 3:
def add(a,b):
    sum=a+b
    print("The sum of two entered numbers is:",sum)

add(6,4)

# WAY-4:-
## Lamda is also called as Anymonous Function in Python

join=lambda a,b:a+b
print(join(45,5))

#   WAY-> 5
# IMPORTANT ARGUMENT TO TAKE MULTIPLE ARGUMENTS:(*args)
def test(*args):
    print(args)
test(1,2,3,4,5,6,7)    
