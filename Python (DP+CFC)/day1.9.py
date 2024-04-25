

friend={
    'name':'Nischal',
    'age':21
}


# when we have to check the key exist in the set or not do this
if 'hello' in friend:
    print("It exist!!")
else:
    print("It doesnt exist!!")
        
        
        
        
friend["isNepali"]=True

print(f"Your name is: {friend['name']}")
print(f"Your age is: {friend['age']}")

# Below one is the JS syntax
# print(`These are your details:`${friend})

print(f"These are your details:\n {friend}");
