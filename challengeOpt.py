#!/Users/christopher.ogbunuzor/.pyenv/shims/python
apples = int(input("how many apples do you want "))
unit = input("what unit shall i use? pls enter kg for kilograms, lb for pounds")

while unit.lower() not in ['kg', 'lb']:
    unit = (input("Ensure you enter kg for kilograms, lb for pounds "))

if unit.lower() == 'kg':
    weight = apples/5
elif unit.lower() == 'lb':
    weight= apples/2.2

print("The weight of your apples in " + unit+ "is "+ str(weight))