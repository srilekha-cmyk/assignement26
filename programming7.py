balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")

# Output:
# Enter withdrawal amount: 1000
# Remaining Balance = 4000
