# Assign a list of strings to the fruits variable
fruits = ['apple', 'banana', 'orange']
# Print the element at index 0 
print(fruits[0])
# Concatenate the string and the element at index 2, and print the result
print('I like ' + fruits[2] + 's')

fruits = ['apple', 'banana', 'orange']
# Add 'grape' to 'fruits'
fruits.append('grape')
# Print 'fruits'
print(fruits)
# Update the element at index 0
fruits[0] = 'cherry'
# Print the element at index 0
print(fruits[0])

# Define print_hand function
def print_hand():
    print('You picked: Rock')
# Call print_hand function
print_hand()

# Define the MenuItem class
class MenuItem:
    pass

class MenuItem:
    pass
# Create an instance of the MenuItem class
menu_item1 = MenuItem()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return self.name + ': $' + str(self.price)
    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return round(total_price)
# Import the MenuItem class using 'from' 'import'
from menu_item import MenuItem
# Inherit the MenuItem class and define the Food class
class Food(MenuItem):
    pass    
# Import the MenuItem class using 'from' 'import'
from menu_item import MenuItem
# Inherit the MenuItem class and define the Drink class
class Drink(MenuItem):
    pass
    
 


