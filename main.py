# Import op_math.py
import libs.op_math as m

# main function

def main():
    while True:
        try:
            # print menu
            print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

            # get user input menu
            choice = int(input("Enter your choice: "))
            
            # 5 option
            if choice == 5:
                print("Goodbye!")
                break

            # if user dont enter 1-5
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            # input number
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            # op maths
            if choice == 1:
                result = m.add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")

            elif choice == 2:
                result = m.subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")

            elif choice == 3:
                result = m.multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")

            elif choice == 4:
                try:
                    result = m.divide(num1, num2)
                    print(f"The result of {num1} / {num2} is: {result}")
                
                except ZeroDivisionError:
                    print("Ops! You can't divide by zero.")
                    continue

        except ValueError:
            print("Ops! Please enter a number.")

# Run the main function
if __name__ == "__main__":
    main()