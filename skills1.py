# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# make my own filter function
def filter(my_function, list):
    return my_function(list)

print filter((lambda x: x % 2 != 0), number_list))

print "*******************"

print "Using filter, map, and reduce:"

# all_odd, all_even, long_words
print "Odds: ", filter((lambda x: x % 2 != 0), number_list)
print "Evens: ", filter((lambda x: x % 2 == 0), number_list)
print "Long words: ", filter((lambda x: len(x) >= 4), word_list)

# smallest, largest
print "Smallest: ", reduce((lambda x, y: x if x < y else y), number_list)
print "Largest: ", reduce((lambda x, y: x if x > y else y), number_list)

# halvsies, word_length
print "Halvsies: ", map((lambda x: x / 2.0), number_list)
print "Word length: ", map((lambda x: len(x)), word_list)

# sum, multiply, join, average
sum_function = lambda x, y: x + y
print "Sum: ", reduce(sum_function, number_list)
print "Multiply: ", reduce((lambda x, y: x * y), number_list)
print "Join: ", reduce((lambda x, y: x + " " + y), word_list)
print "Average: ", reduce(sum_function, number_list) / len(number_list)

print "*******************"

print "Using list comprehension:"

# all_odd, all_even, long_words
print "Odds: ", [x for x in number_list if x % 2 != 0]
print "Evens: ", [x for x in number_list if x % 2 == 0]
print "Long words: ", [x for x in word_list if len(x) >= 4]

# halvsies, word_length
print "Halvsies: ", [x / 2.0 for x in number_list]
print "Word length: ", [len(x) for x in word_list]

print "*******************"

print "Using all separate funcitons:"

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for num in number_list:
        if num % 2 != 0:
            new_list.append(num)
    return new_list

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for num in number_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) >= 4:
            new_list.append(word)
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest = number_list[0]
    for number in number_list[1:]:
        if number < smallest:
            smallest = number
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest = number_list[0]
    for number in number_list:
        if number > largest:
            largest = number
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = []
    for number in number_list:
        num = number / 2.0
        new_list.append(num)
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list:
        new_list.append(len(word))
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = number_list[0]
    for number in number_list[1:]:
        total += number
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = number_list[0]
    for number in number_list[1:]:
        total *= number
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    string1 = ""
    for word in word_list:
        string1 += (word + " ")
    return string1

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    average = sum_numbers(number_list) / len(number_list)
    return average

print "Odds: ", all_odd(number_list)
print "Evens: ", all_even(number_list)
print "Long words: ", long_words(word_list)
print "Smallest: ", smallest(number_list)
print "Largest: ", largest(number_list)
print "Halvsies: ", halvesies(number_list)
print "Word length: ", word_lengths(word_list)
print "Sum: ", sum_numbers(number_list)
print "Multiply: ", mult_numbers(number_list)
print "Join: ", join_strings(word_list)
print "Average: ", average(number_list)