myString="This is a string"
print(str(myString) +" is of the data type " +  str(type(myString))) 
firstString="Water"
secondString="Fall"
thirdString=firstString + secondString
print(thirdString)

#Working with the input String
name = input("What is your name: ")
print(name)

#Formatting Strings
color= input("What is your favorite color: ")
animal= input("What is your favorite animal: ")
print("Hello {}, you like {} and {}, We love that too!!".format(name,color,animal))