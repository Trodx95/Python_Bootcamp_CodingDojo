x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
# print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]


students[0]["last_name"]= 'bryant'
# print(students)



sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0]='Andres'
# print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
# print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(len(students)):
        print(i)
        print(students[i])
        
iterateDictionary(students) 

def iterateDictionary2(first_name, some_list):
    for n in range(len(students)):
        print(n)
        print(students[n])

iterateDictionary(students) 

def iterateDictionary2(last_name, some_list):
    for m in range(len(students)):
        print(m)
        print(students[m])

iterateDictionary(students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        # print(some_dict[key])
        for value in some_dict[key]:
            print(value)
        print()

        

printInfo(dojo)

# def interateDictionary(key_name, some_list)
#     for x2 in range of(len(locations, instructors):)
#         printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

    
    # for key in students.keys(): 
    #     print(key)
    # for val in students.key()
    #     print
    

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




