import string
import random
import argparse

def generate_password(len=12, upper=False, digits=False, special=False):
    chars = string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(len))

def main():
    parser = argparse.ArgumentParser(description="Generate random passwords")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    args = parser.parse_args()

    password = generate_password(args.length, args.uppercase, args.digits, args.special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
