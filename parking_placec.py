while True:
    try:
        k = int(input("Enter a number (k): "))
        if k <= 0:
            print("Το k πρέπει να είναι θετικός ακέραιος. Δοκίμασε ξανά.")
            continue
        break
    except ValueError:
        print("Πρέπει να δώσεις ακέραιο αριθμό. Δοκίμασε ξανά.")

while True:
    try:
        parking_place = int(input("Enter parking place number: "))
        if parking_place <= 0:
            print("Ο αριθμός θέσης πρέπει να είναι θετικός ακέραιος. Δοκίμασε ξανά.")
            continue
        break
    except ValueError:
        print("Πρέπει να δώσεις ακέραιο αριθμό. Δοκίμασε ξανά.")

# Έλεγχος θέσης φόρτισης
if parking_place % k == 0 and parking_place % (k + 1) != 0:
    print("Yes")   # Είναι θέση φόρτισης
else:
    print("No")
