#Creating an empty list to hold the grocery items
grocery_history = [];

#Assigning varible to manage the loop
stop = "go"

#Iterate until the user inputs the letter q to quit and stop the 'while' loop
while stop.lower() != "q":

#Now we'll get input from the user
   item_name = input("Item name:\n");
   quantity = input("Quantity purchased:\n");
   cost = input("Price per item:\n");
   
#This is where we add to the dictionary
   grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)};

#Now we are appending the list
   grocery_history.append(grocery_item);

#Asking our user if they want to keep shopping
   stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n");  

#This is our varible containing the grand total for the user
grand_total = 0;

#Iterating over grocery_history
for grocery_item in grocery_history:
   
#Printing information. Note usage of square brackets to access values.
   print(" %d %s @ $%.2f ea $%.2f " %(grocery_item['number'], grocery_item['name'], grocery_item['price'], (grocery_item['price'] * grocery_item['number'])));

#Getting the sum for grand_total
   grand_total += (grocery_item['price'] * grocery_item['number']);

#Now we can print the grand total!!!
print('Grand total: ${:.2f}'.format(grand_total))

