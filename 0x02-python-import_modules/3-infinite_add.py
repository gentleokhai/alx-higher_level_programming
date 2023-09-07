#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Check if there are at least two arguments (the script name and one number)
    if len(sys.argv) < 2:
        print("Usage: python script.py num1 num2 ...")
    else:
        # Convert arguments to integers and sum them
        try:
            result = sum(int(arg) for arg in sys.argv[1:])
            print(result)
        except ValueError:
            print("Invalid input. All arguments must be integers.")

