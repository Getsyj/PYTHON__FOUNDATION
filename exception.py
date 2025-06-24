try:
    balance = 1000
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive.")
    elif amount > balance:
        raise ValueError("Insufficient balance.")
except ValueError as ve:
    print("Transaction failed:", ve)
else:
    balance -= amount
    print(f"Transaction successful. Remaining balance: ₹{balance}")
finally:
    print("Thank you for banking with us.")
