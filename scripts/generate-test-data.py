import os
import sys
from faker import Faker

try:
    dir_to_add_to = sys.argv[1]
    os.chdir("target_directory/"+ dir_to_add_to)
except IndexError:
    print("ERROR: must supply a directory as an argument. This directory will hold the new file.")
    exit()

fake = Faker('en-GB')
new_name = fake.name()
new_address = fake.address()

surname = new_name.split(" ")[-1]

with open(surname, 'w') as file:
    file.write(new_name)
    file.write("\n")
    file.write(new_address)
