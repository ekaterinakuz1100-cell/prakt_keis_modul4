"""Simple calculator module with CLI interface."""

import argparse
import sys

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Return a raised to power b."""
    return a ** b

def main():
    """Command-line interface for the calculator."""
    parser = argparse.ArgumentParser(description="Simple Calculator")
    
    # Создаём группу операций (обязательно выбрать одну)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--add', nargs=2, type=float, metavar=('A', 'B'),
                       help='Add two numbers')
    group.add_argument('--sub', nargs=2, type=float, metavar=('A', 'B'),
                       help='Subtract two numbers')
    group.add_argument('--mul', nargs=2, type=float, metavar=('A', 'B'),
                       help='Multiply two numbers')
    group.add_argument('--div', nargs=2, type=float, metavar=('A', 'B'),
                       help='Divide two numbers')
    group.add_argument('--pow', nargs=2, type=float, metavar=('A', 'B'),
                       help='Raise A to power B')
    
    args = parser.parse_args()
    
    try:
        if args.add:
            result = add(args.add[0], args.add[1])
            print(f"{args.add[0]} + {args.add[1]} = {result}")
        elif args.sub:
            result = subtract(args.sub[0], args.sub[1])
            print(f"{args.sub[0]} - {args.sub[1]} = {result}")
        elif args.mul:
            result = multiply(args.mul[0], args.mul[1])
            print(f"{args.mul[0]} × {args.mul[1]} = {result}")
        elif args.div:
            result = divide(args.div[0], args.div[1])
            print(f"{args.div[0]} ÷ {args.div[1]} = {result}")
        elif args.pow:
            result = power(args.pow[0], args.pow[1])
            print(f"{args.pow[0]} ^ {args.pow[1]} = {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
