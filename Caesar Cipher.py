alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

def Caesar(text, shift, direction):
    text_index = []
    cipher_text = []
    cipher_index = []
    
    if direction == "decode":
        shift *= -1
    for i in text:
        text_index = alphabet.index(i)
        cipher_index = text_index + shift
        cipher_index %= 25
        cipher_text += alphabet[cipher_index]
        cipher = "".join(cipher_text)
    print(f"The {direction}d text is: {cipher}")
    
Caesar(text, shift, direction)
