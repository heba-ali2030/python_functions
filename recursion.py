##recursion
'''a recursive function (a function that calls itself)'''
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return( x * factorial (x-1))
# number = 3
# print(factorial(number))

# def recursor():
#     recursor()
# recursor()



## Python Anonymous/Lambda Function
'''an anonymous function is a function that is defined without a name'''

# example of lambda function that doubles the input value.
# double = lambda x : x * 2
# print(double(5))

# numbers = [1, 5, 4, 6, 8, 11, 3, 12]
# new_numbers = list (filter(lambda x: (x % 2 == 0 ), numbers))

# new_numbers2 = list (map(lambda x: x*2, numbers))
# print(new_numbers2)


#Python Global, Local and Nonlocal variables

# x = 'global'
# def name ():
#     print(x)
# name()
# print(x)


# def name():
#     x ='local'
#     print(x)
# name()
# print(x)


# a = 1 #global variable
# def add():
#     global a
#     a = a + 2
#     print(a)

# add()
# print(a)


def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)
