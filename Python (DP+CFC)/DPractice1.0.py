
# fruits=["apple","banana","cheery","kiwi","mango"]
# newList=[]

# for x in fruits:
#     if 'a' in x:
#         newList.append(x)

# print(newList)


# newList1=[x for x in fruits if "go" in x]
# print(newList1)


list1=[]
num=int(input("Enter numbers of elements in list:"))

for i in range(num):
    els =int(input("Enter elememts:"))
    list1.append(els)

    print("Largest elemet is:",max(list1))