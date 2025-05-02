user_input = input("Enter a number: ")
int_user_input = int(user_input)

if int_user_input % 3 == 0 and int_user_input % 5 == 0:
    print("Bigyan ng jacket!")
elif int_user_input % 5 == 0:
    print("Horaaay!")
elif int_user_input % 3 == 0:   
    print("Hep! Hep!") 
else: 
    print(f"{int_user_input} Tawsan!")
