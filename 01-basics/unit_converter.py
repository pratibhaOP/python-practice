while True:
    try:
        choice = input("Convert c to f or f to c? ")
        if choice == "c to f":
            celsius = float(input("enter the number in celsius:"))
            fahrenheit = (celsius * 9/5) + 32
            print("Result", fahrenheit,"f")
        elif choice == "f to c":
            fahrenheit = float(input("enter the number in fahrenheit:"))
            celsius = (fahrenheit - 32) * 5/9  
            print("Result", celsius, "c")
        else:
            print("Invalid choice. Please type c to f or f to c")     
    except ValueError:
        print("That is not a valid number. Try again")

    again = input("convert again (y/N):")
    if again.lower() not in ["yes","ys","YES","YS","y","Y"]:
       print("Good bye!")
       break
   

        