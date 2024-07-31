
# method 1

num_list = [1,2,3,4,5]
num_list.append(8)
print(num_list)
 
# method 2

list = [1,2,3,4,5]
list.clear()
print(list)



#method 3

list_count = ["Mango", "Apple", "banana", "cherry", "papaya", "Mango", "banana"]
print(list_count.count("Mango"))

#method 4

fruits = ["Mango", "Apple", "banana", "cherry"]
other_fruits =["papaya", "Mango", "banana"]
fruits.extend(other_fruits)
print(fruits)

#method 5

fruits = ["Mango", "Apple", "banana", "cherry"]
print(fruits.index("cherry"))

#method 6
fruit = ["banana","cherry","grape"] 
fruit.insert(1,"apple") 
print(fruit)

#method 7

fruits = ["apple", "mango", "cherry"] 
fruits.pop() 
print(fruits)

#method 8

lis = ['a', 'b', 'c']
lis.remove("b")
print(lis)

#method 9

list1 = [1, 2, 3, 4, 7, 2, 6] 
list1.reverse() 
print(list1) 

#method 10
number = ['1','4','3','2','6']
number.sort()
print(number)

#method 11

numbers = [23,25,65,21,98]
print(min(numbers))

#method 12
numbers = [23,25,65,21,98]
print(max(numbers))

#Dictionary 

this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
print(this_dic)



# Dictionary Method

#method1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(len(thisdict))

#method 2

x = ('mango', 'apple', 'banana')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#method 3
this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
print(this_dic.get("Color"))

#method 4
this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
print(this_dic.items())

#method 5
this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
print(this_dic.keys())

#method 6
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)


#method 7 

this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
this_dic.setdefault("Color","White")
print(this_dic)


#method 8

car = {
  "Animal" : "Cat",
  "age"    : "One year"
  
}
car.update({"color": "White"})
print(car)

#method 9

this_dic = {
    "Animal" : "Cat",
    "Color"   : "Brown",
     "age"    : "One year"
}
x=this_dic.values()
print(x)

