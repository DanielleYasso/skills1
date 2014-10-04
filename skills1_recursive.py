number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# # Define lambdas for each task
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
    if my_list == []:
        return my_list
    else:
        if my_function(my_list[0]):
            return [ my_list[0] ] + new_filter(my_function, my_list[1:])
        else:
            return new_filter(my_function, my_list[1:])
        
# define new map funciton
def new_map(my_function, my_list):
	if my_list == []:
		return my_list
	else:
		return [my_function(my_list[0])] + new_map(my_function, my_list[1:])

# define new reduce function
def new_reduce(my_function, my_list):
    if len(my_list) == 1:
        return my_list[0]
    elif my_list = []:
        return None
    else:
        return my_function(my_list[0], (new_reduce(my_function, my_list[1:])))

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


