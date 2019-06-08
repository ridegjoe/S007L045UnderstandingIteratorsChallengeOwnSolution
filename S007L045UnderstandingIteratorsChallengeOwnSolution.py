# # 1ST EXAMPLE FOR ITERABLE OBJECT: STRING
# string = "1234567890"
#
# for char in string:
#     print(char)


# # 2ND EXAMPLE FOR ITERABLE OBJECT
# string = "1234567890"
#
# # for char in string:
# #     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) # 10 steps OK
#
# print(next(my_iterator)) # 11th step leads to error

# 3RD EXAMPLE FOR ITERABLE OBJECT: THEY BOTH DO EXACTLY THE SAME THING
# Second example is actually what happening in the first case.
# 1st case 'for' is implicitly creating an iterator from the iterable string object.
# string = "1234567890"
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

# BEGINNING OF CHALLENGE
# Create a list of items (you may use either strings or number in the list),
# then create an iterator using the iter() function
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item
#
# hint: use the len() function rathre than counting the number of items in the list

# MY OWN SOLUTION
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_iterator = iter(week)

for range in week:
    print (next(week_iterator))

# OFFICIAL SOLUTION

my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter (my_iterator)

for i in range(0,len(my_list)):
    next_item = next (my_iterator)
    print(next_item)
