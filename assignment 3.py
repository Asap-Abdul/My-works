```python
def check_eligibility():
    """
    Asks the user for their age and checks if they are 18 or older.
    """
    try:
        # Get age input from the user and convert it to an integer
        age = int(input("Please enter your age: "))
        
        # Check the condition
        if age >= 18:
            print("✅ You are eligible!")
        elif age < 0:
             print("❌ Invalid age entered.")
        else:
            print("🚫 You are not eligible (must be 18 or older).")
            
    except ValueError:
        # Handles cases where the user enters text instead of a number
        print("❌ Invalid input. Please enter a numerical age.")