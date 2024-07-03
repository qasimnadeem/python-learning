#Defining Functions: We can create a function that writes the Fibonacci series to an arbitrary boundary:
#Security of code, on-demand execution of code

# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# Now call the function we just defined:
# fib(2000)

# fib(500)


#Default arguments

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



# def standard_arg(pt):
#     print(pt)

# standard_arg(2)
# standard_arg(pt=2)


# def pos_only_arg(p,/,arg):
#     print(p,arg)

# pos_only_arg(10,20)

#To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.
# def kwd_only_arg(*, arg):
#     print(arg)

# kwd_only_arg(arg=3)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# Lambda Expressions are small anonymous functions can be created with the lambda keyword. 
# Lambda functions can be used wherever function objects are required. 
# They are syntactically restricted to a single expression. 
# Semantically, they are just syntactic sugar for a normal function definition. 
# Like nested function definitions, lambda functions can reference variables from the containing scope:

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

# Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)