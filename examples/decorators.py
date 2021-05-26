# @classmethod
# @staticmethod


def hello():
    print('hellllooooooooo')


greet = hello

del hello

print(greet())


# Higher order function HOC
def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)

print(a)


def greet2():
    def func():
        return 5
    return func


b = greet2()
print(b())

# Decorator


def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func


@my_decorator
def hello1():
    print('helooooooooooooooo')


@my_decorator
def bye():
    print('see you later')


hello1()
bye()

hello2 = my_decorator(hello1)

hello2()
my_decorator(hello1)()


def my_decorator(func):
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func


@my_decorator
def helloagain(greeting):
    print(greeting)

helloagain('hiiiii')



def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func


@my_decorator
def helllo(greeting, emoji=':('):
	print(greeting, emoji)

helllo('hiiii')


