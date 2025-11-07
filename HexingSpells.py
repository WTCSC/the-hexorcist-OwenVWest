import time # only used for typeout function


digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"# Valid digits for bases to use, used to check for valid inputs

def type_out(text, delay=0.01): # text to type and delay between characters
    """
    Used to make outputs easier to follow
    Takes a string input and prints every character on a set delay to make outputs slower and easier to follow
    Not required, Just my preference
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def to_decimal(num_str, base_orig):
    """
    Function use: Converting a number in the given base to base 10
    Function code provided from Notion classroom assignment description https://wtcsc.notion.site/Classroom-Dashboard-25367b69fe3a8002b0c1df716c744385?p=25067b69fe3a809cbe44cedcd6662376&pm=c
    """
    num_str = num_str.upper()
    total_value = 0
    power = 0
    for char in num_str[::-1]:
        char_value = digits.index(char)
        total_value += (char_value * (base_orig ** power))
        power += 1
    return total_value

def to_base(dec_num, targ_base):
    """
    Function use: Converts from base 10 to the requested base
    Function code provided from Notion classroom assignment description https://wtcsc.notion.site/Classroom-Dashboard-25367b69fe3a8002b0c1df716c744385?p=25067b69fe3a809cbe44cedcd6662376&pm=c
    """
    if dec_num == 0:
        return 0
    result_string = ""
    while dec_num > 0:
        remainder = dec_num % targ_base
        dec_num = dec_num // targ_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string

type_out("Welcome to The Hexorcist, Your held together with duct tape base converter\n---------------------------------\n\nEnter the number that you would like to convert: ") # Put multiple lines in one string to save space
num_in = input() # Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly

while all(char in num_in for char in digits): # Input validation: Checks if the provided number is a valid number in the given base
    type_out("The provided input is not a valid input for a number in base 2-36, \nplease provide a base 2-36 number (not case sensitive)\n")
    type_out("Enter the number that you would like to convert: ")
    num_in = input()# Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly

type_out("\nEnter the CURRENT base of the number (2-36): ")
base_in = input()# Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly

while base_in.isdigit() == False or int(base_in) > 36 or int(base_in) < 2: # Input validation: Checks if the number of the provided base is valid (2-36)
    type_out("The provided input is not a valid input for a base,\n please provide a number input between or including 2 and 36.")
    type_out("\nEnter the CURRENT base of the provided number (2-36): ")
    base_in = input()# Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly
base_in = int(base_in)

type_out("\nEnter the base you would like to convert to (2-36): ")
base_goto = input()# Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly

while base_goto.isdigit() == False or int(base_in) > 36 or int(base_in) < 2: # Input validation: Checks if the number of the provided base is valid (2-36)
    type_out("The provided input is not a valid input for a base,\n please provide a number input between or including 2 and 36.")
    type_out("\nEnter the base you would like to convert to (2-36): ")
    base_goto = input()# Inputs are on a seperate line than the string for the input because the typeout function is used instead of printing normaly
base_goto = int(base_goto)

type_out("\n\n------Calculating (with style)------\n\n") # Stylish

base10 = to_decimal(num_in, base_in) # Call function to convert input to base 10
final = to_base(base10, base_goto) # Call function to convert base 10 to requested base
type_out(f"{num_in} in base {base_in} converted to base {base_goto} is: {final}\n") # Final output