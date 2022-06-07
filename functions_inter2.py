# Q1 part 1
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)


# Q1 part 2
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)


# Q1 part 3
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


# Q1 part 4
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)


# Q2
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(li):
    for x in range(0, len(li)):
        k = list(li[x].keys())
        v = list(li[x].values())
        sen_print = ""
        for i in range(0, len(k)-1):
            sen_print += (f"{k[i]} _ {v[i]}, ")
        sen_print += (f"{k[len(k)-1]} _ {v[len(v)-1]}")
        print(sen_print)


print(iterateDictionary(students))


# Q3
def iterateDictionary2(key_name, some_list):
    k = key_name
    for x in range(0, len(some_list)):
        print(some_list[x][k])


print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))


# Q4
def printInfo(_dict):
    for y in _dict:
        print(len(_dict[y]), y)
        for d in _dict[y]:
            print(d)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
