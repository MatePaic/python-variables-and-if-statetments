secret = 10
guess = int(input('Guess the secret number: '))
if guess == secret:
    print('Congratulates, you guessed correctly')
else:
    print('Unfourtanetaly, your guess is wrong, try again. The secret number is not ' + str(guess))
