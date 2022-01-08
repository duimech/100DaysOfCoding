# This program is based on the Caesar Cipher. Insert a message and shift the list to encode/decode it.
# Author: Ray Bolin
# Date: 1/7/2022
# 100DaysOfCoding

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '/', '?', ',', '.', '<', '>', ';', ':', "'", '"', '[', '{', ']', '}', '\\', '|', ' ']
again = "yes"

def caesar(direction, text, shift):
    direction = direction
    text = text.lower()
    shift = shift
    cipher_text = ""

    for letter in text:
        # Check to see if its letter, number, or symbol to use proper list
        is_letter = str.isalpha(letter)
        is_number = str.isnumeric(letter)
        if not is_letter and not is_number:
            is_symbol = True

        # alpha_index based on correct list
        if is_letter:
            alpha_index = alphabet.index(letter)
        elif is_number:
            alpha_index = numbers.index(letter)
        else:
            alpha_index = symbols.index(letter)

        # shift_letter based on moving right or left
        if direction == "encode":
            shift_letter = alpha_index + shift
        
        if direction == "decode":
            shift_letter = alpha_index - shift

        # modulo is based on the length of the list 
        if is_letter:
            shift_letter = shift_letter % 26
            cipher_text += alphabet[shift_letter]

        elif is_number:
            shift_letter = shift_letter % 10
            cipher_text += numbers[shift_letter]

        else:
            shift_letter = shift_letter % 31
            cipher_text += symbols[shift_letter]

    # print the results
    if direction == "encode":
        print(f"The encoded text is {cipher_text}")
    if direction == "decode":
        print(f"The decoded text is {cipher_text}")    
    
    
while again == "yes":

    direction = ""
    while direction != "encode" and direction != "decode":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    again = ""
    while again != "yes" and again != "no":
        again = str.lower(input("Type 'yes' if you want to go again. Otherwise type 'no':  "))

