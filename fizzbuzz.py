#coded in PyCharm
#one of my first python scripts lol
#python is one of the stupidest but also one of the easiest languages that
# I learned/learn.

for i in range(100):
    if (i% 3== 0 & i%5 == 0):
        print("Fizzbuzz")
    if (i%3 == 0):
        print("Fizz")
    if (i%5 == 0):
        print("Buzz")
    else:
        print(i)