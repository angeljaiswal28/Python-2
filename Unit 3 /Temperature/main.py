# Importing functions from the updated module names
import Ctof.py
import ftoc.py
import ctok.py

def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("\nSelect an option (1-3): ")
    
    try:
        val = float(input("Enter temperature value: "))
        
        if choice == '1':
            print(f"{val}°C is equal to {c_to_f(val):.2f}°F")
        elif choice == '2':
            print(f"{val}°F is equal to {f_to_c(val):.2f}°C")
        elif choice == '3':
            print(f"{val}°C is equal to {c_to_k(val):.2f} K")
        else:
            print("Invalid selection. Please try again.")
            
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
  
