# Print 'Hello World'
print('Hello World')

# Print 7 as an integer
print(7)
# Print the sum of 9 and 3
print(9 + 3)
# Print '9 + 3' as a string
print('9 + 3')

# Print the result of 9 / 2
print(9 / 2)
# Print the result of 7 * 5
print(7 * 5)
# Print the remainder of 5 divided by 2 using %
print(5 % 2)

# Assign 'Bob' to the name variable
name = 'Bob'
# Print the value of the name variable
print(name)
print('Bob')
# Assign 7 to the number variable
number = 7
# Print the value of the number variable
print(number)
print(7)

apple_price = 2
apple_count = 8
# Assign the result of apple_price * apple_count to the total_price variable
total_price = apple_price * apple_count
# Print the value of the total_price variable
print(total_price)

money = 20
print(money)
# Add 50 to the money variable
money += 50
# Print the value of the money variable
print(money)

money = 20
print(money)
# Add 50 to the money variable
money += 50
# Print the value of the money variable
print(money)

age = 24
# Print 'I am 24 years old' using the age variable
print('I am ' + str(age) + ' years old')
count = '5'
# Convert the count variable to an integer data type, add 1 to it, and print it
print(int(count) + 1)

x = 7 * 10
y = 5 * 6
# if x equals 70, print 'x is 70'
if x == 70:
    print('x is 70')
# if y does not equal 40, print 'y is not 40' 
if y != 40:
    print('y is not 40')
    
x = 10
# if x is greater than 30, print 'x is greater than 30'
if x > 30:
    print('x is greater than 30')
money = 5
apple_price = 2
# if money is equal to or greater than apple_price, print 'You can buy an apple'
if money >= apple_price:
    print('You can buy an apple')
    
x = 10
# if x is greater than 30, print 'x is greater than 30'
if x > 30:
    print('x is greater than 30')
money = 5
apple_price = 2
# if money is equal to or greater than apple_price, print 'You can buy an apple'
if money >= apple_price:
    print('You can buy an apple')
    
money = 2
apple_price = 2
if money > apple_price:
    print('You can buy an apple')
# When the two variables have the same value, print 'You can buy an apple but your wallet is now empty'
elif money == apple_price:
    print('You can buy an apple but your wallet is now empty')
else:
    print('You do not have enough money')
    
x = 20
# if x ranges from 10 to 30 inclusive, print 'x ranges from 10 to 30'
if 10 <= x and x <= 30:
    print('x ranges from 10 to 30')
y = 60
# if y is less than 10 or greater than 30, print 'y is less than 10 or greater than 30'
if y < 10 or 30 < y:
    print('y is less than 10 or greater than 30')
z = 55
# if z is not equal to 77, print 'z is not 77'
if not z == 77:
    print('z is not 77')
    
# Assign 2 to apple_price variable
apple_price = 2
# Assign 5 to count variable
count = 5
# Assign the result of apple_price * count to total_price variable
total_price = apple_price * count
# By using the count variable, print 'You will buy .. apples'
print('You will buy ' + str(count) + ' apples')
# By using the total_price variable, print 'Your total is .. dollars'
print('The total price is ' + str(total_price) + ' dollars')

apple_price = 2
# Receive the number of apples by using input(), and assign it to the input_count variable 
input_count = input('How many apples do you want?: ')
# Convert the input_count variable to an integer, and assign it to the count variable
count = int(input_count)
total_price = apple_price * count
print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

apple_price = 2
# Assign 10 to the money variable
money = 10
input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count
print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')
# Add control flow based on the comparison of money and total_price
if money > total_price:
    print('You have bought ' + str(count) + ' apples')
    print('You have ' + str(money - total_price) + ' dollars left')
elif money == total_price:
    print('You have bought ' + str(count) + ' apples')
    print('Your wallet is now empty')
else:
    print('You do not have enough money')
    print('You cannot buy that many apples')

