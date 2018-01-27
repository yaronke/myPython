''' sequence from 1 to 100
   all numbers divisible by 3 have the string fizz printed instead of number
   all number divisible by 5 have the string buzz printed instead of number
   all number divisible by 3 and 5 have the string fizzbuzz printed instead of number'''


n = 20

for number in range(1, n +1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)