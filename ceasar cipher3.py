def ceasar_cipher():
    ed = input ("\nType 'E' for encryption and 'D' for decryption:\n").lower()
    if ed == 'e':
        text= input ("\nEnter text for encryption, note(This will only encrypt alphabetic characters, special characters will remain as it is):\n ")
        
        shift = int(input("\nEnter shift key:\n"))
    
        encrypted_text= ""
        for i in text :
            if i. isalpha():
                if i. isupper():
                    base= 65
                else:
                    base= 97
                adjust_pos= chr((ord(i) - base + shift) % 26 + base)
                encrypted_text+= adjust_pos
                
            else:
                encrypted_text+= i
        print ("\nEncrypted text is:\n" ,encrypted_text)
    elif ed == 'd':   
        text= input("\nEnter text for decryption:   ")
        shift = int (input("\nEnter shift key :\n"))
        decrypted_text= ""
        for i in text:
            if i. isalpha():
                if i. isupper():
                    base = 65
                else:
                    base = 97
                adjust_pos = chr((ord (i) - base - shift ) % 26 +base)
                decrypted_text += adjust_pos
                
            else:
                 decrypted_text+= i
        print("\nDecrypted text is:\n", decrypted_text)
        
    else:
        print("\nEnter Valid Text:   ")

    ask_again= input("\nDo you want more try   (y/n):   \n").lower()
    if ask_again == 'y':
        
        ceasar_cipher()
    else:
        print("\nGood Bye:)")

ceasar_cipher()