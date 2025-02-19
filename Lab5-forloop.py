"""
Your module description
"""
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))    
    
    
    
var=1    
print(var > 0)
print(not (var <= 0))
print(var != 0)
print(not (var == 0))


x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
