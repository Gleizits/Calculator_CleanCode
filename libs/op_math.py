# Basic math operations

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        print("Ops! You can't divide by zero.")
        return division(a, b)
    
# If user run this file
if __name__ == "__main__":
    print("Run the main.py file.")