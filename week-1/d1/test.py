# print(type(24))
# print(type(3.9))
# print(type(3j))

first_name ="Tom"
last_name ="Rodriguez"
age = 27

# print("Hi my name is {} {} and i am {} years old".format(first_name, last_name, age))

# print(f"hi my name is {first_name} {last_name} and iam {age} years old..")

# print(first_name.capitalize(), last_name.capitalize())

# print(True)  bool
# print(False)

# if first_name:
#     print("yes")
# else:                      bool 
#     print("no")

# brothers =['tyler' , 'curtis', 'joe'] arrays list
# brothers.append("bob")
# print(brothers)

# person = {
#     'first-name': 'tom', 
#     'last-name': 'rodriguez',
#     'age': 27

# }   

# brothers =[
#     {
#     'first-name': 'tom', 
#     'last-name': 'rodriguez',
#     'age': 27
#     },
#         {
#     'first-name': 'tom', 
#     'last-name': 'rodriguez',
#     'age': 27
    
#     },
#         {
#     'first-name': 'tom', 
#     'last-name': 'rodriguez',
#     'age': 27
#     },
# ]

# #brothers -> list [index] -> dictionaries['key']
# print(brothers[1]['first-name'])

# person2 =('tom')

## conditionals 

# age = 34

# if age >= 65:
#     return "you may enter and get a free drink" 
# elif age >=21:
#     return"you may enter"
# else: 
#     return "you shall not pass"

brothers = ['tyler' , 'curtis' , 'joe', 'bob']

def randomize_list(new_list):
    return_list =[]
    for item in new_list:
        random_num = random_randint(0 , len(new_list) - 1)
        item - new_list[random_num]
        return_list.append(item)
    
    return return_list

#     print(randomize_list(brothers))

# def run_times(num):
#     for indx in range(num):
#         print(randomize_list(new_list))

# print run_times(5, brothers)

def add(num1, num2=10, num3=3):
    return (num1 + num2) * num3

print(add(5, 7, 2))