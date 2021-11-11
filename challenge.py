#!/Users/christopher.ogbunuzor/.pyenv/shims/python
apples = int(input("how many apples do you want"))
unit = input("what unit shall i use? pls enter kg for kilograms, lb for pounds")
#try:
if unit.lower() == 'kg':
    weight = apples/5
elif unit.lower() == 'lb':
    weight= apples/2.2
else:
    while unit.lower() not in ['kg', 'lb']:
        unit = input("ensure you enter kg for kilograms, lb for pounds")
        if unit.lower() == 'kg':
            weight = apples/5
        elif unit.lower() == 'lb':
            weight= apples/2.2
#except:
    #print("An exception occurred")

    

print("The weight of your apples in " + unit+ "is "+ str(weight))