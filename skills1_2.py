number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Define lambdas for each task
odds = lambda x: x % 2 != 0
evens = lambda x: x % 2 == 0
long_words = lambda x: len(x) >= 4

smallest = lambda x, y: x if x < y else y
largest = lambda x, y: x if x > y else y

halvsies = lambda x: x / 2.0
word_length = lambda x: len(x)

sum_function = lambda x, y: x + y
multiply = lambda x, y: x * y
join_function = lambda x, y: x + " " + y

# define new filter function
def new_filter(my_function, my_list):
	new_list = []
	for item in my_list:
		if my_function(item):
			new_list.append(item)
	return new_list

# This funciton broke in an interesting way.
# It only prints the first value of the desired new_list.
# This is due to a mix of spaces and tabs (which count as just 1 space)
# BUT, the return new_list only has one tab (aka space, so it SHOULD be the leftmost...)
#
# def broken_new_filter(my_function, my_list):
#     new_list = []
#     # print "MY LIST"
#     for item in my_list:
#     	print item
#     	if my_function(item) == True:
#     		new_list.append(item)
# 	return new_list

#print "identical(?) new filter that doesn't work...? ", broken_new_filter(odds, number_list)

# define new map funciton
def new_map(my_function, my_list):
	new_list = []
	for item in my_list:
		new_list.append(my_function(item))
	return new_list

# define new reduce function
def new_reduce(my_function, my_list):
	reduced = my_list[0]
	for item in my_list[1:]:
		reduced = my_function(reduced, item)
	return reduced

# Test new functions
print "Evens: ", new_filter(evens, number_list)
print "Long words: ", new_filter(long_words, word_list)

print "Halvsies: ", new_map(halvsies, number_list)
print "Word lenght: ", new_map(word_length, word_list)

print "Sum: ", new_reduce(sum_function, number_list)
print "Multiply: ", new_reduce(multiply, number_list)
print "Join: ", new_reduce(join_function, word_list)

print "Smallest: ", new_reduce(smallest, number_list)
print "Largest: ", new_reduce(largest, number_list)


