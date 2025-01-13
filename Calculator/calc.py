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
print('For calculation use the following operators:')

operators = [
    '+ ~ Addition', 
    '- ~ Subtraction', 
    '* ~ Multiplication', 
    '/ ~ Division', 
    '// ~ Floor Division', 
    '% ~ Remainder', 
    '** ~ Exponentation', 
    'sqrt ~ Square Root', 
    'root ~ Nth-root', 
    'log ~ Natural Logarithm', 
    'log10 ~ Log(base10)', 
    'fac ~ Factorial', 
    'sin / cos / tan / sec / csc / cot ~ Trignometric Functions', 
    'asin / acos / atan / asec / acsc / acot ~ Inverse Trignometric Functions', 
    'rad ~ Radians to Degrees', 
    'deg ~ Degrees to Radian'
]
for operator in operators:
    print(operator)

# Input parsing
def get_input(prompt, is_angle=False, to_radians=False):
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
    '/': lambda a, b: a / b if b != 0 else 'Cannot divide by zero',
    '//': lambda a, b: mp.floor(a / b) if b != 0 else 'Cannot divide by zero',
    '%': lambda a, b: a % b if b != 0 else 'Cannot divide by zero',
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
    'rad': lambda a, _: mp.degrees(a),
    'deg': lambda a, _: mp.radians(a),
}

# Main calculation loop
while True:
    op = input('\nOPERATOR :- ').strip()
    
    if op in operations:
        # Handle single-input operations
        if op in ['sqrt', 'fac', 'log', 'log10', 'rad', 'deg']:
            num = get_input('NUMBER :- ' if op not in ['rad', 'deg'] else 'ANGLE :- ', is_angle=(op in ['rad', 'deg']), to_radians=False)
            result = operations[op](num, None)

        # Handle angle-based operations
        elif op in ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'asin', 'acos', 'atan', 'asec', 'acsc', 'acot']:
            angle = get_input('ANGLE (in degrees) :- ', is_angle=True, to_radians=True)
            result = operations[op](angle, None)

        # Handle binary operations
        else:
            num1 = get_input('NUMBER 1 :- ')
            num2 = get_input('NUMBER 2 :- ')
            result = operations[op](num1, num2)

        # Output
        print(f'\nRESULT: {result}')

    else:
        print("\nInvalid operator! Please use a valid operator.")
