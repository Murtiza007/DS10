#functions

def greet():
    print("Greetings from the function!")


def greet2():
    print("AADAB")
    greet()



# function --  block of code to perform a task
# establishes control --- which part of code to execute
# customises sequence of execution
# reusable code


def odd_even():
    a=int(input("enter a number"))
    if(a%2==0):
        print("even")
    else:
        print("odd")
        
def pos_neg():
    a=int(input("enter a number"))
    if(a>=0):
        print("positive")
    else:
        print("negative")



odd_even()
odd_even()
odd_even()
