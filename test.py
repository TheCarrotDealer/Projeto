from turtle import distance
from graphics import * 
def myFunc(e):
    return e['distance']

l = 1
a = 2
e = 3
c = 4
thing=[l,a,e,c]

for i in thing:
    print(i)
    print(thing)
    thing.remove(i)
print(thing)


