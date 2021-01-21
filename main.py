# read input
# name = input("What is your name?")
# print("Hello " + name)
#
# birth_year = input("What is your birth year: ")
# age = 2020 - int(birth_year)
# print("You are " + str(age) + " years old")

# Strings are immutable
course = 'Distrbuted Systems'
print(course.find('strbuted'))
print(course.replace('Systems', 'fu'))
print(course)

# in operator
print('Systems' in course)

# conditionals
temperature = 35
if temperature < 32:
    print('Less than')
elif temperature == 35:
    print('Equal to')
else:
    print("Greater than or equal to")

i = 0
while i < temperature:
    print(i)
    i += 1

# Lists
names = ['Stephon', 'Cody', 'Chanon']
print(names)
print(names[2])

print(names[-2])  # goes in reverse order

names[0] = 'Khalil'
print(names)
print(names[0:2])

# List methods
names.append('Stephon')
print(names)
names.insert(0, 'Phillip')
print(names)

# for loops
numbers = range(5, 10, 2)  # start, end, step
print(numbers)
for number in numbers:
    print(number)

for number in range(20):
    print(number)

nums = (1, 2, 2, 2, 2, 2, 3)
print(nums.count(2))  # return how many instances of that value
print(nums.index(3))  # returns first instance of value (index)

for number in nums:
    if number % 2 != 0:
        print(number)

#2D Lists
num_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(num_matrix)
