alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


Continue = True

while Continue:
    direction = input("Do your want to encrypt or decrypt : ").lower()
    message = input("Enter your message : ")
    shift = int(input("Enter the shift : "))
    message_list = []
    output = ""
    for n in message:
        message_list.append(n)
    for n in message_list:
        position = alphabet.index(n)
        if direction == "encrypt" :
            new_position = position + shift
            output += alphabet[new_position]
        elif direction == "decrypt" :
            new_position = position - shift
            output += alphabet[new_position]
        else:
            print("Oops wrong command , please recheck the direction command again....\n either type in encrypt or decrypt according to your need")
    print(f"Your message :: {output}")
    once_more = input("do you have another message to encrypt/decrypt (Y/N) : ").upper()
    if once_more == "N":
        Continue = False
        print("THANK YOU ... ")
    elif once_more == "Y":
        Continue = True
    else:
        print("Oops wrong command lets go once more.....")

