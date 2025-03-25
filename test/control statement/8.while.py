while True:
    num = float(input("Enter a number (or enter a negative number to stop) : "))
    if num < 0:
        print("Negative number entered, so the program stopped.")
        break
    print(f"You entered: {num}")


