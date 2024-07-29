def dynamic_xor_encrypt(plaintext, text_key):
    print(plaintext)
    cipher_text = ""
    key_length = len(text_key) # length of the key

    
    # reverse and keeps track of i
    for i, char in enumerate(plaintext[::-1]): # for i, each char var

        key_char = text_key[i % key_length]
        
        #HERE
        encrypted_char = chr(ord(char) ^ ord(key_char))
        
        cipher_text += encrypted_char
        

    
    
    print('\n')
    text_key = text_key[::-1]
    # Reverse it back to picoCTF
    decrypted = ""
    for i, enc_char in enumerate(cipher_text[::-1]):
       
        key_char = text_key[i % key_length]

        
        
        decrypted_char = (ord(enc_char) ^ ord(key_char))
        decrypted += (chr(decrypted_char))
        


    
    
    
    
    
    
    
    
    return cipher_text




enc = dynamic_xor_encrypt("picoCTF", "trudeau")
