
fruits=["apple","banana","cheery","kiwi","mango"]
newList=[]

for x in fruits:
    if 'a' in x:
        newList.append(x)

print(newList)


newList1=[x for x in fruits if "go" in x]
print(newList1)
