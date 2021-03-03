import random
flag = True
while flag:
    num = input('Enter number for an upper bound:')
    if num.isdigit():
        print('Let play')
        num=int(num)
        flag = False
    else:
        print('Try again type a number')
randnum = random.randint(1,num)
guess = None
count = 1
while guess != randnum:
    guess = (input('Enter number between 1 and '+ str(num)+': '))
    if guess.isdigit():
        guess = int(guess)
    count += 1
print('Succeed')
print('You guess count is ',count)