print("Weather Formats:")
print("1. Sunny")
print("2. Rainy")
print("3. Snowy")

weatherCondition = int(input("Choose the current weather conditions (1-3): "))
if weatherCondition == 1:
        temp = int(input("Enter the current temperature: "))
        if 34 <= temp <= 50:
            print("Wear Shorts and a T-shirt! It's too Hot Outside.")
        else:
            print("Invalid temperature for sunny weather.")
elif weatherCondition == 2:
        temp = int(input("Enter the current temperature: "))
        if 10 <= temp <= 20:
            print("Wear a Raincoat! It's raining heavily Outside.")
        else:
            print("Invalid temperature for rainy weather.")
elif weatherCondition == 3:
        temp = int(input("Enter the current temperature: "))
        if 0 <= temp <= 10:
            print("Wear Jacket and Gloves! Snowfall is happening.")
        else:
            print("Invalid temperature for snowy weather.")
else:
        print("Invalid Choice!.")




# # print("Weathers Formats:")
# # print("1. Sunny")
# # print("2. Rainy")
# # print("3. Snowy")
# # weatherCondition=int(input("Choose the current weather conditions(1-3): "))

# # if(weatherCondition>=4):
# #     print("You enter Wrong input")
    
# # temp=int(input("Enter the current temperature:-"))
# # if(weatherCondition==1):
# #     if(temp>=34):
# #         print("Wear Shorts and a T-shirt! Its too Hot Outside.")

# # elif(weatherCondition==2):
# #     if(temp>=10 and temp<=20):
# #          print("Wear RainCoat! Its raining Heavily Outside.")
        
# # elif(weatherCondition==3):
# #     if( temp>=-50 and temp<=0):
# #         print("Wear Jacket and Gloves! Snowfall is happening.")
        
# # else:
# #     print("Invalid Choice! Enter the correct Datas again. Thanks you")
       


# # weather = input("What is the current weather condition? (sunny, rainy, snowy): ").lower()
# # temperature = int(input("What is the temperature in Celsius?: "))

# # if weather == "sunny":
# #     if temperature > 25:
# #         print("Wear shorts and a t-shirt.")
# #     elif temperature > 15:
# #         print("Wear shorts and a light shirt.")
# #     else:
# #         print("Wear shorts and a long-sleeve shirt.")
# # elif weather == "rainy":
# #     print("Wear a raincoat and waterproof shoes.")
# # elif weather == "snowy":
# #     print("Wear a jacket, gloves, and boots.")
# # else:
# #     print("Sorry, I don't have a recommendation for that weather condition.")
# # 

# name="Nischal Shrestha"
# print(name[0:7])

num=int(input("enter the number"))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    # num=num+1
    