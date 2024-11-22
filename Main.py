import pyperclip

# Letters used in Caesar and Vigenère ciphers
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


while True:
    message = input("Enter Your Message to Encrypt (or type 'exit' to quit): ").upper()
    if message == "EXIT":
        print("Exiting the program...")
        break

    # Step 1: Caesar Cipher
    print("\nStep 1: Caesar Cipher")
    key = 3  
    caesar_result = ""
    
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol) + key
            if num >= len(letters):
                num -= len(letters)
            caesar_result += letters[num]
        else:
            caesar_result += symbol

    print(f"Caesar Cipher result: {caesar_result}")
    pyperclip.copy(caesar_result)

    # Step 2: Rail Fence Cipher
    print("\nStep 2: Rail Fence Cipher")
    depth = 2
    rail = [["" for _ in range(len(caesar_result))] for _ in range(depth)]
    direction_down = False
    row, col = 0, 0

    for char in caesar_result:
        if row == 0 or row == depth - 1:
            direction_down = not direction_down
        
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    rail_fence_result = ""
    for i in range(depth):
        for j in range(len(caesar_result)):
            if rail[i][j] != "":
                rail_fence_result += rail[i][j]

    print(f"Rail Fence Cipher result: {rail_fence_result}")
    pyperclip.copy(rail_fence_result)

    # Step 3: Vigenère Cipher
    print("\nStep 3: Vigenère Cipher")
    vigenere_key = "YAYA"  # Fixed Vigenère Cipher key
    key_index = 0
    vigenere_result = ""
    
    for symbol in rail_fence_result:
        if symbol in letters:
            shift = letters.find(vigenere_key[key_index])
            new_index = (letters.find(symbol) + shift) % len(letters)
            vigenere_result += letters[new_index]
            key_index = (key_index + 1) % len(vigenere_key)
        else:
            vigenere_result += symbol

    print(f"Vigenère Cipher result: {vigenere_result}")
    pyperclip.copy(vigenere_result)

    # Step 4: Vigenère Cipher with Autokey
    print("\nStep 4: Vigenère Cipher with Autokey")
    autokey = "YAYA" + rail_fence_result  # Fixed key plus plaintext
    autokey_result = ""
    
    for i in range(len(vigenere_result)):
        if vigenere_result[i] in letters:
            shift = letters.find(autokey[i])
            new_index = (letters.find(vigenere_result[i]) + shift) % len(letters)
            autokey_result += letters[new_index]
        else:
            autokey_result += vigenere_result[i]

    print(f"Vigenère Cipher with Autokey result: {autokey_result}")
    pyperclip.copy(autokey_result)

    # Final result
    print("\nThe final encrypted text is:")
    print(autokey_result)
