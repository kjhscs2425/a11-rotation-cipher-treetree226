import string


alphabet = string.ascii_lowercase
#comments out alphabet
# print(alphabet)

# password = "hi potato zzz"
# # eve wants to steal my password

# # make my password secret
# key = 4

# def encrypt(plaintext):
#     ciphertext = ""
#     for letter in plaintext:
#         old_position = alphabet.find(letter)
#         if old_position == -1:
#             ciphertext += " "
#         else:
#             new_position = old_position + key
#             new_position = new_position % len(alphabet)
#             new_letter = alphabet[new_position]
#             ciphertext += new_letter
#     return ciphertext

# print(encrypt(password))

# Your task:
# figure out what key I used to encrypt this message:
secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"

key1= 10
def decrypt(secret_message): #defining function
    realmessage= ""#empty variable
    for letter in secret_message:#goes through each letter and does something
        if letter==" ":
            realmessage+= " "
        else:
            old_position = alphabet.find(letter)#finds what letter is where in alphabet
            new_position = old_position + key1#makes new letter
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            realmessage += new_letter
        
    return realmessage
    
print(decrypt(secret_message))