"""
Your module description
"""
x=("apple","kiwi" ,"banana")
print(type(x))
print(type(list(x)))

customer = {
    "name":"kiran",
    "vahicle":"AudiQ7,"
}
print(customer["vahicle"])
customer.get("type","true")
print(customer)
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
myFruitList[2] = "orange"
print(myFruitList)
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[1])
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
myFavoriteFruitDictionary["Kiran"] = "mango"

myFavoriteFruitDictionary["Saanvi"] = "orange"
print(myFavoriteFruitDictionary)
del (myFavoriteFruitDictionary ["Paulo"])
print(myFavoriteFruitDictionary)
namelist = ["kiran" , "abeeha" , "Iggy"]
for x in namelist:
    print(x)
    newname = x.capitalize()
    print(newname)




