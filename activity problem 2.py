#ask user to input a message
encrypted_message = input(str("Please input an encrypted message"))
message = ""

#check each character
for i in range(len(encrypted_message)):
    
#This will change the symbol to their corresponding letter
    if encrypted_message[i] == "*":
        message += "a"
    elif encrypted_message[i] == "&":
        message += "e"
    elif encrypted_message[i] == "#":
        message += "i"
    elif encrypted_message[i] == "+":
        message += "o"
    elif encrypted_message[i] == "!":
        message += "u"
    else:
        message += encrypted_message[i]

#This will print the decrypted message   
print(message) 
