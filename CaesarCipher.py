alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

status = True
while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    def caesar(text, shift, direction):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)

                if direction == "encode":
                    cipher_index = index + shift
                    if cipher_index > 25:
                        cipher_index = cipher_index - 26

                elif direction == "decode":
                    cipher_index = index - shift
                    if cipher_index < 0:
                        cipher_index = cipher_index + 26

                cipher_text += alphabet[cipher_index]
            else:
                cipher_text += letter
        print(f"{cipher_text}")

    caesar(text, shift, direction)
    run = input("Would you like to use Cipher Caesar again?'y''n' ")
    if run == 'n':
        status = False
