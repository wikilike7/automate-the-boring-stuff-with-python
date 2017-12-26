import random


def hello(name):
    print('Hello ' + name)
    print(len(name))


hello('Alice')
hello('Bob')


def get_annwer(answernumber):
    if answernumber == 1:
        return 'It is certain'
    elif answernumber == 2:
        return 'It is decidedly so'
    elif answernumber == 3:
        return 'Yes'
    elif answernumber == 4:
        return 'Reply hazy try again'
    elif answernumber == 5:
        return 'Ask again later'
    elif answernumber == 7:
        return 'My reply is no'
    elif answernumber == 8:
        return 'Outlook not so good'
    elif answernumber == 9:
        return 'Very doubtful'


print(get_annwer(random.randint(1, 9)))


def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(0))

