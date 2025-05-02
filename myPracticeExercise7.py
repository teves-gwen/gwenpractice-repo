DISCOUNT_RATE = 0.10  

def input_products():
    order_list = []  

    while True:
        product_name = input("\nEnter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        total_price = calculate_price(price, quantity)  
        order_list.append((product_name, price, quantity, total_price))  

        add_item = input("\nDo you want to add another item? (y/n): ").lower()
        if add_item == "n":  
            break
        elif add_item != "y":
            print("\nInvalid input. Please enter y for 'yes' or n for 'no'.")

    total_amount, customer_name, senior_id = discount_privilege(order_list)  

    grand_total = calculate_discount(total_amount, senior_id)

    display_details(order_list, grand_total, customer_name, senior_id)

def calculate_price(price, quantity):
    return price * quantity

def discount_privilege(order_list):
    customer_name = input("\nEnter your name: ")
    senior_id = input("Enter your senior ID no. (Leave blank if not senior citizen): ").strip()

    total_amount = sum(item[3] for item in order_list) 

    return total_amount, customer_name, senior_id

def calculate_discount(total_amount, senior_id):
    discount = total_amount * DISCOUNT_RATE if senior_id else 0  
    return total_amount - discount  

def display_details(order_list, grand_total, customer_name, senior_id):
    print("\n******************************")
    print("\n       CUSTOMER RECEIPT      ")

    print("\n  = = = ORDER DETAILS = = =")
    for product_name, price, quantity, total in order_list:
        print(f"Product: {product_name}")
        print(f"Price: ₱{price}")
        print(f"Quantity: {quantity}")
        print(f"Total: ₱{total:.2f}\n")

    print("= = = CUSTOMER DETAILS = = =")
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No.: {'N/A' if not senior_id else senior_id}")

    print("\n     = = = BILL = = =")
    print(f"Grand Total: ₱{grand_total:.2f}")

input_products()
print("\nThank you for your order!")
print("\n******************************")
