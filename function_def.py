# 함수 정의


def dummy():
    pass


def my_function():
    print('Hello World')


def time(a, b):
    return a ** b


def none():
    return


def swap(a, b):
    return b, a


dummy()
my_function()
print(time(2, 10))
print(none())

# 함수도 객체다.
print(dummy, type(dummy))
t = time
print(t(2, 5))

a = 10
b = 20

a, b = swap(a, b)
print(a, b)
