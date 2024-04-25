name=["nischal","rohan","sushil"]
print(name)
name.append("Niraj")
name.extend("dipan")
name.insert(0,"Hikmat")
name.insert(1,"rohan")
# name.pop("rohan")

del name[0]
name.reverse()
subName=name.copy()
print(f"These are datas of name: {name}")
print()
print(F"These are the datas of subNames:{subName}")
number=subName.count("rohan")

print("\n")
print(f"The number of time string repeated is:{number}")
