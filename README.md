# 🔐 Multi-Step Encryption Tool

A Python-based program that applies **four layered cryptographic techniques** to encrypt a given message. The tool integrates Caesar Cipher, Rail Fence Cipher, Vigenère Cipher, and Vigenère Cipher with Autokey. The final encrypted result is also copied to your clipboard for convenience.

---

## ✨ Features

### 🔹 Step 1: Caesar Cipher

* Shifts each letter of the input message by a fixed key (**default: 3**) within the English alphabet.

### 🔹 Step 2: Rail Fence Cipher

* Applies a **zigzag transformation** with a default depth of **2**.

### 🔹 Step 3: Vigenère Cipher

* Encrypts the intermediate result using a fixed **Vigenère key: `YAYA`**.

### 🔹 Step 4: Vigenère Cipher with Autokey

* Enhances the Vigenère encryption by extending the key with the **plaintext itself**.

### 📋 Clipboard Integration

* Each result is **automatically copied to your clipboard** using the `pyperclip` library.

---

## ⚡ Prerequisites

* **Python 3.x**
* **pyperclip library** → Install via:

  ```bash
  pip install pyperclip
  ```

---

## 🚀 How to Use

1. **Clone or download** the project files to your machine.

   ```bash
   git clone https://github.com/your-username/multi-step-encryptor.git
   cd multi-step-encryptor
   ```

2. **Run the script** in your terminal:

   ```bash
   python encryptor.py
   ```

3. **Enter your message** when prompted. The program will:

   1. Apply the **Caesar Cipher**.
   2. Transform the result using the **Rail Fence Cipher**.
   3. Encrypt that output using the **Vigenère Cipher (`YAYA`)**.
   4. Perform an additional **Vigenère Cipher with Autokey**.
   5. Display each intermediate result and the final **fully encrypted text**.

4. Type `exit` anytime to quit the program.
