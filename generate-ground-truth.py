import os
import random
import pathlib
import subprocess

from time import sleep
from sys import exit
from shutil import rmtree

yesAnswers = ["", "y", "yes"]
noAnswers = ["n", "no"]

def yesno(msg):
    reply = input(f"{msg} [y/n]: ").casefold()
    
    if reply in yesAnswers: return True
    elif reply in noAnswers: return False

    print("Invalid yes/no answer!")
    return yesno(msg)

def divider():
    print("----------------------")

def register_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

base_name = input("Enter base name: ")
if not base_name:
    exit(0)

font_name = input("Enter font name: ")
if not font_name:
    exit(0)

use_fonts_dir = yesno("Do you want to use the data/fonts directory? (Note that text2image accepts only .ttf files)")

training_text_file = "data/training_text"

output_directory_base = "output"
output_directory = f"{output_directory_base}/{base_name}-ground-truth"

if yesno("Would you like to output the ground truth straight to the tesstrain data folder?"):
    new_output_directory = f"tesstrain/data/{base_name}-ground-truth"

    if os.path.exists(new_output_directory):
        if yesno(f"{new_output_directory} already exists. Overwrite?"):
            rmtree(new_output_directory)
            os.mkdir(new_output_directory)
            output_directory = new_output_directory
    else:
        output_directory = new_output_directory

# Register the base output directory
register_dir(output_directory_base)

# Register the output directory
if os.path.exists(output_directory):
    rmtree(output_directory)

os.mkdir(output_directory)

# Register the fonts directory
fonts_directory = os.path.join("data", "fonts")
if use_fonts_dir:
    register_dir(fonts_directory)
else:
    fonts_directory = ""

font_file = os.path.join(fonts_directory, f"{font_name}")

lines = []
with open(training_text_file, "r") as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

random.shuffle(lines)

try:
    max_count = int(input("Input max amount of training files to generate (defaults to 100): ")) or 100
except ValueError:
    max_count = 100

lines = lines[:max_count]

print("Generating tif/box files...")
divider()
print("---First generation---")

count = 0
for line in lines:
    base_filename = f"{base_name}.exp{count}"
    base_file = os.path.join(output_directory, base_filename)
    gt_file = f"{base_file}.gt.txt"

    with open(gt_file, 'w') as output_file:
        output_file.writelines([line])
    
    #print(f"  |--{base_filename}")

    stderr = subprocess.DEVNULL
    if count == 0:
        stderr = None

    result = subprocess.run([
        "text2image",
        f"--font={font_name}",
        f"--fonts_dir={fonts_directory}",
        f"--text={gt_file}",
        f"--outputbase={base_file}",
        "--max_pages=1",
        "--ptsize=32",
        "--leading=32",
        "--xsize=3600",
        "--ysize=480",
        "--resolution=500",
        "--char_spacing=1.0",
        "--unicharset_file=data/unicharset"
    ], stderr=stderr)

    if result.returncode == 1:
        divider()
        print("text2image returned exit code 1")
        print("Exiting...")
        exit(0)
    
    if count == 0:
        divider()
        print("Generating rest...")

    count += 1

divider()
print(f"Generated {count} ground truth sets")