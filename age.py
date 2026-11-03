
try:
    age = int(input("Enter your age: "))
    
    if 18 <= age <= 22:
        print("Yes, you may participate in the activity.")
    else:
        print("No, you may not participate in the activity.")
        
except ValueError:
    print("Invalid input. Please enter a valid number.")
