#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    
    # Print the number of arguments and whether it's singular or plural
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")
    
    # Print each argument with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

