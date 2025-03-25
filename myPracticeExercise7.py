DISCOUNT_RATE = 0.10 
total_amount = 0 

def input_products():
    order_list = []

    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        total_price = order_details(price, quantity) 
        order_list.append((product_name, price, quantity, total_price)) 

        add_item = input("Do you want to add another item? (yes/no): ").lower()
        if add_item == "no":  
            break
        elif add_item != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")

    discount = discount_privilege(order_list) 
    display_details(order_list, discount)

def order_details(price, quantity):
    return price * quantity

def discount_privilege(order_list):
    global customer_name, senior_id

    customer_name = input("Enter your name: ")
    senior_id = input("Enter your senior ID no. (Leave blank if not senior citizen): ").strip()

    for item in order_list:
        total_amount += item[3]  

    if senior_id:
        discount = total_amount * DISCOUNT_RATE  
    else:
        discount = 0  

    return total_amount - discount  

def display_details(order_list, grand_total):
    # Display each product in the order list
    print("\n===== ORDER DETAILS =====")
    for product_name, price, quantity, total in order_list:
        print(f"Product: {product_name}")
        print(f"Price: {price}")
        print(f"Quantity: {quantity}")
        print(f"Total: {total}\n")

    # Display customer details
    print("===== CUSTOMER DETAILS =====")
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No.: {'N/A' if not senior_id else senior_id}")

    # Display total amount
    print("===== BILL =====")
    print(f"Grand Total: {grand_total:.2f}")
    print("\nThank you for your order!")

input_products()


"""
Create a file called main.py. The program will ask the user for the following order details:
Product Name
Price
Quantity
After the last detail, it will ask if the user wants to add another item answerable by 
y for yes or n for no. If the user enters y, it will ask order details. 
Otherwise, it will proceed to the next step. After the orders are completed, 
the program will ask for the customer name and senior ID no.(blank if not senior citizen). 
If the customer is a senior citizen, a 10% discount will be deducted in the grand total. 
After that, the program will display the the following details:
Items(product name, price, quantity, total)
Customer Name
Senior ID No.
Grand Total
The challenge of this assignment is how you would split the problem into smaller problems 
and delegate these to all your team members. I should be able to see a significant contribution
for each team member not just adding a space or renaming variables and functions. 

Make use of # TODOs to ensure all the tasks are equally distributed. 
Start with designing your solution by thinking of the functions that will be 
involved and how it will integrate with one another including the problem it solves, 
the parameters it accepts, and the value it returns. Take note of the coding guidelines. 
Good luck!
"""


   
