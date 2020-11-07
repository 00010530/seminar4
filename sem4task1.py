def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


num = input('Number: ')
num = int(num)
if num > 0:
    countdown(num)
else:
    countup(num)
