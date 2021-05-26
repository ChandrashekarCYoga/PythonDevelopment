import re

string = 'search inside of this text please!'

a = re.search('this', string)

print(a)

print(a.span())

print(a.start())

print(a.end())

print(a.group())

a = re.search('thIs', string)

print(a)


pattern = re.compile('this')

a = pattern.search(string)

b = pattern.findall(string)

c = pattern.fullmatch(string)

d = pattern.match(string)

print(a.group())

print(b)
print(c)
print(d)

