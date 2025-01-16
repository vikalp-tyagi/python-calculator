'''
==============================
LICENSE AND COPYRIGHT NOTICE
==============================

python-calculator
Copyright (C) 2024 vikalp-tyagi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more information or to contact the author, please reach me at:
Email: vickyt.1309@gmail.com

See the GNU General Public License for more details:
Link: https://www.gnu.org/licenses/
'''

import mpmath as mp

# Operators
def operators():
    """Display the list of supported operators."""

    print("For calculation, use the following operators:")
    operators = [
        "+ ~ Addition",
        "- ~ Subtraction", 
        "* ~ Multiplication", 
        "/ ~ Division",
        "// ~ Floor Division", 
        "% ~ Remainder", 
        "** ~ Exponentiation",
        "sqrt ~ Square Root", 
        "root ~ Nth-root", 
        "log ~ Natural Logarithm",
        "log10 ~ Log(base10)", 
        "fac ~ Factorial",
        "sin / cos / tan / sec / csc / cot ~ Trigonometric Functions",
        "asin / acos / atan / asec / acsc / acot ~ Inverse Trigonometric Functions",
        "deg ~ Radians to Degrees", 
        "rad ~ Degrees to Radians"
    ]

    print("\n".join(operators))

# Input parsing
def get_input(prompt: str, is_angle: bool = False, to_radians: bool = False):
    """
    Parse user input and return a valid mpmath number.
    
    Args:
        prompt (str): The input prompt message.
        is_angle (bool): Whether the input is an angle.
        to_radians (bool): Whether to convert angles to radians.
    
    Returns:
        mp.mpc: Parsed real or complex number.
    """

    while True:
        try:
            value = input(prompt)
            parsed = mp.mpc(eval(value)) if 'j' in value else mp.mpf(value)
            return mp.radians(parsed) if is_angle and to_radians else parsed
        except Exception:
            print("Invalid input! Please enter a valid number.")

# Operation mapping
operations = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b, 
    '/': lambda a, b: a / b if b != 0 else 'Can\'t divide by zero',
    '//': lambda a, b: mp.floor(a / b) if b != 0 else 'Can\'t divide by zero',
    '%': lambda a, b: a % b if b != 0 else 'Can\'t divide by zero',
    '**': lambda a, b: a ** b,
    'sqrt': lambda a, _: mp.sqrt(a), 
    'root': lambda a, b: a ** (1 / b),
    'log': lambda a, _: mp.log(a), 
    'log10': lambda a, _: mp.log10(a),
    'fac': lambda a, _: mp.gamma(a + 1) if a.real >= 0 else 'Factorial not defined for negatives',
    'sin': lambda a, _: mp.sin(a), 
    'cos': lambda a, _: mp.cos(a), 
    'tan': lambda a, _: mp.tan(a),
    'sec': lambda a, _: 1 / mp.cos(a), 
    'csc': lambda a, _: 1 / mp.sin(a), 
    'cot': lambda a, _: 1 / mp.tan(a),
    'asin': lambda a, _: mp.degrees(mp.asin(a)), 
    'acos': lambda a, _: mp.degrees(mp.acos(a)),
    'atan': lambda a, _: mp.degrees(mp.atan(a)), 
    'asec': lambda a, _: mp.degrees(mp.asec(a)),
    'acsc': lambda a, _: mp.degrees(mp.acsc(a)), 
    'acot': lambda a, _: mp.degrees(mp.acot(a)),
    'deg': lambda a, _: mp.degrees(a), 
    'rad': lambda a, _: mp.radians(a),
}

# Main code  
def calculator():
    """Main calculation loop."""
    
    operators()

    while True:
        op = input("\nEnter an operator (or 'exit' to quit): ").strip().lower()
        
        if op == "exit":
            print("Goodbye!")
            break

        if op in operations:
            # Handle single-input operations
            if op in ['sqrt', 'fac', 'log', 'log10', 'rad', 'deg']:
                num = get_input("Enter a number: " if op not in ['rad', 'deg'] else "Enter an angle: ")
                result = operations[op](num, None)

            # Handle angle-based operations
            elif op in ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'asin', 'acos', 'atan', 'asec', 'acsc', 'acot']:
                angle = get_input("Enter an angle (in degrees): ", is_angle=True, to_radians=True)
                result = operations[op](angle, None)

            # Handle binary operations
            else:
                num1 = get_input("Enter the first number: ")
                num2 = get_input("Enter the second number: ")
                result = operations[op](num1, num2)

            # Output result
            print(f"\nResult: {result}")

        else:
            print("Invalid operator! Please choose a valid operator.")

# Run the calculator
if __name__ == "__main__":
    calculator()
