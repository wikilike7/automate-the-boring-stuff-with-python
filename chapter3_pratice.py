# collatz序列
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


try:
    while True:
        numbers = int(input('Enter a number >>> '))
        while numbers != 1:
            if numbers == 0:
                print(0)
                break
            numbers = collatz(numbers)
            print(int(numbers))
        break
except ValueError:
    print('Please enter a integer')
