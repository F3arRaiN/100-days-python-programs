from art import logo
def caesar():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    print(logo)
    print("Welcome to caesar cipher where your messages are encrypted with one of the most ancient methods of protecting text.")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
    def encrypt(original_text, shift_amount):

        # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
        #  by the shift amount and print the encrypted text.
        encrypted_text = ""

        for letter in original_text:
            if letter in alphabet:
                for pos in range(len(alphabet)):
                    if letter == alphabet[pos]:
                        new_pos = pos + int(shift_amount)

                        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

                        if new_pos > len(alphabet) - 1:
                            new_pos = new_pos % len(alphabet)
                        encrypted_text += alphabet[new_pos]
            else:
                encrypted_text += letter

        print(f"Encrypted text: {encrypted_text}")

    # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
    #  message.

    # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
    def decrypt(original_text, shift_amount):

        # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
        #  by the shift amount and print the decrypted text.
        org_word = ""
        for letter in original_text:
                if letter in alphabet:
                    for pos in range(len(alphabet)):
                        if letter == alphabet[pos]:
                            new_pos = pos - int(shift_amount)

                            # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

                            if new_pos > len(alphabet) - 1:
                                new_pos = new_pos % len(alphabet)
                            org_word += alphabet[new_pos]
                else:
                    org_word += letter

        print(f"Decrypted text: {org_word}")

    # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
    #  Use the value of the user chosen 'direction' variable to determine which functionality to use.

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Please enter a valid response.")


caesar()