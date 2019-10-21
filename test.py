#### class 1

message = "Hafeez"
helloWorld = """Hafeez is possessed by 

====> demons"""

greeting = """just kidding"""
message1 = 'Hafeez'

print(message1)
print(helloWorld[10:19])
print(helloWorld[:6])
print(len(helloWorld[0:6]))
print(len(helloWorld))
print(message.lower())
print(message.upper())
print(message.count("e")) # gives count of string occurances
print(message.count("o")) 
print(message.replace("ee", "oo"))
print(message)



print(helloWorld+greeting) 
print('{}, {}. Welcome'.format(helloWorld, greeting))

print(f'{helloWorld}, {greeting.upper()}. Welcome')


print(greeting.split()) 
# print(help(greeting.split())) 


#### class 2

num =2
print(type(num))
print(2+2)
print(2-12)
print(2%2)
print(2/2)
print(13//2) # floor division
print(2*2) 
print(2**4) # exponent
num *= 10
print(num)

num/=3
num1 = 12
num2 = "87"
num3 = "22"
print(round(num,2))
print(num == num1)
print(int(num2) + int(num3))


### Class 3
### lists, tupes and sets
print("List, tuples and sets")

lists = ["php","nodejs", "reactjs","angularJs"]
print(len(lists))
print(lists[2])
# print(lists[56])

lists.append("Sailsjs")
print(lists)

lists.insert(2, "ExpressJs")
print(lists)

lists1 = ["HTML", "CSS"]

print(lists.extend(lists1)) # if insert is used it adds [['HTML', 'CSS'], 'php', 'nodejs', 'ExpressJs', 'reactjs', 'angularJs']
print(lists)

print(lists.remove("php"))
print("After removing a entry: ", lists)
lists.reverse()
print("reversed: ", lists)

lists.sort()
print("sorted : ", lists)

numLists = [12,22,9,41,9,5]
numLists.sort()
print("sorted : ",numLists)
numLists.sort(reverse=True)
print("sort : ",numLists)

print("Sorted without altering the original: ",sorted(lists1))
print("Min",min(numLists))
print("Max",max(numLists))
print("Sum",sum(numLists))


print("index of: ", lists.index("nodejs"))
print("index of: ", "nodejs" in lists)

print("")
print("")
print("for starts")
print("")
print("Simple for loop")
for item in lists:
    print(item)


print("")
print("")
print("For loop with enumrate")
for index,item in enumerate(lists):
    print(index,item)

print("")
print("")
print("For loop with enumrate with start value")
for index,item in enumerate(lists, start=2):
    print(index,item)

print("")
print("")
print("stringify array with joining ,")
temp = ', '.join(lists)
print(temp)


print("")
print("")
print("Major differences list and tupules, tupules are immutable")


print("")
print("")
print("tupules")

tuples_1 = ("Bin" ,"Tin","Sin","Jin")
print("tupules behave exactly like lists")
print(tuples_1)

print("")
print("")
print("sets")

sets_1 = {"Bin" ,"Tin","Sin","Jin", "Jin","Tin"}
sets_2 = {"Flag" ,"Tag","Sin","Jin", "Jag","Blah"}
print("unordered and no duplicates")
print(sets_1)
print(sets_2)
print("Intesections of 2 sets: ", sets_1.intersection(sets_2))
print("Union of 2 sets: ", sets_1.union(sets_2))
print("differences of 2 sets: ", sets_1.difference (sets_2))


print("")
print("")
print("creating empty lists")
empty_lst = []
empty_lst = list()
print(empty_lst)

print("")
print("")
print("creating empty tuple")
empty_tpl = ()
empty_tpl = tuple()
print(empty_lst)

print("")
print("")
print("creating empty set")
# empty_set = [] # incorrect
empty_set = set()
print(empty_set)


# class 4 
# Dictionaries


print("")
print("")
print("Dictionaries")
studs = {"name":"hafeez","age":21,"qualifications":"BE"}

print("")
print("")
print("Accessing dictionaries")
print("Age: ",studs["age"])
print("non existing phone with 'in': ","phone" in studs)
print("non existing phone with 'get': ", studs.get("phone"))
studs["phone"] = 12341234234
print("After adding phone to diction: ",studs )
studs.update({
    "name":"Hafeez Khan",
    "age":26,
    "phone":22222
})
print("Updating a dicstiosn", studs)


del studs['qualifications']
print("Deleting from diction: ",studs )
print("Length of ducto: ",len(studs))
print("Keys of ducto: ",studs.keys())
print("values of ducto: ",studs.values())
print("items of ducto: ",studs.items())



print("Looping throu ducto")
for keys, values in studs.items():
    print(keys, values)
