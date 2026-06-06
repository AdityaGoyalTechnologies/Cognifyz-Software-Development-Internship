# ==========================================
# Pattern Generator: Right-Angled Triangle
# ==========================================

# 1. Display a title and brief description
print("--- Right-Angled Number Triangle ---")
print("This program creates a right-angled triangle.")
print("Each row shows a sequence of numbers starting from 1 up to the current row number.\n")

# 2. Accept the number of rows from the user
# We use input() to get the value, and int() to convert that text into a whole number.
user_input = input("Enter the number of rows you want for your triangle: ")
row_count = int(user_input)

print("\nHere is your pattern:\n")

# 3. Generate the pattern using nested loops
# The outer loop determines the current row we are working on (from 1 to row_count)
for row in range(1, row_count + 1):
    
    # The inner loop determines what numbers to print on the current row
    # It prints numbers from 1 up to the current 'row' value
    for col in range(1, row + 1):
        # Print the column number. 
        # end=" " ensures the next number prints on the same line, separated by a space.
        print(col, end=" ")
        
    # After the inner loop finishes, we need to move to the next line for the next row.
    # A simple print() statement creates this newline.
    print()