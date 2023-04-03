def generateKey(message, key): 
  key = list(key) 
  if len(message) == len(key): 
    return(key) 
  else: 
    for i in range(len(message) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 

def encryption(message, key):
    encrypted_text = []
    for i in range(len(message)):
        number_equivalent = (ord(message[i]) +ord(key[i])) % 26
        number_equivalent += ord('A')
        encrypted_text.append(chr(number_equivalent))
    return("" . join(encrypted_text))

if __name__ == "__main__": 
    message = input("Input a message you want to encrypt:")
    keyword = input("Please input a keyword to encrypt the message:")
    key = generateKey(message,keyword)
    encrypted_message = encryption(message, key)
    print("Message is", message)
    print("Encrypted message is", encrypted_message)