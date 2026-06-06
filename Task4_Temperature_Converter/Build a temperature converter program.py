# ==========================================
# Temperature Converter Console Application
# ==========================================

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    """Main program loop and user interface."""
    print("--- Temperature Converter ---")
    
    # Continuous loop keeps the program running until the user types '3'
    while True:
        print("\nMenu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        # Check if the user wants to exit
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
            
        # Check if the user selected a valid conversion option
        elif choice == '1' or choice == '2':
            temp_input = input("Enter the temperature value: ").strip()
            
            # Validate that the user typed a number, not letters
            try:
                # float() allows for decimal numbers like 98.6
                temperature = float(temp_input)
            except ValueError:
                # Catch the error if float() fails to prevent a crash
                print("Error: Please enter a valid numeric temperature (e.g., 25 or 98.6).")
                continue  # Skip to the next iteration of the loop
                
            # Perform the calculation based on the user's menu choice
            if choice == '1':
                converted = celsius_to_fahrenheit(temperature)
                print(f"Result: {temperature}°C is equal to {converted:.2f}°F")
            elif choice == '2':
                converted = fahrenheit_to_celsius(temperature)
                print(f"Result: {temperature}°F is equal to {converted:.2f}°C")
                
        # Handle invalid menu selections
        else:
            print("Error: Invalid choice. Please select 1, 2, or 3.")

# This ensures the program runs automatically when the file is executed
if __name__ == "__main__":
    main()