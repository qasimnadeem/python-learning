#A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
        
# r= http_error(4000)
# print(r)

#Tour guide
city = input("Please enter city: ")
match city:
    case 'lhr':
        print("Visit historical places")
    case 'khi':
        print("Visit sea")
    case 'fsd':
        print("Visit industry")
    case _:
        print("Stay at home")
        



