#implementing Morse Code Translator
#creating a morse code chart
morse_code_list = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to encrypt the string according to the morse code chart
def encrypt(message):   # message stores the string to be encoded or decoded
    cipher = ''     #stores the morse translated form of the english string
    
    for letter in message:
        if letter != ' ':
 # Looks up the chart and adds the corresponding morse code with a space to separate morse codes for different characters
            
            cipher += morse_code_list [letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
 
# Function to decrypt the string from morse to english
def decrypt(message):
    # extra space added at the end to access the last morse code
    
    message += ' ' 
    decipher = ''   #stores the english translated form of the morse string
    citext = ''     #stores morse code of a single character
    
    for letter in message:
 
        # checking for space
        if (letter != ' '):
 
            #keeps count of the spaces between morse characters
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1, new character
            i += 1
 
            # if i = 2, new word
            if i == 2 :
 
                #separating words with a space
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(morse_code_list .keys())[list(morse_code_list .values()).index(citext)]
                citext = ''
 
    return decipher
 
def main():
    message = "HELLO WORLD 1234"
    result = encrypt(message.upper())
    print("Before encryption:   "+message)
    print ("Encrypted message:  "+result)
 
    message = "-.. .- .--. .... -.-- -.  ----- ----."
    result = decrypt(message)
    print ("Decrypted message:  " + result)
    
    #allowing user input
    
    message1 = input(print("Enter any message you wish to encrypt:  "))
    result1 = encrypt(message.upper())
    print("Before encryption:   "+message1)
    print ("Encrypted message:  "+result1)
    
    message2 = input(print("Enter any message you wish to decrypt:  "))
    result2 = decrypt(message.upper())
    print("Before decryption:   "+message2)
    print ("Decrypted message:  "+result2)
    
if __name__ == '__main__':
    main()
