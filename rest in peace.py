x = int(input())
for i in range(x + 1):
    y = input()
    if ('21' in y or int(y) % 21 == 0):
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")


