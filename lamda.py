# lambda 함수


def blahblah(x):
    return x**2


for i in range(10):
    print("{0}:{1}".format(i, blahblah(i)), end=' ')
else:
    print()


for i in range(10):
    print("{0}:{1}".format(i, (lambda x: x**2(i)), end=' '))
else:
    print()


strings = ['foo', 'a', 'card', 'bar', 'abab', 'a']
strings.sort(key=lambda x: len(x), reverse=False)
print(strings)

strings.sort(key=lambda x: strings.count(x), reverse=False)
print(strings)
