# Ceaser-Cipher
# 🔐 Caesar Cipher CLI Tool

A simple Python command-line Caesar Cipher encryption tool with **brute-force decryption** support. Built for learning, experimenting, and extending classical cryptography techniques.

---

## 🚀 Features

- ✅ Encrypt text using the Caesar Cipher  
- ✅ Brute-force decryption with all 26 possible shifts  
- 🛠️ Clean command-line interface using `argparse`  
- 🧪 Easily extendable for more complex ciphers (e.g., RSA planned)  
- 🧩 Future support for custom alphabets (partial ASCII sets)

---

## 🧠 What Is the Caesar Cipher?

The **Caesar Cipher** is a classic substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. For example, with a shift of 3:

```
Plaintext:  HELLO
Ciphertext: KHOOR
```

---

## 🖥️ Requirements

- Python 3.x

> No external libraries needed — uses only Python standard library (`argparse`, `string`)

---

## ⚙️ Usage

Clone the repository and run the script using command-line arguments.

```bash
python caesar.py --mode encrypt --text "HELLO" --shift 3
```

### 🔐 Encrypt Mode

Encrypt text with a specified shift:

```bash
python caesar.py -m encrypt -t "HELLO WORLD" -s 5
```

Output:
```
🔒 Encrypted (Shift 5): MJQQT BTWQI
```

### 🔓 Brute-Force Mode

Try all 26 shifts to help decode unknown ciphertext:

```bash
python caesar.py -m brute -t "KHOOR"
```

Output:
```
🔍 Brute-force Results:
Shift  0: KHOOR
Shift  1: LIPPS
Shift  2: MJQQT
...
Shift 25: JGNNQ
```

---

## 🧩 Planned Enhancements

- [x] Brute-force decryption support  
- [ ] Use custom/incomplete ASCII sets for the alphabet  
- [ ] Add RSA encryption/decryption logic  
- [ ] GUI or web-based Caesar Cipher playground

---

## 📁 Project Structure

```
caesar.py       # Main script file with encryption and brute-force logic
README.md       # Project documentation
```

---

## 🧑‍💻 Developer Notes

- The current implementation uses only uppercase letters (`A-Z`)  
- Non-alphabet characters (punctuation, digits) are preserved  
- Text is automatically converted to uppercase before encryption  
- Shift range is limited to `0-25` (modulo 26)

---

## 💡 Example Snippet (Encrypt Logic)

```python
def caesar_shift(text, shift):
    result = ""
    alphabet = string.ascii_uppercase

    for char in text.upper():
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % 26
            result += alphabet[idx]
        else:
            result += char
    return result
```


## 🏷️ License

This project is open-source and free to use.


## 🤝 Contributions

Pull requests are welcome! Feel free to fork the repo, suggest improvements, or help implement RSA and ASCII set customization.
