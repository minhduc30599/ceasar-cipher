from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > 26:
    shift = shift % 26

flag = True

def encrypt(t, s):
    t_array = [x for x in t]

    for i in range(0, len(t_array)):
        if t_array[i] in alphabet:
            index = alphabet.index(t_array[i])
            t_array[i] = alphabet[index + s]
        else:
            t_array[i] = t_array[i]
    t_string = "".join(t_array)
    print(t_string)

def decrypt(t, s):
    t_array = [x for x in t]

    for i in range(s):
        index = alphabet.index(t_array[i])
        t_array[i] = alphabet[index - s]
    t_string = "".join(t_array)
    print(t_string)

def ceasar(d, plain_t, plain_s):
    if direction == "encode":
        encrypt(t = plain_t, s = plain_s)    
    elif direction == "decode":
        decrypt(t = plain_t, s = plain_s) 
    else:
        print("Try again")

while flag:
    ceasar(d = direction, plain_t = text, plain_s = shift)

    yes_or_no = input("Type 'Yes' if you want to go again. Otherwise, type 'No':\n").lower() 

    if yes_or_no == 'no':
        flag = False
        print("Goodbye")  
