import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

# def encrypt(text, shift):
#     encryptText = []
#     for x in text:
#         if x in alphabet:
#             encryptText.append(alphabet[(alphabet.index(x)+shift) % 26])
#         else:
#             encryptText.append(x)
#     encryption = "".join(encryptText)
#     print(f"Encoded text is {encryption}.")

# def decrypt(text, shift):
#     decryptText = []
#     for x in text:
#         if x in alphabet:
#             decryptText.append(alphabet[(alphabet.index(x)-shift) % 26])
#         else:
#             decryptText.append(x)
#     decryption = "".join(decryptText)
#     print(f"Decoded text is {decryption}.")


def caesar(text, shift, direction):
    codeText = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            codeText += alphabet[(alphabet.index(i)+shift) % 26]
        else:
            codeText += i
    print(f"The {direction}d text is {codeText}.")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    choice = input("Enter 'yes' to go again. Otherwise type 'no'.")
    if choice == 'no':
        break
