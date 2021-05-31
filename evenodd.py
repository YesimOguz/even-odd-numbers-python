#We can use this code,if we want to know the numbers even or odd which users enter.

number = int(input('please enter a number: '))

result = number % 2

if result == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
