alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(original_text, shift_amount):
    deciphered_text=''
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter)-shift_amount
            deciphered_text += alphabet[shifted_position]
        else:
            deciphered_text += letter
    print(f"Here is the decoded result: {deciphered_text}")


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

def ceaser(direction,original_text,shift):
    if direction=='encode':
        encrypt(original_text,shift)
    elif direction=='decode':
        decrypt(original_text,shift)

restart ='yes'
while restart=='yes':
    print("Welcome to Cypher coder, Get ready to pass the message")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction,text,shift)
    restart=input("Want to run the cipher logic once more (yes/no) :").lower()
    if restart=='no':
        print("End of logic")