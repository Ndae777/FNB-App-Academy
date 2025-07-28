print("We back")

#strings
#can take double or single qoutes
#three qoutes take any length
messsage = "\"This is a message\"" #i used escape \

messageLong= """
 yes it takes upon any length.
"""

print(messsage)

#index accessing

print(messsage[0]) #prints out T
print(messsage[-1]) #prints out last index
print(len(messsage)) #prints out length of string , including white spaces
print(messageLong.strip()) #removes leading white space
print(messsage.lower()) #convert all characters to lowercase
print(messsage.split(' ')) #returns an arrray

#numberic data

num = 3
print(num) #int
print(type(num))#should tell you what type it is
num2 = 3.14
print(num2) #float

#variables

#must start with letter or underscore  
#must be all lower case  
#use meaningful naming
#use snake casing or underscores

#operators
#addition +
#subtraction -
#multiplication *
#division /
#modules %
#exponents **
#increment +=
#decrement -=

# + concat strings.

#control

if num > 10:
    print("Yes number is great than ten")
elif num > 1:
    print("atleast this number is positive")    
else:
    print("Nah the number is not great than ten")
    
#input variables

num_1 = int(input("Enter the 1st number: "))

#loops
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1,2,3,4,5]

for number in numbers:
    print(numbers)
    
count = 1
while(count<10):
    count += 1


#lists
#fruits is our earlier; , they are 0 index so first item is at index 0.
print(fruits[0])
fruits[0] = "blueberry"
print(fruits[0])

#adding to list
fruits.append("kiwi")
print(fruits)

#adding in between
fruits.insert(1,"orange")
print(fruits)

#removing 
fruits.remove("orange") #remove first instance

#sort
fruits.sort()

#sort in reverse
fruits.sort(reverse=True) 

#tuples

my_tuple = (1,2,3,4,5,6)
tuple1 =(1,2,3,4,5,6)
#concat tuples

conc_tuple = my_tuple + tuple1

#repeatition
rep_tuple =tuple1*3

#sets
my_set = {1,2,3,4,5}
my_set.add(6)
my_set.remove(6)
my_set2= {5,6,7,8,9}
union_set = my_set.union(my_set2) # 1,2,3,4,5,6,7,8,9 rm duplicates
inter_set = my_set.intersection(my_set2 ) #5 #prints common only
diff_set = my_set.difference(my_set2) #1,2,3,4, sets present in one but not the other set

#dictionaries
my_dict= {'apple':3,
          'banana': 5,
          'orange': 2
          }

#print value for apple
print(my_dict['apple'])

#adding to dict
my_dict['candy'] = 4

#changing in dict
my_dict['candy'] = 100




