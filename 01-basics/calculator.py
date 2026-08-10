while True:
    try:
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
        operation = input("enter second operation (+,-,*,/):")

        if operation == '+':
         result = num1 + num2
        elif operation == '-':
         result = num1 - num2
        elif operation == '*':
         result = num1 * num2
        elif operation == '/':
         if num2 !=0:
           result = num1 / num2
         else:
           result = "error: division by zero"
        else: 
           result = " error: Invalid Operation"

        print("The result is:", result)   

    except ValueError: 
      print("This is not a valid number. Try again")

    again = input("Calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
