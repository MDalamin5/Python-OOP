# function is a first class object 

def double_decker():
    print('Starting the double decker')

    def inner_fun():
        print('Inside the inner')
        return 400

    return inner_fun


# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('work Started')
    # print(work)
    work()
    print('Work ended')

# do_something(32)

def coding():
    print('Coding in python')

# do_something(coding)

def slepping():
    print('sleeping and dreaming in python')

do_something(slepping)