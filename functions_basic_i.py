# #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

## this will print 5


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

## this will throw an error, because the first function has not been defined


# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

## this will print 5


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

##this will print 5


#5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

##this will print 5, but then print none, because the function returns nothing by default if there is no return statement.


#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

##this will print 3, 5 and throw an error, because you can't add none and none.


# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

# # 25 will be printed


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

# # 100 will be logged, and then 10 will be returned and printed.


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# # 7, 14, and then 21 will be printed


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

# #  8 will be outputted


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# # 500 will print
# # then 500 again
# # then 300 will print
# # then 500 will print


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# # 500 will print
# # 500 will print again
# # 300 will print
# # 500 will print


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

# # 500 will print
# # 500 will print again
# # 300 will print
# # 300 will print again, because b was assigned to the value of the function.


#14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

# # 1, then 3, then 2 will print


# #15
# def foo():
#     print(1) # # 1 will print
#     x = bar() # 5 is assigned, and 3 is printed
#     print(x) # 5 is printed
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo() # 10 is returned, 1 is printed, 3 is printed, then 5 is printed
# print(y) # 10 is printed
