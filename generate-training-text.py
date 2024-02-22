import random
import os

output_file = "data/training_text"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Replace with relevant characters
chars = "1234567890/.,:[]()?!+-#"
chars += alphabet
chars += alphabet.upper()

try:
    num_samples = int(input("Input number of lines to generate [Defaults to 100]: "))
except ValueError:
    num_samples = 100

def generate_sample():
    # Generate a random string of characters
    sample_length = random.randint(5, 20)  # You can adjust the length range as needed
    sample = ''.join(random.choice(chars) for _ in range(sample_length))
    return sample

def main():
    if os.path.exists(output_file):
        overwrite = input("training_text.txt already exists. Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("Aborting operation.")
            return
    
    with open(output_file, "w") as f:
        for _ in range(num_samples):
            sample = generate_sample()
            f.write(sample)
            if _ != num_samples - 1:
                f.write("\n")  # Add newline character for all lines except the last one

if __name__ == "__main__":
    main()