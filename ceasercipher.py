import string
import argparse

#I will need to change the alphabet value to input of ascii length, like incomplete alphabets instead of the complete alphabets
#that will make it more advanced
#then I will create a code for RSA
# Caesar Cipher Logic
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

# Brute Force Caesar Cipher
def brute_force(text):
    print("\n🔍 Brute-force Results:")
    for shift in range(26):
        print(f"Shift {shift:2}: {caesar_shift(text, shift)}")

# CLI Argument Parser
def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Tool with Brute-Force Support")
    parser.add_argument("-m", "--mode", choices=["encrypt", "brute"], required=True, help="Choose 'encrypt' or 'brute'")
    parser.add_argument("-t", "--text", required=True, help="Text to encrypt or brute-force")
    parser.add_argument("-s", "--shift", type=int, help="Shift value (0-25) for encryption")

    args = parser.parse_args()

    if args.mode == "encrypt":
        if args.shift is None:
            print("❗ Please provide a shift value with -s for encryption.")
        elif 0 <= args.shift <= 25:
            encrypted = caesar_shift(args.text, args.shift)
            print(f"🔒 Encrypted (Shift {args.shift}): {encrypted}")
        else:
            print("❗ Shift must be between 0 and 25.")
    elif args.mode == "brute":
        brute_force(args.text)

if __name__ == "__main__":
    main()
