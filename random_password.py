import random
import string
import os
clear = lambda: os.system("cls")

def generate_password(letters, nums, chars):
  generated_password = letters + nums + chars
  random.shuffle(generated_password)
  random_password = "".join(generated_password)
  return random_password

def main():
  clear()
  print("----------------------")
  print("| PASSWORD GENERATOR |")
  print("----------------------")

  options = input("""
1. Generate a random password by default.
2. Generate a personalized random password.

Type your choice: """)

  if options == "1":
    clear()
    password = generate_password(letters=random.sample(string.ascii_letters, 10), nums=random.sample(string.digits, 7), chars=random.sample(string.punctuation, 3))
    print(f"Your password is: {password}")
  elif options == "2":
    clear()
    random_letters = int(input("How many letters does your password have to be? "))
    random_nums = int(input("How many numbers does your password have to be? "))
    random_chars = int(input("How many chars does your password have to be? "))
    password = generate_password(letters=random.sample(string.ascii_letters, random_letters), nums=random.sample(string.digits, random_nums), chars=random.sample(string.punctuation, random_chars))
    print(f"Your password is: {password}")
  else:
    print("Error: Type a right option.")

if __name__ == "__main__":
  main()