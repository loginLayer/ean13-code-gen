import random

def generate_ean13():
    """
    Generates a random EAN-13 code.

    Returns:
        str: The generated EAN-13 code.
    """
    # Generate the first 12 random digits
    digits = [random.randint(0, 9) for _ in range(12)]

    # Calculate the check digit
    even_sum = sum(digits[-2::-2])
    odd_sum = sum(digits[-1::-2])
    total_sum = even_sum + odd_sum * 3
    check_digit = (10 - (total_sum % 10)) % 10

    # Add the check digit to the list
    digits.append(check_digit)

    # Convert the list of digits to an EAN-13 string
    ean13_code = ''.join(map(str, digits))

    return ean13_code

# Generate and print 10 EAN-13 codes on separate lines
print("EAN-13 Codes\n")
for _ in range(10):
    generated_code = generate_ean13()
    print(generated_code)
print("\nGitHub | @loginLayer FERNANDO ROJAS")
print("https://github.com/loginLayer")
