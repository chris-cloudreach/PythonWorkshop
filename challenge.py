apples = int(input("how many apples do you want"))
unit = input("what unit shall i use? pls enter kg for kilograms, lb for pounds")
#try:
if unit == 'kg':
    weight = apples/5
elif unit == 'lb':
    weight= apples/2.2
else:
    print("You have to specify the right unit, pls enter kg or lb")
#except:
    #print("An exception occurred")

    

print("The weight of your apples in " + unit+ "is "+ str(weight))