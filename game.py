#"A number-guessing game."
print('heller')

from random import randint
randint(1, 100)

#greet player 
print('greeting, playa!')

#player name
name = input('Enter your name: ')
print("Hello", name + "! I'm thinking of a number between 0-100. Try to guess my number!")

#Create a random number from 0 to 100
rand_num = random.randint(0, 100)
guess = True
num_guess = 0
smallest_guess = 100

#Player guess
n = random.randint(1, 100)
print(n)
guess = int(input("What's your guess? "))
number_of_tries=1;
while n != guess:
    
    number_of_tries = number_of_tries + 1; 
    
    if guess < n:
        print ("Your guess is too low");
        guess = int(input("What's your guess? "))
    elif guess > n:
        print ("Your guess is too high");
        guess = int(input("What's your Guess? "))
        
    else: 
        break
print ('Good job, ' + name + ' you guessed correctly in '+ str(number_of_tries) + ' tries');
    


    
   