# Program to check if pwer to 4

def powerOf8(number):

    count = 0

    if (number &(~(number& (number -1)))):

        while(number > 1):
            number >>=1
            count += 1

        if(count % 3 == 0):
            return True
        else:
            return False
        
number = int(input('enter your number'))
if(powerOf8(number)):
    print('\nthe number is power of 8')
else:
    print('\nthe number is not pwer of 8')