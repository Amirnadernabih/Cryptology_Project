**Overview**

This program is a multi-step encryption tool that applies a combination of cryptographic techniques to encrypt a given message. The steps include the Caesar Cipher, Rail Fence Cipher, Vigenère Cipher, and Vigenère Cipher with Autokey. The final encrypted text is copied to the clipboard for easy use.

**Features**

**Step 1:** Caesar Cipher
Shifts each letter of the input message by a fixed key (default is 3) within the English alphabet.

**Step 2:** Rail Fence Cipher
Applies a rail fence (zigzag) transformation with a default depth of 2.

**Step 3:** Vigenère Cipher
Encrypts the result using a fixed Vigenère key (YAYA).

**Step 4:** Vigenère Cipher with Autokey
Enhances the Vigenère encryption by using the plaintext as part of the key.

**Clipboard Integration:**

The result of each step is automatically copied to the clipboard using the pyperclip library.

**Prerequisites**
Python 3.x
pyperclip library (Install using pip install pyperclip)

**How to Use**

1) Clone or download the project files to your local machine.
2) Run the Python script in your terminal:
   
              bash
              Copy code
              python encryptor.py
4) Enter your message when prompted. The program will:
			  1) Apply the Caesar Cipher to the message.
              2) Transform the result using the Rail Fence Cipher.
              3) Encrypt the Rail Fence output using the Vigenère Cipher with a fixed key.
              4) Perform an additional Vigenère Cipher with Autokey encryption.
              5) Each encryption step will display the intermediate result, and the final encrypted text will be shown at the end.

5) Type exit to quit the program.
