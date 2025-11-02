import time
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def type_out(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def to_decimal(num_str, base_orig):
    num_str = num_str.upper()
    total_value = 0
    power = 0
    for char in num_str[::-1]:
        char_value = digits.index(char)
        total_value += (char_value * (base_orig ** power))
        power += 1
    return total_value

def to_base(dec_num, targ_base):
    if dec_num == 0:
        return 0
    result_string = ""
    while dec_num > 0:
        remainder = dec_num % targ_base
        dec_num = dec_num // targ_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string

type_out("Welcome to The Hexorcist, Your held together with duct tape base converter\n---------------------------------\n\nEnter the number that you would like to convert: ")
num_in = input()

while all(char in num_in for char in digits):
    type_out("The provided input is not a valid input for a number in base 2-36, \nplease provide a base 2-36 number (not case sensitive)\n")
    type_out("Enter the number that you would like to convert: ")
    num_in = input()

type_out("\nEnter the CURRENT base of the number (2-36): ")
base_in = input()

while base_in.isdigit() == False or int(base_in) > 36 or int(base_in) < 2: # input validation
    type_out("The provided input is not a valid input for a base,\n please provide a number input between or including 2 and 36.")
    type_out("\nEnter the CURRENT base of the provided number (2-36): ")
    base_in = input()
base_in = int(base_in)

type_out("\nEnter the base you would like to convert to (2-36): ")
base_goto = input()

while base_goto.isdigit() == False or int(base_in) > 36 or int(base_in) < 2: # input validation
    type_out("The provided input is not a valid input for a base,\n please provide a number input between or including 2 and 36.")
    type_out("\nEnter the base you would like to convert to (2-36): ")
    base_goto = input()
base_goto = int(base_goto)

type_out("\n\n------Calculating (with style)------\n\n")

base10 = to_decimal(num_in, base_in)
final = to_base(base10, base_goto)
type_out(f"{num_in} in base {base_in} converted to base {base_goto} is: {final}\n")